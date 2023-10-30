#include <stdio.h>

/* ***** MAIN ******
        Función principal
        Ejemplo: Hola mundo!
*/
char var = 'a';
int numero = 2;
float dato = 4.56;

int main(void)
    {
        printf("\nHola mundo!\n\n"); //funciona como fstring (SIN \n incluido)
        puts("hola mundo"); //print() (con \n incluido)
        printf("texto %c texto %i texo...", var, numero); //%<tipo>
        return 0;
    }

/*  

-------------------- C -------------------- 30/10
codigo compilador ejecutable ejecucion

EJECUTABLE Y EJECUTAR:
----------------------
gcc -Wall -std=c17 -o ejecutable PC_13_C.c  
./ejecutable


TIPOS DE DATOS
--------------
* char -> caracter, 1 byte // unsignes char:[0,255] / char:[-128,127] (con signo)
* short -> 2 bytes // entero corto
* int -> 4 bytes 
* long -> 8

* float -> 4 // precision simple
* double -> 8 // precision doble

caracteres(char) 'A' '3' '\0' '\n' 
strins(char*) -> "a" (incluye \0) (OJO " != ')
enteros(int,short,long)
flotantes(float,double)

PALABRAS RESERVADAS
-------------------

DEFINIR VARIABLES
-----------------
<tipo> nombre = valor
*/

#define PI 3.1415926535 //constante

/*
DIRECTIVAS DEL PROCESADOR
-------------------------
if elif undef ifdef endif line ifndef include define ... 
*/

#include <stdio.h> //importar librerías
#define VALOR 16 //generar constantes o expresiones

/* 

INPUT
-----
scanf("%<formato>, &<variable>") 


ESTRUCTURAS DE CONTROL
----------------------
int main() {
if (condicion logica 0 o 1) {
    sentencia;
}
else if (condicion logica 0 o 1) {
    sentencia;
}
else
    sentencia;
    return 0; --> le devuelve un msg de todo ok

}
*/
int main() 
{
    int a = 2,b = 3;

    if (a == b) { //condiciones entre ()
        puts("a y b son iguales");
    }
    else if (a>b) {
        puts("a es mayor que b");
    }
    else {
        puts("a es menor que b");
    }
    return 0;

}

/*
SWITCH ()
---------
switch(<valor>){ //DEBE SER INT O CHAR
            case <expresión 1>:
                 <sentencias 1>
                break;
            case <expresión 2>:
                <sentencias 2>
                break;
            case <expresión 3>:
                <sentencias 3>
break; ...
            default:
                <sentencias por defecto>
                }
*/ 

int main(void) 
{
    int n;
    printf("Ingrese la opcion 1\n");
    scanf("%i",&n); //tiene q ser ENTERO (int o char)
    
    switch(n)
    {
        case 1:
            printf("Opcion 1\n");
            break;
        case 2:
            printf("Opcion 2\n");
            break;
        case 3:
            printf("Opcion 3\n");
            break;
        default:
        printf("Opcion desconocida\n");
    }
    return 0;
}

/*

WHILE
-----
while (<condicion>){ // se mantiene la iteracion mientras la condicion sea 1
  <sentencia_1>
  <sentencia_2>
}
*/
#include <stdio.h>
  int main(void)
  {
    int x = 0;
    while (x != 8)
    {
      printf("x vale %i\n", x);
      x++; //incrementa (en 1) / ++x = x++
      if (x == 5) {
        break; //condicion de corte
      }
    } 
    printf("x quedó en %i",x);
return 0; 
    }

// ++ = +1