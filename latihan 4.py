def add_driver_info(cls):
    def show_info(self):
        print(f"Driver: {self.name} | Team: {self.team}")
    
    cls.show_info = show_info  
    return cls  

@add_driver_info
class F1Driver:
    def __init__(self, name, team):
        self.name = name
        self.team = team

verstappen = F1Driver("Max Verstappen", "Red Bull Racing")
sainz = F1Driver("Carlos Sainz", "Williams Racing")

verstappen.show_info()
sainz.show_info()
