/*
Write a program to calculate perimeter of rectangle. Take sides, a & b, from the user.
*/


#include<stdio.h>

float fun_perimeter_rectangle(float a, float b){

    float perimeter = 2*(a+b);
    return perimeter;

}

int main(){

    float a,b;
    printf("Enter side a : ");
    scanf("%f",&a);
    printf("Enter side b : ");
    scanf("%f",&b);

    float perimeter = fun_perimeter_rectangle(a,b);
    printf("perimeter is : %f\n",perimeter);


    return 0;
}