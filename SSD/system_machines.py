import simpy
import random

SIM_TIME = 1000
RANDOM_SEED = 42
MEAN = 1.8
VAR = 0.2
NUM_MACHINES = 10
REPOSITORY = 3
NUM_REPAIRMEN = 3
MAX_EXPERIENCE = 1.65
MIN_EXPERIENCE = 0.55

# Constante que calcula la experiencia del operario
EXPERIENCE_PER_HOUR = (MAX_EXPERIENCE-MIN_EXPERIENCE)/SIM_TIME

class SystemMachine(object):
    def __init__(self, env):
        self.env = env
        self.machines = simpy.Resource(env, NUM_MACHINES)
        self.repairmen = simpy.Resource(env, NUM_REPAIRMEN)
        
def machine(env, name, system):
    # Espera hasta que se ocupar un recurso cuando esta disponible
    # y lo libera cuando lo deja (automaticamente)
    print('%s arrives to the system at %.2f.' % (name, env.now))
    while True:
        with system.machines.request() as request:
            yield request
            print('%s working at %.2f.' % (name, env.now))
            yield env.timeout(random.normalvariate(MEAN, VAR))
            print('%s has failed at %.2f.' % (name, env.now))

        with system.repairmen.request() as request:
            yield request
        
            #yield env.process(repairman(env, system))
            paramExponential = (EXPERIENCE_PER_HOUR*env.now)+MIN_EXPERIENCE
            yield env.timeout(random.expovariate(paramExponential))
            print('%s repaired at %.2f.' % (name, env.now))
                
# Create an environment and start the setup process
random.seed(RANDOM_SEED)
env = simpy.Environment()

system = SystemMachine(env)

# Create 13 machines
total_machines = NUM_MACHINES + REPOSITORY
for i in range(total_machines):
    env.process(machine(env, 'Machine %d' % i, system))

# Execute!
env.run(until=SIM_TIME)
    
