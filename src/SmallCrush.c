#include "/opt/TestU01/include/ulcg.h"
#include "/opt/TestU01/include/unif01.h"
#include "/opt/TestU01/include/bbattery.h"
#include <stdlib.h>
#include <stdio.h>


int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("The arguments should be at least one\n");
    exit(1);
  }
  unif01_Gen *generator;
  generator = ulcg_CreateLCG2e31m1HD(16087, atol(argv[1]));

  //Set number of calls to 5000
  /* unif01_TimerRec timer; */
  /* timer.gen = generator; */
  /* timer.n = 200000; */

  bbattery_SmallCrush(generator);
  ulcg_DeleteGen(generator);
  
  return 0;
}
