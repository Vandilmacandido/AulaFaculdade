#include <stdio.h>

int main() {
    char nome[50];
    float salario, novoSalario;
    int anos;

    printf("Digite o nome do funcionário: ");
    scanf(" %[^\n]", nome); // Lê o nome, incluindo espaços
    printf("Digite o salário do funcionário: ");
    scanf("%f", &salario);
    printf("Digite quantos anos o funcionário tem na empresa: ");
    scanf("%d", &anos);

    // Calcula o novo salário com base nos anos de empresa
    if (anos <= 3) {
        novoSalario = salario * 1.03; 
    } else if (anos <= 10) {
        novoSalario = salario * 1.125; 
    } else {
        novoSalario = salario * 1.20; 
    }

    // resultado
    printf("\nNome do funcionário: %s\n", nome);
    printf("Salário antigo: R$ %.2f\n", salario);
    printf("Novo salário: R$ %.2f\n", novoSalario);

    return 0;
}

