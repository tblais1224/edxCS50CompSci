#include <stdio.h>
#include <cs50.h>
#include <math.h>

int lengthCheck(long cardNum)
{
    int counter = 0;
    while (cardNum > 0)
    {
        cardNum = cardNum / 10;
        counter += 1;
    };
    return counter;
};

// To get individual digits do num %10^digit place needed
string cardName(string name, long cardNum, int length)
{
    int length1 = length - 1;
    int length2 = length - 2;
    long firstPow = pow(10, length1);
    long secondPow = pow(10, length2);
    int firstDigit = cardNum / firstPow;
    int secondDigit = cardNum / secondPow;
    switch (length)
    {
        case 13:
            if (firstDigit == 4)
            {
                name = "VISA";
            }
            else
            {
                name = "INVALID";
            };
            return name;
        case 15:
            if (firstDigit == 3)
            {
                if (secondDigit == 34 || secondDigit == 37)
                {
                    name = "AMEX";
                }
                else
                {
                    name = "INVALID";
                };
            }
            else
            {
                name = "INVALID";
            };
            return name;
        case 16:
            if (firstDigit == 4)
            {
                name = "VISA";
            }
            else if (firstDigit == 5)
            {
                if (secondDigit >= 51 && secondDigit <= 55)
                {
                    name = "MASTERCARD";
                }
                else
                {
                    name = "INVALID";
                };
            }
            else
            {
                name = "INVALID";
            };
            return name;
        default:
            name = "INVALID";
            return name;
    };
};

string testNum(long cardNum, int length, string name)
{
    int total = 0;
    int lengthCopy = length;
    char arr[lengthCopy];
    while (lengthCopy--)
    {
        arr[lengthCopy] = cardNum % 10;
        cardNum /= 10;
    };
    int count = 1;
    for (int i = length - 1; i >= 0; i--)
    {
        if (count % 2 == 0)
        {
            int numDoubled = arr[i] * 2;
            if (numDoubled / 10 != 0)
            {
                int splitNumSum = (numDoubled % 10) + 1;
                total += splitNumSum;
            }
            else
            {
                total += numDoubled;
            }
        }
        else
        {
            total += arr[i];
        };
        count++;
    };
    if (total % 10 != 0)
    {
        name = ("INVALID");
    };
    return name;
};

int main(void)
{
    long cardNum = get_long("Please enter a valid credit car number: ");
    int length = lengthCheck(cardNum);
    string name = "";
    name = cardName(name, cardNum, length);
    string invalid = "INVALID";
    if (name == invalid)
    {
        printf("%s\n", name);
    }
    else
    {
        printf("%s\n", testNum(cardNum, length, name));
    };
};
