#include <stdio.h>
#include <string.h>
/*
int main(void)
{
    char c = 'D';
    printf("%c\n",c); //char == valor de 1 byte (num o letra), 
    //q lo guarda como el valor de ASCII 
    // pero al pasarlo x un print, trata siempre de imprimirlo x num

}
//'' PARA LETRAS, "" PARA STRINGS
//size of --> cuantos bytes ocupa
*/

/*  EJERCICIO 1
*****************************************************
int main(void){
//CHAR-----------
    char c = 127; //[-128,127]
    c ++;
    printf("%d\n",c);// -128 (vuelve a empezar)

    unsigned char c2 = 255; //[0,255]
    c2 ++;
    printf("%ld\n",c2); // 0 (vuelve a empezar)
//SHORT------------
    //max = 2^16-1

//INT---------------
    //max 2^31-1        %lu (long unsignes)

//SHORT-------------
//LONG--------------
/* 
float -> 4 // precision simple -->menos precision
double -> 8 // precision doble *

} */

/*  EJERCICIO 2
*****************************************************
*/
float sumar(float a, float b){ // ACLARAR TIPOS!!
      float c;
c = a + b;
return c; }

float restar(float a, float b){ // ACLARAR TIPOS!!
      float c;
c = a - b;
return c; }

float mult(float a, float b){ // ACLARAR TIPOS!!
      float c;
c = a * b;
return c; }

float division(float a, float b){ // ACLARAR TIPOS!!
      float c;
c = a / b;
return c; }

int main(void){
    //short --> [-2**15,2**15 - 1]
    short x = 400;
    short y = -200;
    int suma;
    suma = sumar(x,y);
    int resta;
    resta = restar(x,y);
    int multiplicacion;
    multiplicacion = mult(x,y);
    int div;
    div = division(x,y);

    //printf("suma: %i, resta: %i, multiplicacion: %i, division: %i\n",suma,resta,multiplicacion,div);

    char n[100];
    printf("Elija la operación: ");
    scanf("%s",n);
    
    if (strcmp(n, "suma") == 0){
        printf("suma: %i\n",suma);
        }
    else if (strcmp(n, "resta") == 0){
        printf("resta: %i\n",resta);
        }
    else if (strcmp(n, "multiplicacion") == 0){
        printf("multiplicacion: %i\n",multiplicacion);
        }
    else if (strcmp(n, "division") == 0){
        printf("division: %i\n",div);
        }

    return 0;
}


