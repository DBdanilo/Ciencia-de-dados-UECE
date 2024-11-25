#include <stdio.h>

int main() {
    int d;
    const char *dias_semana[] = {
        "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira",
        "Quinta-feira", "Sexta-feira", "Sábado"
    };

    printf("Insira um valor de 1 a 7: \n");
    scanf("%d", &d);

    // Validação do valor inserido
    if (d >= 1 && d <= 7) {
        printf("%s.\n", dias_semana[d - 1]);
    } else {
        printf("Valor inválido! \n");
    }

    return 0;
}
