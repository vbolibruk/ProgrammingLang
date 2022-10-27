// Болібрук Влад
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int arrOfn[20];
    int arrOfx[20];
    int result;
    int a,b;
    for (int j = 0; j < 20; j++)
    {
        arrOfn[j] = j;
    }

    for (int j = -10; j < 10; j++)
    {
        arrOfx[j] = j;
    }
    for (int j = 0; j < 20; j++)
    {
        a +=  arrOfn[j] * arrOfx[j];
        b +=  arrOfn[j];
    }

    printf("task is A_9_278\n");
    printf("result is %d\n", a/b);

    return 0;
}
