#include "../include/congruencial_generator.h"

// Mutiplicative generator
long mGenerator(parameters values) {
  return ((values.a*values.prev)%values.mod);
}

// Linear generator
long lGenerator(parameters values) {
  return (((values.a*values.prev)+values.b)%values.mod);
}

