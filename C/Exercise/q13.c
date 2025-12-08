/*
Write a program in C to find the maximum number between two numbers using a pointer.
*/

#include<stdio.h>

float* fun_max_between_two(float* p1, float* p2){

    if(*p1 > *p2){
        return p1;
    }
    else return p2;

    }

int main(){

    float a,b;
    float *ptra = &a;
    float *ptrb = &b;

    printf("Enter two numbers : ");
    scanf("%f",ptra);
    scanf("%f",ptrb);

    float *ptr = fun_max_between_two(ptra,ptrb);
    printf("Max is : %f",*ptr);
    

    return 0;
}