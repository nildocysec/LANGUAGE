/*
Write a program to check if a number is prime or not.
*/

#include<stdio.h>

int fun_check_prime_number(int n){
    for(int i=2;i<n;i++){
        if(n%i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int n;
    printf("Enter a number : ");
    scanf("%d",&n);

    int result = fun_check_prime_number(n);
    if(result==1){
        printf("Prime Number\n");
    }
    else printf("NOT prime number\n");

    return 0;

}