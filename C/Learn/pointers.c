#include<stdio.h>

int fun_square(int* num){
    
    *num = (*num)*(*num);
}

int fun_swap(int* a, int* b){

    int temp = *a;
    *a=*b;
    *b=temp;

}

int main(){

    int age =22;
    int *ptr =&age;
    int _age =*ptr;

    printf("%d\n",age);
    printf("%d\n",*ptr);
    printf("%d\n",_age);

    printf("%p\n",&age);
    printf("%p\n",ptr);
    printf("%p\n",&ptr);

    printf("%u\n",&age);
    printf("%u\n",ptr);
    printf("%u\n",&ptr);

    int **pptr = &ptr;
    printf("%d\n",**pptr);
    printf("%d\n",*pptr);

    fun_square(ptr);
    printf("%d\n",age);

    int a=1; int b=0;
    fun_swap(&a,&b);
    printf("%d and %d\n",a,b);

    int *ptra=&a; int *ptrb=&b;
    printf("%u\n",ptra);
    printf("%u\n",ptra+1);

    printf("%u\n",ptrb);
    printf("%d\n",ptra-ptrb);


    

    return 0;
}