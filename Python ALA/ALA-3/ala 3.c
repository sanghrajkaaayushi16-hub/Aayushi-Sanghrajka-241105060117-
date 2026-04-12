#include<stdio.h>
int main(){
 int a=4, b=6, max;
 max = (a>b) ? a : b;
 while(1){
 if(max%a==0 && max%b==0){
 printf("LCM = %d\n", max);
 break;
 }
 max++;
 }
 return 0;
}