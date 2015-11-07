// Parameters used by congruencial generators
typedef struct generator_parameters {
  long seed; // First value of Xi 
  long a; // Multiplicator
  long b; // Sesgo
  long mod; // Module
  long prev; // Previous random number (Xi)
} parameters;

// Mutiplicative generator
inline long mGenerator(parameters values) {
  return ((values.a*values.prev)%values.mod);
}

// Linear generator
inline long lGenerator(parameters values) {
  return (((values.a*values.prev)+values.b)%values.mod);
}

// More types of congruencial generators could be added
