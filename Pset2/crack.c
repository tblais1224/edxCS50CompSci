#include <cs50.h>
#include <stdio.h>
#include <crypt.h>


// 50cI2vYkF0YU2   =  LOL

char *getSalt(char * hashPass)
{
    static char salt[3] = "\0";
    salt[0] = hashPass[0];
    salt[1] = hashPass[1];
    return salt;
}

int main(int argc, string argv[])
{
    char * hashedPass;
    if(argc == 2)
    {
        hashedPass = argv[1];
        printf("%s\n", hashedPass);
    }
    else
    {
        return 1;
    }
    char * salt = getSalt(hashedPass);
    char * test = crypt("LOL", salt);
    printf("%s   %s\n",salt, test);
}
