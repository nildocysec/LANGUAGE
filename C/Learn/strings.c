#include<stdio.h>
#include<string.h>


// NULL character is \0 terminate array forming a string
//gets(str)


void fun_print_string(char name[]){

    int i=0;
    while(name[i]!='\0'){
        printf("%c",name[i]);
        i++;
    }

}

void fun_fgets_puts_string(){

    char words[10];
//clear newline in buffer
    while(getchar()!='\n');
// fgets(str,n,fileName)
    fgets(words,10,stdin);
    puts(words);

}

int fun_string_length(char str[]){

    int length=0;
    for(int i=0;str[i]!='\0';i++){
        length++;
    }
    return length;
}

void fun_string_slice(char str[],int m,int n){
    
    int sliced_size=n-m+1;
    int j=0;
    char sliced_str[sliced_size];
    for(int i=m-1;i<=n-1;i++){
        sliced_str[j]=str[i];
        j++;
    }
    sliced_str[j]='\0';
    puts(sliced_str);

}

int main(){

    char name[] = {'n','i','l','\0'};
    char names[] = "nil ratri";

    fun_print_string(names);
    fun_print_string(name);    

    char word[10];
    printf("\nEnter a word : ");
    scanf("%s",word);
    printf("%s\n",word);

    printf("Enter Multi word string: ");
    fun_fgets_puts_string();    

//Can be reinitialized
    char *str = "Hello world";
//can not reinitialized
    char strr[]="hello world";
    puts(str);
    puts(strr);
    str="hell";
// strr="hell";
    puts(str);
//puts(strr);

    printf("lenght is : %d\n",fun_string_length(word));

//standard library functions
    printf("%d\n",strlen(str));

    char newstr[20]="newstr";
    char oldstr[]="oldstr";
    strcpy(newstr,oldstr);
    puts(newstr);

    strcat(newstr,oldstr);
    puts(newstr);

    char str1[]="world";
    char str2[]="World";
    printf("%d\n",strcmp(str1,str2));

    fun_string_slice(str1,2,4);

    return 0;
}