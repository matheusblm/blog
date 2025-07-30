#include <stdio.h>

static int a = 0;

void incrementar(void)
{
    int b = 0;        // variável local, alocação automática
    static int c = 0; // variável local, alocação estática
    printf("a: %d, b: %d, c: %d\n", a, b, c);
    a++;
    b++;
    c++;
}

int main(void)
{
    int i;
    for (i = 0; i < 5; i++)
        incrementar();
    // system("pause");
    return 0;
}