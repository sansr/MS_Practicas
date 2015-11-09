////////////////////////////////////////////////////////
//                                                    //
// IMSL generator takes two arguments:                //
//   1- Amount of desired random values               //
//   2- Seed's value                                  //
//   3- File name to print the obtained random values //
//                                                    //
////////////////////////////////////////////////////////

#include "/opt/TestU01/include/ulcg.h"
#include "/opt/TestU01/include/unif01.h"
#include "/opt/TestU01/include/bbattery.h"
#include "../include/congruencial_generator.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


void _help(void) {
  printf("The number of arguments should be three\n");
  printf("Usage mode: imsl <AMOUNT_OF_RANDOM_VALUES> <SEED> <OUTPUT_FILE_NAME>\n");
  exit(1);
}

int main(int argc, char* argv[]) {
  // Check if imsl receives three arguments (amount of random numbers, seed and output file)
  if (argc != 4 || strcmp(argv[1],"--help") == 0) {
    _help();
  }

  if (atol(argv[1]) < 51320000) {
    printf("The amount of random values should be at least 51320000\n");
    exit(1);
  }
  
  // Define the parameters of the generator
  parameters values;
  values.seed = atol(argv[2]);
  values.a = 16807;
  values.b = 0; // Because imsl is multiplicative
  values.mod = pow(2,31)-1;
  values.prev = values.seed;
  
  // Call the generator to generate the desired amount
  // of random numbers indicated in the first argument
  long amount = atol(argv[1]);

  FILE *f = fopen(argv[3], "w+");
  if (f == NULL) {
    printf("Error opening file\n");
    exit(1);
  }
    
  for (long i = 0; i < amount; i++) {
    long Xi = mGenerator(values);
    values.prev = Xi;
    
    // Fit Xi to a Uniform[0,1)
    float u = (float)Xi/values.mod;

    // Write random numbers in a file 
    fprintf(f, "%f ", u);
  }
  
  // Tests
  bbattery_SmallCrushFile(argv[3]);
 
  return 0;
}
