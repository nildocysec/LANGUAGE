/*
Write a program to check if a given number is a Armstrong number or not.
*/

#include<stdio.h>
#include<math.h>

int fun_number_of_digit(int n){
    
    int digits=1;
    while(n/10 != 0){
        n=n/10;
        digits++;
    }

    return digits;
}



int fun_check_armstrong(int n){
    int num=n;
    int sum=0,remainder;
    int exp = fun_number_of_digit(n);

    while(n != 0){
        remainder = n%10;
        sum = sum + (int)pow(remainder,exp);
        n=n/10;

    }

    if(sum==num){
        return 1;
    }
    else return 0;

}

int main(){

    int n;
    printf("Enter number : ");
    scanf("%d",&n);

    int result = fun_check_armstrong(n);
    if(result==1){
        printf("%d is a armstrong number\n",n);
    }
    else printf("NOT a armstrong number\n");

    return 0;
}