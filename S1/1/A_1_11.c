// Болібрук Влад 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main() {
		
	int x = 1;
	int y = 2;
	int z = 3;

	float resultA = (sqrt(abs(x-1)) - pow(abs(y),1/3))/(1+(x*x)/2+(y*y)/4);
	float resultB = x*(atan(z)+ exp(-(x+3)));

	printf("task is A_1_11\n");
	printf("result is %f\n",resultA);
	printf("result is %f\n",resultB);

	return 0;	
}
