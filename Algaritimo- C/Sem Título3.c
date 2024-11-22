#include <stdio.h>

int main(){
	
	char op;
	float x, y, resultado;
	
	printf("Digite um Numero: ");
	scanf("%f", &x);
	
	printf("Digite um Numero: ");
	scanf("%f", &y);
	
	getchar(); 
	printf("qual operação? + soma| - Subritação | * Mutiplicação | / divição");
	scanf("%f", &op);
	
	switch(op){
		case '+':
			resultado= x+y;
			printf("%f", resultado);
		break;
		case '-':
			resultado= x-y;
			printf("%f", resultado);
		break;
		case '*':
			resultado= x*y;
			printf("%f", resultado);
		break;
		case '/':
			if y == 0;
				printf("não pode ser dividido por 0");
			else
				resultado= x/y;
				printf("%f", resultado);
		break;
		default:
			printf("Operador invalido");
			break;
	}
	
	return 0;			
}
