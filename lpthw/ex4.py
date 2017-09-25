# Setting the cars variable to 100
cars = 100

#Setting how much space in each car
space_in_a_car = 4.0

#Number of drivers
drivers = 30

#Number of passengers
passengers = 90

#Number of cars not driven subtracting the number of cars from the number of drivers
cars_not_driven = cars - drivers

#Number of cars driven
cars_driven = drivers

#Total space in the car (carpool capacity) by multiplying cars driven by the space in each car
carpool_capacity = cars_driven * space_in_a_car

#Finding the average number of passengers per car by diving the passengers by cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
