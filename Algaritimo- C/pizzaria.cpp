#include <stdio.h>

int main() {
    float valorTotal, desconto, valorComDesconto, valorPorPessoa;
    int quantidadePessoas;

    printf("Digite o valor total da conta: R$ ");
    scanf("%f", &valorTotal);

    printf("Digite a quantidade de pessoas: ");
    scanf("%d", &quantidadePessoas);

    printf("Digite o percentual de desconto (em %%): ");
    scanf("%f", &desconto);

    // Cálculo do valor com desconto
    valorComDesconto = valorTotal - (valorTotal * (desconto / 100));

    // Cálculo do valor por pessoa
    valorPorPessoa = valorComDesconto / quantidadePessoas;

    // resultados
    printf("\n--- Resultado ---\n");
    printf("Valor total com desconto: R$ %.2f\n", valorComDesconto);
    printf("Valor por pessoa: R$ %.2f\n", valorPorPessoa);

    return 0;
    
    }
