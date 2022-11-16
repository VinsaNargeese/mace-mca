#include<stdio.h>
#include<conio.h>
void main()
{
int a[50],i,num,pos,n;
clrscr();
printf("enter the size of array:");
scanf("%d",&n);
printf("enter the array elements:");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
printf("enter the position to be deleted:");
scanf("%d",&pos);
for(i=pos-1;i<n-1;i++)
a[i]=a[i+1];
n=n-1;
printf("new array:");
for(i=0;i<n;i++)
printf("%d" "    ",a[i]);
getch();
}
