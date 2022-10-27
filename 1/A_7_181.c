// Болібрук Влад
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int arrL = 11, j;
    int arrOfa[11] = {1, 2, 3, 4, 5, 6, 7, 8, 9, -5, -15};
    int sum = 0;

    for (int j = 0; j < arrL; j++)
    {
        int i = j * j;
        if ((arrOfa[j] % 5 == 0) && (arrOfa[j] % 2 != 0) && (arrOfa[j] < 0) && (abs(arrOfa[j]) < i))
        {
            sum += arrOfa[j];
        }
    }

    printf("task is A_7_181\n");
    printf("result  is %d\n", sum);

    return 0;
}
