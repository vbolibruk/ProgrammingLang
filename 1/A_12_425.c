// Болібрук Влад
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float calculateRes(float a,float b);

int main()
{
    float s = -10;
    float t = 20;
    float result = calculateRes(1.2, s)+calculateRes(t, s) - calculateRes(2*s-1, s*t);


    printf("task is A_12_425\n");
    printf("result is %f\n", result);

    return 0;
}
float calculateRes(float a,float b){
    return ((a*a)+(b*b))/((a*a)+(2*a*b)+(3*b*b)+4);
}
