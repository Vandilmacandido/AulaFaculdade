#include<stdio.h>

int main() {

	int x;
	int antes;
	int depois;

	printf("Digite um Numero: ");
	scanf("%d", &x);
	
	depois = x+1;
	antes = x-1;
	
	printf("antecessor: %d",antes);
	printf("\nsucessor: %d", depois);

	return 0;
}
