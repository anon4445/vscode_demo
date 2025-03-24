class Car:
    """Represents a car with attributes and methods."""

    def __init__(self, make, model, year, color):
        """Initializes the Car object."""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} ({self.color})"
        return long_name.title()

    def read_odometer(self):
        """Prints a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Sets the odometer reading to the given value.
        Rejects the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Adds the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't add negative miles!")

# Global Variable
total_cars_created = 0

def create_car_object(make, model, year, color):
  """Function to create and return a Car object, and increment the global counter."""
  global total_cars_created
  new_car = Car(make, model, year, color)
  total_cars_created += 1
  return new_car

def display_total_cars():
  """Function to display the total number of car objects created."""
  print(f"Total cars created: {total_cars_created}")

# Example Usage:

my_car = create_car_object("Toyota", "Camry", 2023, "Silver")
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(23)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()
my_car.increment_odometer(-10) #example of negative miles error
my_car.update_odometer(10) #example of rollback error.

another_car = create_car_object("Honda", "Civic", 2022, "Blue")
print(another_car.get_descriptive_name())

display_total_cars() #display the global variable.