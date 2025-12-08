#include <stdio.h>
#include <stdlib.h>

typedef struct Student_Info {
    char name[20];
    int sid;
    float cgpa;
} std;

typedef struct Teaching_Staff {
    char name[20];
    int tid;
    float salary;
} ts;

typedef struct Non_Teaching_Staff {
    char name[20];
    char role[20];  
    int id;
    float salary;
} nts;

int main() {
    int n_students, n_teaching, n_nonteaching;

    printf("Enter number of students: ");
    scanf("%d", &n_students);
    std students[n_students];

    printf("Enter number of teaching staff: ");
    scanf("%d", &n_teaching);
    ts teaching_staff[n_teaching];

    printf("Enter number of non-teaching staff: ");
    scanf("%d", &n_nonteaching);
    nts non_teaching_staff[n_nonteaching];

    for(int i = 0; i < n_students; i++) {
        printf("\nEnter details of student %d\n", i+1);
        printf("Name: ");
        scanf(" %[^\n]", students[i].name);
        printf("Student ID: ");
        scanf("%d", &students[i].sid);
        printf("CGPA: ");
        scanf("%f", &students[i].cgpa);
    }

    for(int i = 0; i < n_teaching; i++) {
        printf("\nEnter details of teaching staff %d\n", i+1);
        printf("Name: ");
        scanf(" %[^\n]", teaching_staff[i].name);
        printf("Teacher ID: ");
        scanf("%d", &teaching_staff[i].tid);
        printf("Salary: ");
        scanf("%f", &teaching_staff[i].salary);
    }

    for(int i = 0; i < n_nonteaching; i++) {
        printf("\nEnter details of non-teaching staff %d\n", i+1);
        printf("Name: ");
        scanf(" %[^\n]", non_teaching_staff[i].name);
        printf("Role: ");
        scanf(" %[^\n]", non_teaching_staff[i].role);
        printf("ID: ");
        scanf("%d", &non_teaching_staff[i].id);
        printf("Salary: ");
        scanf("%f", &non_teaching_staff[i].salary);
    }

    printf("\n--- Student Records ---\n");
    for(int i = 0; i < n_students; i++) {
        printf("Name: %s, ID: %d, CGPA: %.2f\n", students[i].name, students[i].sid, students[i].cgpa);
    }

    printf("\n--- Teaching Staff Records ---\n");
    for(int i = 0; i < n_teaching; i++) {
        printf("Name: %s, ID: %d, Salary: %.2f\n", teaching_staff[i].name, teaching_staff[i].tid, teaching_staff[i].salary);
    }

    printf("\n--- Non-Teaching Staff Records ---\n");
    for(int i = 0; i < n_nonteaching; i++) {
        printf("Name: %s, Role: %s, ID: %d, Salary: %.2f\n", non_teaching_staff[i].name, non_teaching_staff[i].role, non_teaching_staff[i].id, non_teaching_staff[i].salary);
    }

    return 0;
}
