class Truck:
    def __init__(self, capacity, speed, miles, address, depart_time, packages):
        self.capacity = capacity
        self.speed = speed
        self.miles = miles
        self.address = address
        self.depart_time = depart_time 
        self.packages = packages

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.miles,
                                           self.address, self.depart_time, self.packages)