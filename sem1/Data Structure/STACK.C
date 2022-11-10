#include<stdio.h>
#include<conio.h>
#define SIZE 100
int stack[SIZE];
int top;
int a;
int choice;
void push();
void pop();
void print();
int main()
{
top=-1;
do
{
print("1.insert an element:\n2.delete an element\n3.display the element of the stack\n4.exit\n\n");
printf("enter your choice:");
scanf("%d",&choice);
switch(choice)
{
case 1:
push();
break;
case 2:
pop();
break;
case 3:
print();
break;
case 4:
exit(0);
break;
default:
printf("enter valid choice!");
break;
}
}while(choice!=4);
return 0;
}
void push()
{
int value;
if(top==SIZE-1)
{
printf("\n stack is empty");
}
else
{
printf("enter the element to be pushed:");
scanf("%d",&value);
printf("element added\n");
top++;
stack[top]=value;
}
}
void pop()
{
int value;
if(top==-1)
{
printf("stack empty");
}else
{
value=stack[top];
printf("deleted the element:%d\n",value);
printf("deleted\n");
top--;
}
}
void print()
{
if(top==-1)
{
printf("stack is empty\n");
}
else if(top=>0){
printf("elements are:");
for(a=top;a>=0;a--)
{
printf("%d\n",stack[a]);
}
}
}