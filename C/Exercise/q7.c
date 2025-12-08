/*
Write a program to check if the given number is a natural number.
*/

#include<stdio.h>

int fun_check_natural_number(int n){
    if(n>1){
        return 1;
    }
    else return 0;
}

int main(){
    int num;
    printf("Enter a number : ");
    scanf("%d",&num);

    int result = fun_check_natural_number(num);
    if(result ==1 ){
        printf("It is a Natural Number\n");
    }
    else printf("NOT natural number\n");

    return 0;
}