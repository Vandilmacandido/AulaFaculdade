#include <stdio.h>

int main(){
	
	char op;
	float x, y, resultado;
	
	printf("Digite um Numero: ");
	scanf("%f", &x);
	
	printf("Digite um Numero: ");
	scanf("%f", &y);
	
	getchar(); 
	printf("qual opera��o? + soma| - Subrita��o | * Mutiplica��o | / divi��o");
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
				printf("n�o pode ser dividido por 0");
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
