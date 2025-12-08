#include<stdio.h>
#include<string.h>


typedef struct student{
    char name[10];
    int id;
    float cgpa;
}stud;

void fun_print_student_info(stud pcb[]){

    for(int i = 0; i < 3; i++) {
    
        printf("\nStudent %d:\n", i+1);
        printf("Name: %s", pcb[i].name);
        printf("ID: %d\n", pcb[i].id);
        printf("CGPA: %.2f\n", pcb[i].cgpa);
    }

}

int main(){

    struct student s1;
    strcpy(s1.name,"Nil");
    s1.id=1;
    s1.cgpa=9.9;

    printf("Name : %s\n",s1.name);
    printf("id : %d\n",s1.id);
    printf("cgpa is : %f\n",s1.cgpa);

    stud pcb[3];
    for(int i=0;i<3;i++){

        char str_name[10];
        fgets(str_name,10,stdin);
        strcpy(pcb[i].name,str_name);
        scanf("%d",&pcb[i].id);
        scanf("%f",&pcb[i].cgpa);
        while (getchar() != '\n');

    }

   fun_print_student_info(pcb);

    
    struct student *ptr = &s1;
    printf("id is : %d\n",(*ptr).id);
    printf("cgpa is : %f\n",ptr->id);

    return 0;

}