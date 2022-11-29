import pygame

class SolarSystem:
    """
    This class holds all the information about the solar system. It also 
    contains methods for generating a solar system, loading a solar system, 
    saving a solar system, updating a solar system, and rendering a solar 
    system.
    This class also contains data fields for time, celestial bodies, and 
    player vessels.
    """
    
    def __init__(self, window_dimensions, savename, font):
        # Set window dimensions, savename, and font.
        self.window_dimensions = window_dimensions
        self.savename = savename 
        self.font = font
        
        # Initialize time.
        self.time = 0
        
        # Initialize celestial bodies.
        self.celestial_bodies = {}
        
        # Initialize player vessels.
        self.player_vessels = {}
        
        # Initialize player statistics.
        
        # Initialize player achievements.
        
        print(f"Init solar system '{self.savename}'")
    
    def render(self, display):
        pass
    
    def update(self, delta_time, mouse_position, mouse_pressed, keys_pressed):
        # Increment time.
        self.time += delta_time
        
        # Calculate total forces and torques on all vessels.
        
        # Update vessel velocities and positions.
        
        # Update celestial body positions.
        
        # Move vessel positions with the amount its parent celestial body 
        # moved.
        
        # Recalculate parent celestial bodies for all vessels.
        
        # Detect player achievements.
        
        # Update player statistics.
        
        pass
    
    def load(self):
        # Load time from save folder.
        
        # Load celestial bodies from save folder.
        
        # Load active player vessels from save folder.
        
        # Load player statistics.
        
        # Load player achievements.
        
        print(f"Load solar sytem '{self.savename}'")
    
    def save(self):
        # Save time to save folder.
        
        # Save celestial bodies to save folder.
        
        # Save active player vessels to save folder.
        
        # Save player statistics.
        
        # Save player achievements.
        
        print(f"Save solar sytem '{self.savename}'")

class CelestialBody:
    """
    This class holds all information about one celestial body in the solar 
    system. This information includes orbit parameters, precalculated orbit 
    positions, texture, size, and mass. Possibly also includes luminosity in 
    the future.
    """
    
    def __init__(self):
        pass
    
    def load_from_file(self, path):
        pass
    
    def save_to_file(self, path):
        pass

class Vessel:
    """
    This class contains information about a vessel *in the solar system*. It 
    contains the position and velocity of the vessel, the vessel 
    configuration, staging information, rocket engine positions and 
    directions, angular position and velocity, and rocket engine statuses.
    """
    
    def __init__(self):
        pass
    
    def load_from_file(self):
        pass
    
    def save_to_file(self):
        pass