#include <stdio.h>
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