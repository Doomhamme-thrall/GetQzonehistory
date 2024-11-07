#include<stdio.h>
#include<stdlib.h>
typedef struct {
    int value;
    struct node *next;
    struct node *prev;
} node;

void insert(node *head, int value){
    node *new_node = (node *)malloc(sizeof(node));
    new_node->value = value;
    new_node->next = head->next;
    new_node->prev = head;
    head->next = new_node;
}

void delete(node *head, int value){
    node *current = head->next;
    while(current != NULL){
        if(current->value == value){
            current->prev->next = current->next;
            current->next->prev = current->prev;
            free(current);
            return;
        }
        current = current->next;
    }
}

void print(node *head){
    node *current = head->next;
    while(current != NULL){
        printf("%d\n", current->value);
        current = current->next;
    }
}


int main(){
    node *head = (node *)malloc(sizeof(node));
    head->next = NULL;
    head->prev = NULL;

    insert(head, 1);
    insert(head, 2);
    insert(head, 3);
    insert(head, 4);
    insert(head, 5);

    print(head);

    delete(head, 3);
    delete(head, 5);

    print(head);

    return 0;
}