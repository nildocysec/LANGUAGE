/*
In an array of numbers, find how many times does a number 'x' occurs.
*/

#include<stdio.h>

int fun_frequency(int arr[], int size, int n){

    int count = 0;
    for(int i=0;i<size;i++){
        if(arr[i] == n){
            count++;
        }
    }

    return count;
}

int main(){
    int size,num;
    printf("Enter array size : ");
    scanf("%d",&size);

    int arr[size];
    printf("Enter array elements : \n");
    for(int i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }

    printf("Enter number : ");
    scanf("%d",&num);

    int frequency = fun_frequency(arr,size,num);
    printf("Frequency is : %d\n",frequency);

    return 0;
}