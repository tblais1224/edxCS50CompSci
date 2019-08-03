// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>


#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

node *root;

int count = 0;

// returns index of char
int get_index(char c)
{
    if (c == '\'')
    {
        return 26;
    }
    else if (c >= 'a' && c <= 'z')
    {
        return c - 'a';
    }
    else if (c >= 'A' && c <= 'Z')
    {
        return c - 'A';
    }
    //error, not a-zA-Z char
    return -1;
}

// create an all NULL root / new node
node *create_node()
{
    // Initialize trie
    node *create_root = malloc(sizeof(node));
    // set end of word to false until changed
    create_root->is_word = false;
    // create a NULL node for each letter and \0
    for (int i = 0; i < 27; i++)
    {
        create_root->children[i] = NULL;
    }
    return create_root;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    int index;
    root = create_node();

    // open readable dictionary file
    FILE *dict_ptr = fopen(dictionary, "r");
    if (dict_ptr == NULL)
    {
        fprintf(stderr, "File empty\n");
        // Indicate failed
        return false;
    }

    //initialize root node as new_node
    node *new_node = root;
    
    char c_init = fgetc(dict_ptr);
    
    //initialize c to get chars one at a time from words in dict
    for (char c = c_init; c != EOF; c = fgetc(dict_ptr))
    {
        if (c != '\n')
        {
            //get characters index in tree
            index = get_index(c);
            // create new node if no child node with chars index
            if (new_node->children[index] == NULL)
            {
                // create a new node at the new_nodes child for the char test
                new_node->children[index] = create_node();
            }
            //set the new node equal to the child node just created
            new_node = new_node->children[index];
        }
        else
        {
            // mark end of word
            new_node->is_word = true;
            // add to word count
            count++;
            // set new_node back to the root node
            new_node = root;
        }
    }

    // Close dictionary
    fclose(dict_ptr);
    return true;
}


// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *new_node = root;
    // loop through each char of a word, set to 45 (max chars in word) because loop will break when not found in tree anyways
    for (int i = 0; i < 45; i++)
    {
        // check for end of word
        if (word[i] == '\0')
        {
            // if word is word is true ruten tru, else word isnt in dict so return false
            if (new_node->is_word == true)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        int index = get_index(word[i]);
        // if the childs index is false then word isnt in dict so return false
        if (new_node->children[index] == NULL)
        {
            return false;
        }
        // set node pointer to the child at the char index
        new_node = new_node->children[index];

    }
    return false;
}

bool unload2(node *new_node)
{
    for (int i = 0; i < 27; i++)
    {
        if (new_node->children[i] != NULL)
        {
            unload2(new_node->children[i]);
        }
    }
    free(new_node);
    return true;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    if (unload2(root))
    {
        return true;
    }
    return false;
}

