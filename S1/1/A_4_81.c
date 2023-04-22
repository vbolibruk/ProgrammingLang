// Болібрук Влад 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {
		
	int x = 1;
	int a = 2;
	int n = 3;
    int j,result=1;

    if(n==1){
        result = ((x+a)*(x+a));
    }else{
        for( int j = 0; j < n; j++ ) {
            result = (result+2)*(result+2);
        }
    }
    result = result+2;

	printf("task is A_4_81\n");
	printf("result  is %d\n",result);

	return 0;	
}
