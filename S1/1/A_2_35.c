// Болібрук Влад 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int minF(int a,int b);
int maxF(int a,int b);
int main() {
		
	int x = 1;
	int y = 2;
	int z = 3;

    int sum = x+y+z;
    int mult = x*y*z;
	int max = maxF(sum,mult);
	int min = (minF(x+y+z/2,x*y*z)*minF(x+y+z/2,x*y*z))+1;

	printf("task is A_2_35\n");
	printf("result max is %d\n",max);
	printf("result min is %d\n",min);

	return 0;	
}

int minF(int a,int b){
    return (a>b) ? b : a ;
}
int maxF(int a,int b){
    return (a>b) ? a : b ;
}