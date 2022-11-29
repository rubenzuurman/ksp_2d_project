class VehicleAssemblyBuilding:
    """
    This class allows the user to create, load, and save vessel 
    configurations. It is also the class 
    """
    
    def __init__(self, window_dimensions, font):
        # Set window dimensions and font.
        self.window_dimensions = window_dimensions
        self.font = font
        
        # Initialize vessel configuration.
        self.vessel_config = VesselConfiguration()
        
    def render(self, display):
        pass
    
    def update(self, mouse_position, mouse_pressed, keys_pressed):
        # Move parts and shit.
        pass

class VesselConfiguration:
    """
    The configuration contains information about which components are 
    connected to each other and in what order to file the decouplers.ff
    """
    
    def __init__(self):
        pass
    
    def load_from_file(self):
        pass
    
    def save_to_file(self):
        pass
    
    def create_new(self):
        pass