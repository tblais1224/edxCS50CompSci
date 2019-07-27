#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    char *alphabet[26] = {"a", "b", "c", "d", "e", "f","g", "h", "i","j", "k", "l","m", "n", "o","p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"};
    char *alphabetCaps[26] = {"A", "B", "C", "D", "E", "F","G", "H", "I","J", "K", "L","M", "N", "O","P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"};
    
    int key = 0;
    string plainText = "";
    key = get_int("Please input a number greater than 0: ");
    plainText = get_string("Please enter a string to be encrypted: ");
    int count = 0;
    while(plainText[count])
    {
        char character[2] = "\0";
        character[0] = plainText[count];
        char *newCharacter = character;
        for(int i = 0; i < 26; i++)
        {
            char *alphChar = alphabet[i];
            char *alphCharCap = alphabetCaps[i];
            if(newCharacter == alphChar)
            {
                printf("hi");
                int newIndex = i + key;
                if(newIndex < 26)
                {
                    newCharacter = alphabet[newIndex];
                }
                else
                {
                    int newerIndex = newIndex - 26;
                    newCharacter = alphabet[newIndex];
                }
                i = 26;
            }
            else if(character == alphCharCap)
            {
                int newIndex = i + key;
                if(newIndex < 26)
                {
                    newCharacter = alphabetCaps[newIndex];
                }
                else
                {
                    int newerIndex = newIndex - 26;
                    newCharacter = alphabetCaps[newIndex];
                };
                i = 26;
            };
        };
        printf("%s" , newCharacter);
        count++;
    }
}
