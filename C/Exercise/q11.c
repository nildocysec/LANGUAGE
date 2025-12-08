/*
Write a function to find sum of digits of a number.
*/

#include<stdio.h>

int fun_sum_of_digits(int n){
    
    int sum=0,remainder;
    while(n!=0){
        remainder=n%10;
        sum=sum+remainder;
        n=n/10;
    }

    return sum;
}

int main(){
    int n;
    printf("Enter a number : ");
    scanf("%d",&n);

    int sum = fun_sum_of_digits(n);
    printf("sum is : %d\n",sum);

    return 0;

}