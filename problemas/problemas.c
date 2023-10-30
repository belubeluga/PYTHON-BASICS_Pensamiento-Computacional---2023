/*
PROBLEMA 1
Implementar en C un código que calcule el área y perímetro de un c
írculo. Debe definir una constante con el número pi (al menos con 4 decimales), 
solicitar el ingreso del radio del círculo desde la terminal y luego 
imprimir un resumen con el área y perímetro calculados.
*/
#include <stdio.h>
#define PI 3.1415926535 //constante
int main(void) 
{
    int radio;
    printf("Ingrese el radio\n");
    scanf("%i",&radio);
    int area = (PI*radio*radio);
    printf("%i\n",area);
    return 0;
}

/*
mplemente un programa en C que imprima una tabla cuya primer columna sea el número de muestra 
generada y la segunda un número random. Tanto la cantidad de muestras a mostrar 
(largo de la tabla) como el máximo valor del número random (entre 0 y el máximo) serán ingresados 
por el usuario a través de la terminal. Por ejemplo:

Tabla random
************
Ingrese la cantidad de números totales: 6
Ingrese el máximo número random: 1500

Sample  Number
0       1281
1       103
2       1074
3       479
4       1164
5       499

*/