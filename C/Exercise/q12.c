/*
Write a function to find square root of a number.
*/

#include<stdio.h>
#include<math.h>

float fun_square_root(int n){
    
    float root = sqrt(n);
    return root;

}

int main(){
    int n;
    printf("Enter a number : ");
    scanf("%d",&n);

    float square_root = fun_square_root(n);
    printf("square root is : %f\n",square_root);

    return 0;
}