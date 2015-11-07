// Parameters used by congruencial generators
typedef struct generator_parameters {
  long seed; // First value of Xi 
  long a; // Multiplicator
  long b; // Sesgo
  long mod; // Module
  long prev; // Previous random number (Xi)
} parameters;

// Mutiplicative generator
long mGenerator(parameters values);

// Linear generator
long lGenerator(parameters values);

// More types of congruencial generators could be added
