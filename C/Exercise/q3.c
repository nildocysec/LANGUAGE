/*
Write a program to print the average of 3 numbers.
*/

#include<stdio.h>
 
float fun_average_of_three(float a, float b, float c){

    float average = (a+b+c)/3;
    return average;

}
int main(){

    float a,b,c;
    printf ("Enter three numbers\n");
    scanf("%f",&a);
    scanf("%f",&b);
    scanf("%f",&c);

    float average = fun_average_of_three(a,b,c);
    printf("Average is : %f : ",average);

    return 0;
}