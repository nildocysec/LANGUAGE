/*
Write a program in C to print the elements of an array in reverse order
*/

#include<stdio.h>

void fun_reverse_array(float arr[], int n){

    float temp;
    for(int i=0; i<n/2;i++){
        temp = arr[i];
        arr[i] = arr[n-1-i];
        arr[n-i-1] = temp;
    }

}

int main(){
    
    int n;
    printf("Enter size of array : ");
    scanf("%d",&n);

    float arr[n];

    for(int i=0; i<n; i++){
        scanf("%f",&arr[i]);
    } 

    fun_reverse_array(arr,n);
    printf("Reversed array is :\n");
    for(int i=0; i<n; i++){
        printf("%f\n",arr[i]);
    } 


    return 0;
}