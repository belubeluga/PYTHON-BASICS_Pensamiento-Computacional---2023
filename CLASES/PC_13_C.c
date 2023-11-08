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
* char -> caracter, 1 byte
    char:[-2^7,2^7-1] (con signo) / [-128,127]
    unsignes char:[0,255] / [0, 2^8-1]
* short -> 2 bytes // entero corto
    short:[-2^15,2^15-1]
    unsigned short: [0, 2^16-1]
* int -> 4 bytes 
    int: [-2^31,2^31-1] (cantidad de bits menos 1)
    unsigned int: [0,2^32-1]
* long -> 8
    long: [-2^63,2^63-1]
    unsigned long: [0,2^64-1] ---->unsigned UL

(cuantizacion no uniforme)
* float -> 4 // precision simple -->menos precision
* double -> 8 // precision doble
    largo: signo*mantisa* 2**exponente


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
        break; //condicion de corte (continue tmb funciona igual)
      }
    } 
    printf("x quedó en %i",x);
return 0; 
    }

// ++ = +1

/*
FOR
---
for (<exp_inicial>; <exp_condicion>; <exp_iteración>){
  <sentencia_1>
  <sentencia_2>
}
*/
#include <stdio.h>
int main(void)
{
    int n;
    for (n = 0; n < 10; n++)
    {
      printf("Iteración número %i\n",n);
    }
    return 0; 
}

/*
rand()
------
Devuelve un valor entero entre 0 y RAND_MAX (constante definida en stdlib.h). 
Todos los posibles números tienen la misma probabilidad de ocurrir (uniforme).

srand()
-------
Establece la semilla que rand() usará para generar números pseudo-aleatorios. 
Si no se fija una semilla, por defecto siempre será la misma, igual a 1.
#include <stdlib.h>

time()
------
(para q no se repita el num random del algoritmo y genere numeros random NUEVOS)
Permite obtener el tiempo actual en segundos, contado desde 
el 1 de enero de 1970 (timestamp de Unix).
Es útil para usar el tiempo actual como semilla de rand(), 
así el patrón aleatorio es siempre distinto.
#include <time.h>
*/

/*
PROBLEMA 1
Implementar en C un código que calcule el área y perímetro de un c
írculo. Debe definir una constante con el número pi (al menos con 4 decimales), 
solicitar el ingreso del radio del círculo desde la terminal y luego 
imprimir un resumen con el área y perímetro calculados.
*/



/*-------------------- C -------------------- 30/10
FUNCIONES
<tipo> <funcion>(<tipo> <arg1>, <tipo> <arg2>,....){
  <sentencia_1>
  <sentencia_2>
   return <valor_retorno>;
}

*/

#include <stdio.h>
   float sumar(float a, float b){ // ACLARAR TIPOS!!
      float c;
c = a + b;
return c; }
   int main(void)
   {
     float x = 5;
     float y = 25;
     float s;
     s = sumar(x,y);
     printf("resultado: x + y = %f\n", s);
     return 0;
}

/*
VOID
"sin tipo"
--> no devuelve nada
int func(void) (entra int y no devuelve nada)
void func(void)
*/
#include <stdio.h>
void menu(void){ //no recibe ni retorna nada
  printf("Ingrese una opción:\n");
  printf("[1] Fácil\n");
  printf("[2] Dificil\n");
  printf("[3] Salir\n");
}
int main(void){
  menu();
return 0; }

// DECLARACION
int function(int, int);
/* En la declaración se especifica solo el nombre, el tipo que devuelve 
y los tipos de los argumentos. 
Termina con punto y coma; */

//DEFINICION
int function(int x, int y){
}
/* En la definición se define el cuerpo de la función, es decir, 
las instrucciones que deberá ejecutar (entre llaves { }) */

void menu(void){
  puts("Ingrese una opción:");
  puts("[1] Fácil");
  puts("[2] Dificil");
  puts("[3] Salir");
}
int select(void){
  int op;
  scanf("%i",&op); // puntero
return op; }

// VARIABLES DE ALCANCE GLOBAL Y LOCAL

// ARCHIVOS.c
/*ARCHIVOS.h --> headers
directivas (no incluyen instructivos)
*/

//CONVERSION AUTOMATICA de tipos