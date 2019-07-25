#include <cs50.h>
#include <stdio.h>
#include <string.h>

void splitInput(string plainText)
{
    string chars;
    chars=strtok(plainText, "");
    printf("hi   %s\n", chars);
    while (chars!= NULL)
    {
        printf ("im working     %s\n",chars);
        chars = strtok (NULL, ",:");
    }
}

int main(int argc, string argv[])
{
    string alphabet[26] = {"a", "b", "c", "d", "e", "f","g", "h", "i","j", "k", "l","m", "n", "o","p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"};
    string alphabetCaps[26] = {"A", "B", "C", "D", "E", "F","G", "H", "I","J", "K", "L","M", "N", "O","P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"};
    
    int key = 0;
    string plainText = "";
    key = get_int("Please input a number greater than 0: ");
    plainText = get_string("Please enter a string to be encrypted: ");
    printf("%d    %s\n", key, plainText);
    splitInput(plainText);
}
