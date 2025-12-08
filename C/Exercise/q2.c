/*
Take a number(n) from user & output its cube(n*n*n).
*/

#include<stdio.h>

float fun_cube(float n){

    float cube = n*n*n;
    return cube;
}

int main(){

    float n;
    printf("Enter a number : ");
    scanf("%f",&n);
    float cube = fun_cube(n);
    printf("cube is : %f\n",cube);

    return 0;
}