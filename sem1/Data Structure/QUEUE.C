#include<stdio.h>
#include<conio.h>
#define MAX 100
int front=-1,rear=-1;
int queue[MAX];
void insert();
void delet();
void print();
main(){
int choice;
clrscr();
while(1){
printf("1.insert\n2.delete\n3.display\n4.exit\nEnter your choice");
scanf("%d",&choice);
switch(choice)
{
case 1:insert();break;
case 2:delet();break;
case 3:print();break;
case 4:exit(0);break;
default:printf("\ninvalid choice");
break;
}
}
}
void insert()
{ int value;
printf("enter the element\n");
scanf("%d",&value);
if(rear==MAX-1)
{printf("queue is overflow");
}
if(front==-1 && rear==-1)
{
front=0;
rear=0;
}
else
{
rear=rear+1;
{
queue[rear]=value;
printf("\nelement inserted\n");
}
}
}
void delet()
{
if(front==-1||front>rear)
{printf("queue underflow");
return;
}
else
{printf("element deleted from queue is%d",queue[front]);
front=front+1;
}
}
void print()
{int i;
if(front==-1)
printf("empty");
else
{ printf("queue is:\n");
for(i=front;i<=rear;i++);
printf("%d""",queue[i]);
printf("\n");
}
}