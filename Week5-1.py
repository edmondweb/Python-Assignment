# Creating a class

class Country:
    def __init__(self, name, capital, currency, population=0):
        self.name = name
        self.capital = capital
        self.currency = currency
        self._population = population
        
        
    # Getting the population

    def get_population(self):
        return self._population
    
    # Setting the population
    def set_population(self, population):
        if population > 0:
            self._population = population
        else:
            print("Population must be a positive number")
    
    # Displaying country information 
    def display_info(self):
        print(f"Country: {self.name}, Capital City: {self.capital}, Currency: {self.currency}")
        print(f"Population: {self._population}")
    
# Creating an instance of the Country class
        

my_country = Country("Japan", "Tokyo", "Yen", 124905773)
my_country.display_info()

# Modify the population
my_country.set_population(125000000)
my_country.display_info()
