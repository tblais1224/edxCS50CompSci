#include <cs50.h>
#include <stdio.h>
#include <crypt.h>
#include <string.h>


char *getSalt(char *hashPass)
{
    static char salt[3] = "\0";
    salt[0] = hashPass[0];
    salt[1] = hashPass[1];
    return salt;
}

bool bruteForce(char *salt, char *hashPass)
{
    string checkAlph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string newHash = "";
    int count = 0;
    char password[5] = "\0";
    
    //one digit
    for (int i = 0; i < 26 * 2; i++)
    {
        password[0] = checkAlph[i];
        newHash = crypt(password, salt);
        if (strcmp(newHash, hashPass) == 0)
        {
            printf("%s\n", password);
            return true;
        }
    }
    
    //two digits
    for (int i = 0; i < 26 * 2; i++)
    {
        password[0] = checkAlph[i];
        for (int k = 0; k < 26 * 2; k++)
        {
            password[1] = checkAlph[k];
            newHash = crypt(password, salt);
            if (strcmp(newHash, hashPass) == 0)
            {
                printf("%s\n", password);
                return true;
            }
        }
    }
    
    //three digits
    for (int i = 0; i < 26 * 2; i++)
    {
        password[0] = checkAlph[i];
        for (int k = 0; k < 26 * 2; k++)
        {
            password[1] = checkAlph[k];
            for (int l = 0; l < 26 * 2; l++)
            {
                password[2] = checkAlph[l];
                newHash = crypt(password, salt);
                if (strcmp(newHash, hashPass) == 0)
                {
                    printf("%s\n", password);
                    return true;
                }
            }
        }
    }
    
    //four digits
    for (int i = 0; i < 26 * 2; i++)
    {
        password[0] = checkAlph[i];
        for (int k = 0; k < 26 * 2; k++)
        {
            password[1] = checkAlph[k];
            for (int l = 0; l < 26 * 2; l++)
            {
                password[2] = checkAlph[l];
                for (int m = 0; m < 26 * 2; m++)
                {
                    password[3] = checkAlph[m];
                    newHash = crypt(password, salt);
                    if (strcmp(newHash, hashPass) == 0)
                    {
                        printf("%s\n", password);
                        return true;
                    }
                }
            }
        }
    }
    
    //five digits
    for (int i = 0; i < 26 * 2; i++)
    {
        password[0] = checkAlph[i];
        for (int k = 0; k < 26 * 2; k++)
        {
            password[1] = checkAlph[k];
            for (int l = 0; l < 26 * 2; l++)
            {
                password[2] = checkAlph[l];
                for (int m = 0; m < 26 * 2; m++)
                {
                    password[3] = checkAlph[m];
                    for (int n = 0; n < 26 * 2; n++)
                    {
                        password[4] = checkAlph[n];
                        newHash = crypt(password, salt);
                        if (strcmp(newHash, hashPass) == 0)
                        {
                            printf("%s\n", password);
                            return true;
                        }
                    }
                }
            }
        }
    }
    return false;
}

int main(int argc, string argv[])
{
    char *hashedPass;
    if (argc == 2)
    {
        hashedPass = argv[1];
    }
    else
    {
        return 1;
    }
    char *salt = getSalt(hashedPass);
    bruteForce(salt, hashedPass);
}
