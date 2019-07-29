#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    char alphabet[26] = "abcdefghijklmnopqrstuvwxyz";
    char alphabetCaps[26] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int key = 0;
    if(argv[1]>0)
    {
        key = atoi(argv[1]);
    }
    else
    {
        return 1;
    }
    
    string plainText = "";
//     key = get_int("Please input a number greater than 0: ");
    plainText = get_string("Please enter a string to be encrypted: ");
    int count = 0;
    printf("ciphertext: ");
    while (plainText[count])
    {
//         char *character[2] = "\0";
//         character[0] = plainText[count];
        char character = plainText[count];
        char newCharacter = character;
        for (int i = 0; i < 26; i++)
        {
            char alphChar = alphabet[i];
            char alphCharCap = alphabetCaps[i];
            if (plainText[count] == alphChar)
            {
                int newIndex = i + key;
                if (newIndex < 26)
                {
                    newCharacter = alphabet[newIndex];
                }
                else
                {
                    while(newIndex > 25)
                    {
                        newIndex = newIndex - 26;
                    };
                    newCharacter = alphabet[newIndex];
                }
                i = 26;
            }
            else if (plainText[count] == alphCharCap)
            {
                int newIndex = i + key;
                if (newIndex < 26)
                {
                    newCharacter = alphabetCaps[newIndex];
                }
                else
                {
                    int newerIndex = newIndex - 26;
                    newCharacter = alphabetCaps[newerIndex];
                };
                i = 26;
            };
        };
        printf("%c", newCharacter);
        count++;
    }
    printf("\n");
    return 0;
}
