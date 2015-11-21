import simpy
import random

#### VARIABLES GLOBALES ###

SIM_TIME = 1000 # Tiempo de simulación
RANDOM_SEED = 42 # Semilla para la funciones de random
MEAN = 1.8 # Media de la Normal
VAR = 0.2  # Varianza de la Normal
NUM_MACHINES = 10 # Numero de maquinas en el sistema
REPOSITORY = 3 # Numero de maquinas en la reserva
NUM_REPAIRMEN = 3 # Numero de operarios
MAX_EXPERIENCE = 1.65 # Experiencia del operario al inciar la solucion
MIN_EXPERIENCE = 0.55 # Experiencia del operario al acabar la simulación

# Constante que calcula la experiencia del operario
EXPERIENCE_PER_HOUR = (MAX_EXPERIENCE-MIN_EXPERIENCE)/SIM_TIME

# Tiempo que tarda en fallar una maquina ~ N(1.8, 0.2)
def time_to_fail():
        return random.normalvariate(MEAN, VAR)

class Machine(object):
    # Constructor
    def __init__(self, env, name, system, repairman):
        self.env = env
        self.m_name = name

        # Se lanza el proceso que define el comportamiento de una máquina
        env.process(self.working(system, repairman))

    def time_to_fail(self):
        return random.normalvariate(MEAN, VAR)

    def working(self, system, repairman):
 
        while True:
            # Espera hasta que ocupa un recurso cuando esta disponible
            # y lo libera cuando lo deja (automaticamente)
            with system.request() as request:
                yield request        
                print('%s working at %.2f.' % (self.m_name, self.env.now))
                yield env.timeout(self.time_to_fail())
                print('%s has failed at %.2f.' % (self.m_name, env.now))

            # Una vez que se ha roto debe esperar a que haya algun operario libre
            with repairman.request() as request:
                yield request
                paramExponential = (EXPERIENCE_PER_HOUR*self.env.now)+MIN_EXPERIENCE
                yield self.env.timeout(random.expovariate(paramExponential))
                print('%s repaired at %.2f.' % (self.m_name, self.env.now))

# Proceso encargado de asegurar que siempre hay 10 maquinas en el sistema
def system_failing(env, system):
    while True:
        # Le he puesto un timeout "simbolico" para poder ponerlo en
        # un proceso aparte que monitorice
        yield env.timeout(0.5)
        if system.count < 10:
            print('System failed. It shoud be 10 machines working')
            exit()
        
# Create an environment and start the setup process
print('System started')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Creamos dos recursos: el sistema con espacio para diez máquinas y los tres operarios
system = simpy.Resource(env, capacity=NUM_MACHINES)
repairman = simpy.Resource(env, capacity=NUM_REPAIRMEN)

# Se crean 13 maquinas
total_machines = NUM_MACHINES + REPOSITORY
for i in range(total_machines):
    Machine(env, 'Machine %d' % i, system, repairman)

env.process(system_failing(env, system)
)
# Ejecuta la simulacion
env.run(until=SIM_TIME)
    
