#include<stdio.h>

int main(){
	
	int numero;
	
	printf("Digite um numero: ");
	scanf("%d", &numero);
	
	int doblo = numero*2;
	float terco = numero/3;
	
	printf("O doblo de %d �: %d", numero, doblo);
	printf("A ter�a Parte de %.2f", numero, terco);
	
	
	
}
