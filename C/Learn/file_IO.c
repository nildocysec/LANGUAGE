#include<stdio.h>

/*
    r=read
    w=write
    a=append
    rb=read in binary
    wb=write in binary
*/

int main(){

//FILE structure and file pointer
    FILE *fptr;

//Open file in read mode
    fptr=fopen("file1.txt","r");

//Check file exist
    if(fptr==NULL){
        printf("File DO NOT exist\n");
    }
    else{
        printf("File exist\n");
        fclose(fptr);
    }

//Read file
    fptr=fopen("file1.txt","r");
    char ch;
    fscanf(fptr,"%c",&ch);
    printf("%c",ch);
    fclose(fptr);

    //Write in file
    fptr=fopen("file1.txt","w");
    fprintf(fptr,"%C",'A');
    fclose(fptr);

//other method of write 
    fptr=fopen("file1.txt","w");
    fputc('B',fptr);
    fclose(fptr);

//other method of read
    fptr=fopen("file1.txt","r");
    printf("%c\n",fgetc(fptr));
    fclose(fptr);

//End Of File
    fptr=fopen("file1.txt","r");
    char ch;
    ch=fgetc(fptr);
    while(ch!=EOF){
        printf("%c",ch);
        ch=fgetc(fptr);
    }
    fclose(fptr);


    


    return 0;
}