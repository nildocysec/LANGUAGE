/*
Write a program to print the largest number in an array.
*/

#include<stdio.h>

int fun_largest_number(float arr[], int size){
    int index=0;
    for(int i=0;i<size-1;i++){
        if(arr[i+1]<arr[i]){
            index=i;
        }
        else index = i+1;
    }

    return index;
}

int main(){
    
    int size;
    printf("Enter array size : ");
    scanf("%d",&size);

    float arr[size];
    printf("Enter array elements : \n");
    for(int i=0;i<size;i++){
        scanf("%f",&arr[i]);
    }

    int index = fun_largest_number(arr,size);
    printf("largest number is : %f",arr[index]);

    return 0;

}
