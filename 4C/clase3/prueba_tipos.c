#include <stdio.h>

char variable = 0B01000001;

int main(int argc, char *argv[])
{
  // Vamos a ver: 'A'
  printf("Variable en formato char: %c\n", variable);
  
  // Vamos a ver: 65
  printf("Variable en formato int: %d\n", (int)variable);
}