#include <stdio.h>

int main() {
    char nome[50];
    float salario, novoSalario;
    int anos;

    printf("Digite o nome do funcion�rio: ");
    scanf(" %[^\n]", nome); // L� o nome, incluindo espa�os
    printf("Digite o sal�rio do funcion�rio: ");
    scanf("%f", &salario);
    printf("Digite quantos anos o funcion�rio tem na empresa: ");
    scanf("%d", &anos);

    // Calcula o novo sal�rio com base nos anos de empresa
    if (anos <= 3) {
        novoSalario = salario * 1.03; 
    } else if (anos <= 10) {
        novoSalario = salario * 1.125; 
    } else {
        novoSalario = salario * 1.20; 
    }

    // resultado
    printf("\nNome do funcion�rio: %s\n", nome);
    printf("Sal�rio antigo: R$ %.2f\n", salario);
    printf("Novo sal�rio: R$ %.2f\n", novoSalario);

    return 0;
}

