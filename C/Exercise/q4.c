/*
Write a program to check if given character is digit or not.
*/

#include<stdio.h>

int fun_is_digit(char ch){

    if(ch>='0' && ch<='9'){
        return 1;
    }
    else return 0;

}

int main(){

    char ch;
    printf("Enter a character: ");
    scanf("%c",&ch);
    
    int result = fun_is_digit(ch);
    if(result==1){
        printf("%c is a digit\n",ch);
    }
    else {
        printf("%c is not a digit\n",ch);
    }

    return 0;

}