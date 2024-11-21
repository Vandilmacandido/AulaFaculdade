#include<stdio.h>

int main(){
	
	char nome[10];
	float salario;
	
	printf("Digite o nome do fucionario: ");
	scanf("%s", &nome);
	
	printf("Digite o salario do fucionario: ");
	scanf("%f", &salario);
	
	printf("O fucionario %s recebe o valor de R$%.2f", nome , salario);
}
