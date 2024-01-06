# Class Packages for storing package data    
class Package:
    def __init__(self, ID, address, city, state, zipcode, delivery_deadline, 
                 weight, status):
        self.id = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.depart_time = None
        self.delivered_time = None

    # Returns a string representation of the object
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id,
                self.address, self.city, self.state, self.zipcode, self.delivery_deadline,
                self.weight, self.status, self.delivered_time)
                
    def status_update(self, convert_time):
        if self.delivered_time < convert_time:
            self.status = "Package Delivered"
        elif self.depart_time > convert_time:
            self.status = "Package En Route"
        else:
            self.status = "Package At Hub"


