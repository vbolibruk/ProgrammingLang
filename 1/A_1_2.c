// Болібрук Влад 
#include <stdio.h>
#include <stdlib.h>
int main() {
		
	int x = -1;
	int y = 1;
	
	float result = (abs(x)-abs(y))/(1+abs(x*y));
	
	printf("task is A_1_2\n");
	printf("result is %f\n",result);
	
	return 0;	
}
