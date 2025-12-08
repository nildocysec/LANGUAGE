/*
Write a program to print the smallest number of two.
*/

#include<stdio.h>

float fun_smallest_among_two(float a, float b){
    if(a>b){
        return b;
    }
    else return a;
}

int main(){
    float a,b;
    printf("enter two numbers\n");
    scanf("%f",&a);
    scanf("%f",&b);

    float smallest = fun_smallest_among_two(a,b);
    printf("Smallest numbers is : %f\n",smallest);

    return 0;
}