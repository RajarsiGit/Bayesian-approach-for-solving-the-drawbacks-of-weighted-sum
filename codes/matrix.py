class Matrix(object):
    #class to convert time, distance and availability into a matrix
    
    def __init__(self, time, distance, availability):
        
        self.distance = distance
        self.time = time
        self.availability = availability