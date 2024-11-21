#include <stdio.h>

int main() {
	
	float n1, n2, resultado;
	
	printf("digite a primeira nota: ");
	scanf("%f, &n1");
	printf("digite a segunda nota: ");
	scanf("%f, &n2");
	
	resultado= (n1+n2)/2;
	
	if (resultado >= 7){
		printf("Aprovado");
	}
	
	else {
		printf ("Reprovado");
	}
	
	return 0;
}
