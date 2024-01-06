# Author: Vinh Dinh
# Student ID: 009454302
# Title: WGU Vehicle Routing Program  

import csv
import datetime
from Truck import Truck
from Package import Package
from ChainingHashTable import ChainingHashTable


# Loading the address CSV file
with open("CSV/AddressC950.csv") as address_csv:
    address_dataCSV = csv.reader(address_csv)
    address_dataCSV = list(address_dataCSV)

# Loading the package CSV file
with open("CSV/PackagesC950.csv") as packages_csv:
    packages_dataCSV = csv.reader(packages_csv)
    packages_dataCSV = list(packages_dataCSV)

# Loading the distance CSV file
with open("CSV/DistanceC950.csv") as distance_csv:
    distance_dataCSV = csv.reader(distance_csv)
    distance_dataCSV = list(distance_dataCSV)


# Function that will create package objects from package class       
# Load CSV package file into the hash table
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_delivery_deadline = package[5]
            package_weight = package[6]
            package_status = "Package at Hub"

            p = Package(package_id, package_address, package_city, package_state,
                        package_zipcode, package_delivery_deadline, package_weight,
                        package_status)
            
            package_hash_table.insert(package_id, p)
            

# Function to find the distance between 2 points
def distance_between(x_value, y_value):
    distance = distance_dataCSV[x_value][y_value]
    if distance == '':
        distance = distance_dataCSV[y_value][x_value]

    return float(distance)


# Function for retrieving address from string 
def get_address(address):
    for row in address_dataCSV:
        if address in row[2]:
            return int(row[0])
        
# Manual loading of the trucks for tighter control
# Loading first truck with departed time
truck1 = Truck(16, 18, 0.0, "4001 South 700 East", datetime.timedelta(hours=8),
               [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40])

# Loading second truck with departed time
truck2 = Truck(16, 18, 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=30),
               [3, 12, 17, 18, 21, 22, 23, 24, 26, 27, 33, 35, 36, 38, 39])

# Loading third truck with departed time
truck3 = Truck(16, 18, 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=10),
               [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32])

# Created a package hash table using the class ChainingHashTable
package_table = ChainingHashTable()

# Load packages into the package hash table
load_package_data("CSV/PackagesC950.csv", package_table)


# Function that initializes a list of undelivered packages for a given truck
def package_delivery(truck):
    not_delivered = []
    for package_id in truck.packages:
        package = package_table.search(package_id)
        not_delivered.append(package)

    # The list given to each truck needs to be cleared so that the algorithm can properly list it
    truck.packages.clear()

    while len(not_delivered) > 0:
        next_address = float('inf')
        next_package =  None
        for package in not_delivered:
          if distance_between(get_address(truck.address), get_address(package.address)) <= next_address:  
            next_address = distance_between(get_address(truck.address), get_address(package.address))
            next_package = package

        # Adds the nearest package to truck list
        truck.packages.append(next_package)  

        # Removes the added package from the undelivered list
        not_delivered.remove(next_package)

        # Adds the miles that were driven to deliver said package
        truck.miles += next_address

        # The current truck's location will now be updated to the delivered packaged
        truck.address = next_package.address

        # The time it took for the truck to deliver said package
        truck.depart_time += datetime.timedelta(hours=next_address / 18)
        next_package.delivered_time = truck.depart_time
        next_package.depart_time = truck.depart_time


# Calling on the function to load truck1 and truck2
package_delivery(truck1)
package_delivery(truck2)

# Loading truck3 and departing after truck1 and truck2 have finished their delivery
truck3.depart_time = min(truck1.depart_time, truck2.depart_time)
package_delivery(truck3) 


class Main:
    # User Interface
    # Function that uses users time imput
    @staticmethod
    def get_user_time():
        user_time = input("Please enter a time to check the status of your package(s). Use the following format HH:MM:SS ")
        (h, m, s) = user_time.split(":")
        return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    
    # Function that retrieves a single package
    @staticmethod
    def processs_individual_package(package_table, convert_time):
        single_input = input("Enter package ID number:")
        try:
            package = package_table.search(int(single_input))
            package.status_update(convert_time)
            print(str(package))
        except ValueError:
            print("Invalid package ID. Closing program.")
            exit()
    
    # Function that retrieves all packages
    @staticmethod
    def process_all_packages(package_table, convert_time):
        try:
            for package_id in range(1, 41):
                package = package_table.search(package_id)
                package.status_update(convert_time)
                print(str(package))
        except ValueError:
            print("Invalid package ID. Closing program.")
            exit()

    # Interface where user will be asked to input data
    def run(self):
        print("Western Governors University Parcel Service")
        total_miles = truck1.miles + truck2.miles + truck3.miles
        print("The current mileage route is:", total_miles)

        text = input("To start, please type 'start' (Anything else will terminate the program): ")

        if text.lower() != "start":
            print("Invalid entry. Closing program.")
            exit()

        try:
            convert_time = self.get_user_time()

            second_input = input("To view the status of an individual package, type 'single'. For a list of all the packages, type 'all'.")

            if second_input.lower() == "single":
                self.processs_individual_package(package_table, convert_time)
            elif second_input.lower() == "all":
                self.process_all_packages(package_table, convert_time)
            else:
                exit()
        except ValueError:
            print("Invalid entry. Closing program.")
            exit()


if __name__ == "__main__":
    main = Main()
    main.run() 