#include<stdio.h>
#include<conio.h>
void main()
{
int a[10],b[10],c[10],s1,s2,s3,i,j,k,temp;
clrscr();
printf("enter the size of first array");
scanf("%d",&s1);
printf("enter the elements:");
for(i=0;i<s1;i++)
scanf("%d",&a[i]);

{
     printf("%d\t",a[i]);
}
for(i=0;i<s1-1;i++)
{
for(j=i+1;j<s1;j++)
{if(a[i]>a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
printf("\n enter the size of second array:");
scanf("%d",&s2);
printf("enter the elements:");
for(i=0;i<s2;i++)
scanf("%d",&b[i]);
{
printf("\t%d",b[i]);
}
for(i=0;i<s2-1;i++)
{
for(j=i+1;j<s2;j++)
{
if(b[i]>b[j])
{temp=b[i];
b[i]=b[j];
b[j]=temp;
}
}
}
s3=s1+s2;
i=0;j=0;k=0;
while(i<s1&&j<s2)
{
if(a[i]<=b[j])
{
c[k]=a[i];
k++;
i++;
}
else{
c[k]=b[j];
k++;
j++;
}
while(j<s2)
{
c[k]=b[j];
k++;
j++;
}
printf("merged array:");
for(i=0;i<s3;i++)
{printf("\t%d",c[i]);
}
getch();
}}




