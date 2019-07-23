#include <stdio.h>
#include <cs50.h>
#include <math.h>

int lengthCheck(long cardNum){
    int counter = 0;
    while(cardNum>0){
        cardNum = cardNum/10;
        counter+=1;
    }; 
    return counter;
};

//to get individual digits do num %10^digit place needed
string cardName(long cardNum, int length){
    int firstDigit = cardNum % pow(10, length);
    int secondDigit = cardNum % pow(10, length-1)
    string name = ""
    switch(length){
        case 13:
            if(firstDigit == 4){
                name = "VISA";
            }else{
                name = "INVALID";
            };
            return name;
        case 15:
            if(firstDigit == 3){
                if(secondDigit == 4 || secondDigit == 7){
                    name = "AMEX";
                }else{
                 name = "INVALID";
                };
            }else{
            name = "INVALID";
            };
            return name;
        case 16:
            if(firstDigit == 4){
                name = "VISA";
            }else if(firstDigit == 4){
                if(secondDigit <= 1 && secondDigit >= 5){
                    name = "MASTERCARD"
                }else{
                name = "INVALID";
                };
            }else{
                name = "INVALID";
            };
            return name;
        default:
            name = "INVALID";
            return name;
    };
};

int main(void){
    long cardNum = get_long("Please enter a valid credit car number: ");
    int length = lengthCheck(cardNum);
    string cardName =  cardName(cardNum, length);
    printf("%ld\n%d\n%s\n",cardNum, length, cardName);
}
