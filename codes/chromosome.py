import random

class Chromosome(object):
#Chromosme class to convert chromosome to vector    
    def __init__(self, vector):
        self.vector = vector

    def __repr__(self):
        return str(self.vector)

    def get(self):
        return self.vector

    def size(self):
        return len(self.vector)

    def path(self):
        return sum(self.vector)

    def mutate(self):
        #function to mutate a chromosome at 3 random points
        
        pos = random.randint(1, self.size() - 2)
        self.vector[pos] = random.randint(0, 19)
        
        pos = random.randint(1, self.size() - 2)
        self.vector[pos] = random.randint(0, 19)
        
        pos = random.randint(1, self.size() - 2)
        self.vector[pos] = random.randint(0, 19)