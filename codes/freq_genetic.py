import random
from chromosome import Chromosome
from import_code import Import_Code
import scipy.io

dim = 39
quite = False

class GeneNetwork(object):
    
    def __init__(self, dim, chromosome_length, weight_list, i, source, destination):
        #initializing all member variables
        if source >= dim or destination >= dim:
            raise ValueError
        self.chromosome_length = chromosome_length
        self.dim = dim
        
        self.distance = matrices.distance
        self.time = matrices.time
        self.availability = matrices.availability
        self.normal_dist = self.norm_dist(self.distance)
        self.normal_time = self.norm_time(self.time)
        self.normal_avail = self.norm_avail(self.availability)
        
        self.source = source
        self.destination = destination
        self.population = []
        self.population_size = 0
        self.results = []
        self.best = None
        self.weight_list = weight_list
        self.i = i
        #weights from external weight list
        self.w1 = self.weight_list[i][0]
        self.w2 = self.weight_list[i][1]
        self.w3 = self.weight_list[i][2]

    def start(self, gen_max, pop_size):
        #function to start the genetic algorithm
        
        #from first generation
        gen = 1  
        
        #generate initial population
        self.generate_population(pop_size)
        self.population_size = pop_size

        while gen <= gen_max:
            gen += 1
            p = 1
            new_population = list()
            
            while p <= self.population_size:
                p += 1
                #taking two chromosomes at a time
                parents = random.sample(range(self.population_size), 2)
                #calling the random crossover function
                newbie = self.crossover(self.population[parents[0]], self.population[parents[1]])
                #calling the random mutation function
                newbie.mutate()
                fit = self.fitness(newbie)
                
                while not (fit > -5):
                    #taking two random chromosomes at a time
                    parents = random.sample(range(self.population_size), 2)
                    #calling the random crossover function
                    newbie = self.crossover(self.population[parents[0]], self.population[parents[1]])
                    #calling the random mutation function
                    newbie.mutate()
                    fit = self.fitness(newbie)
                    
                self.results.append((newbie, fit))
                new_population.append(newbie)
                
                #checking for the best chromosome
                if self.best is None or self.best[1] > fit:
                    self.best = (newbie, fit)
            
            #selecting best set of chromosomes using selection function        
            self.population = self.selection(self.population, new_population)
    
        return self.best

    def selection(self, prev, now):
        #selection function to select best set of chromosomes
        
        #adding the new population to the old population
        prev.extend(now)
        #sorting the population according to the fitness values of each chromosome
        prev.sort(lambda x, y: self.compare(self.fitness(x), self.fitness(y)))
        #cropping out best set of choromosomes
        population = prev[:self.population_size]
        return population
    
    def norm_dist(self, value):
        #function to calculate normalised distance values
        
        dist_set = set()
        for row in self.distance:
            for col in row:
                dist_set.add(col)
                
        min_dist = min(dist_set - {10000.0})
        max_dist = max(dist_set - {10000.0})
        array = [[0 for x in range(dim)] for y in range(dim)]
        
        for i in range(dim):
            for j in range(dim):
                if self.distance[i][j] == 10000.0:
                    array[i][j] = 10000.0
                else:
                    array[i][j] = (self.distance[i][j] - min_dist)/(max_dist - min_dist)
                    
        return array
    
    def norm_time(self, value):
        #function to calculate normalised time values
        
        time_set = set()
        for row in self.time:
            for col in row:
                time_set.add(col)
                
        min_time = min(time_set - {10000.0})
        max_time = max(time_set - {10000.0})
        array = [[0 for x in range(dim)] for y in range(dim)]
        
        for i in range(dim):
            for j in range(dim):
                if self.time[i][j] == 10000.0:
                    array[i][j] = 10000.0
                else:
                    array[i][j] = (self.time[i][j] - min_time)/(max_time - min_time)
                    
        return array
    
    def norm_avail(self, value):
        #function to calculate normalised availability values
        
        avail_set = set()
        for item in self.availability:
            avail_set.add(item)
            
        min_avail = min(avail_set - {10000.0})
        max_avail = max(avail_set - {10000.0})
        array = [0 for x in range(dim)]
        
        for i in range(dim):
            if self.availability[i] == 10000.0:
                array[i] = 10000.0
            else:
                array[i] = (self.availability[i] - min_avail)/(max_avail - min_avail)
                
        return array

    def generate_population(self, n):
        #function to generate initial population
        
        chromosomes = list()
        for i in range(n):
            #calling chromosome generating function
            chromosomes.append(self._gen_chromosome())
        self.population = chromosomes

    def _gen_chromosome(self):
        #function to generate chromosomes
        
        #generating random chromosomes from list excluding source and destination
        chromosome = random.sample(list(set(range(self.dim)) - {self.source, self.destination}), self.chromosome_length - 2)
        
        chromosome.insert(0, self.source)
        chromosome.append(self.destination)
        
        return Chromosome(chromosome)

    def crossover(self, mother, father):
        #function to create new chromosome using crossover method 
        
        mother_list = mother.get()
        father_list = father.get()
        
        #choosing a random point to make the crossover happen
        cut = random.randint(0, self.chromosome_length - 1)
        child = mother_list[0:cut] + father_list[cut:]
        
        return Chromosome(child)

    def fitness(self, chromosome):
        #function to calculate fitness value of each chromosome
        
        chromosome_list = chromosome.get()
        
        #returning fitness value
        return self.w3*self.sum_value(self.normal_dist, chromosome_list) + self.w1*self.sum_value(self.normal_time, chromosome_list) - self.w2*self.sum1_value(self.normal_avail, chromosome_list)

    def sum_value(self, value, chrom_list):
        #function to calculate sum
        
        return sum([value[i][j] for i, j in zip(chrom_list[:-1], chrom_list[1:])])
    
    def sum1_value(self, value, chrom_list):
        #function to calculate sum
        
        return sum([value[j] for i, j in zip(chrom_list[:-1], chrom_list[1:])])

    def compare(self, item1, item2):
        #function to compare fitness values
        
        sign = item1 - item2
        
        if sign < 0:
            return -1
        else:
            return 1

    def print_chromosomes(self, chromosomes):
        #function to print chromosomes
        
        for chromosome in chromosomes:
            print str(chromosome) + ' ' + str(self.fitness(chromosome))

    def pretty_print(self, to_print, hint=''):
        #function to create a print format
        
        print ''
        print '=================='
        print hint + str(to_print)
        print '=================='


if __name__ == "__main__":
    #main script
    
    #loading the weight matrix
    weight_list = scipy.io.loadmat('freq_weights.mat')
    weight_list = weight_list['weights']
    
    imp = Import_Code()
    matrices = imp.create_matrices()
    
    #taking inputs
    source = input('Enter source: ')
    destination = input('Enter destination: ')
    
    chromosome_length = 3
    best = None
    
    #running genetic algorithm for all weights
    for i in range(len(weight_list)):
        while not best or best[1] > 10:
            gene_network = GeneNetwork(dim, chromosome_length, weight_list, i, source, destination)
            
            #taking 1000 generations
            res = gene_network.start(1000, 50)
            if best is None or best[1] > res[1]:
                best = res
            chromosome_length += 1
            
        gene_network.pretty_print(res, 'Solution: ')
        gene_network = None
        chromosome_length = 3
        
    print ''
    print ''
    #printing the best solution
    print 'OPTIMUM SOLUTION WITH BEST FITNESS: '
    print best