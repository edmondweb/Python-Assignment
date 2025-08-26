# Polymorphism Challenge

class Cars:
    def move(self):
        return "Moves on roads"
    
class Boats:
    def move(self):
        return "Moves on water"
    
class Planes:
    def move(self):
        return "Moves in the air"
    

# Function to demonstrate polymorphism

for vehicle in (Cars(), Boats(), Planes()):
    print(vehicle.move())