#include<stdio.h>

 int fun_array( char arr[], int size){
    
    for(int i=0;i<size;i++){
        printf("%c\t",arr[i]);
    }
    
    return 0;        
}

int fun_reverse_array(int arr[], int size){

    int temp;
    for(int i=0;i<size/2;i++){
        temp=arr[i];
        arr[i]=arr[size-i-1];
        arr[size-i-1]=temp;
    }

    return 0;
}

int main(){

    char name[]={'n','i','l'};

    for(int i=0;i<3;i++){
        printf("%c\t",name[i]);
    }

    //int *ptr = arrayName == int *ptr = &array[0]

    fun_array(name,3);  
  /*  
    int m,n,i,j;
    printf("Enter size of arrays\n");
    scanf("%d",&m);
    scanf("%d",&n);
    int arr2d[m][n];

    printf("Enter elements\n");
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            scanf("%d",&arr2d[i][j]);
        }
    }

    for(i=0;i<m;i++){
        printf("\n");
        for(j=0;j<n;j++){
            printf("%d\t",arr2d[i][j]);
        }
    }

*/

    int arr[5] = {1,2,3,4,5};
    fun_reverse_array(arr,5);
    for(int i=0;i<5;i++){
        printf("%d\t",arr[i]);
    }
    
    

    return 0;
}