/*
Write a program to insert an element at the end of an array
*/

#include<stdio.h>

int fun_insert_element(char arr[], int size, char element){
    
    arr[size]=element;
    size=size+1;
    return size;
}

int main(){

    int size;
    printf("Enter array size : ");
    scanf("%d",&size);

    char arr[size];
    printf("Enter array elements : \n");
    for(int i=0;i<size;i++){
        scanf(" %c",&arr[i]);
    }

    char element;
    printf("Enter new element : ");
    scanf(" %c",&element);

    size=fun_insert_element(arr,size,element);

    printf("New array elements : \n");
    for(int i=0;i<size;i++){
        printf("%c\t",arr[i]);
    }    

    return 0;
}