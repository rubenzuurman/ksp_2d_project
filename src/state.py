import pygame

import solar_system as ss
import ui
import vehicle_assembly_building as vab

class State:
    """
    Give data in initializer.
    Call update and render methods until the state 
    """
    def __init__(self):
        self.next_state = None
    
    def update(self, mouse_position, mouse_pressed, keys_pressed):
        pass
    
    def render(self):
        pass
    
    def get_next_state(self):
        return self.next_state

class MenuState(State):
    
    def __init__(self, window_dimensions):
        # Initialize superclass.
        super().__init__()
        
        # Set window dimensions.
        self.window_dimensions = window_dimensions
        
        # Set button size and textarea size.
        button_size = (800, 200)
        textarea_size = (800, 50)
        
        # Create fonts.
        button_font = pygame.font.SysFont("Courier New", 48)
        textearea_font = pygame.font.SysFont("Courier New", 32)
        
        # Create UI and add elements.
        self.ui = ui.UI(window_dimensions, button_size, \
            textarea_size, button_font, textearea_font)
        
        load_button = ui.Button("load_button", (window_dimensions[0] // 2, \
            window_dimensions[1] // 4), "Load Existing Save")
        create_button = ui.Button("create_button", (window_dimensions[0] // 2, \
            window_dimensions[1] // 4 * 2), "Create New Save")
        exit_button = ui.Button("exit_button", (window_dimensions[0] // 2, \
            window_dimensions[1] // 4 * 3), "Exit")
        self.ui.add_uielement(load_button)
        self.ui.add_uielement(create_button)
        self.ui.add_uielement(exit_button)
    
    def update(self, mouse_position, mouse_pressed, \
        keys_pressed):
        # Call superclass update.
        super().update(mouse_position, mouse_pressed, keys_pressed)
        
        return_dict = self.ui.update(mouse_position, mouse_pressed, \
            keys_pressed)
        
        # Check button presses.
        if return_dict["load_button"]:
            # Create load state and set next state.
            self.next_state = LoadState(self.window_dimensions)
        elif return_dict["create_button"]:
            # Create create state and set next state.
            self.next_state = CreateState(self.window_dimensions)
        elif return_dict["exit_button"]:
            # Return false to signal the main method that the application can 
            # be terminted.
            return False
        
        return True
    
    def render(self, display):
        # Render UI.
        self.ui.render(display)

class LoadState(State):
    
    def __init__(self, window_dimensions):
        # Initialize superclass.
        super().__init__()
        
        # Set window dimensions.
        self.window_dimensions = window_dimensions
        
        # Set button size and textarea size.
        button_size = (800, 200)
        textarea_size = (800, 50)
        
        # Create fonts.
        button_font = pygame.font.SysFont("Courier New", 48)
        textearea_font = pygame.font.SysFont("Courier New", 32)
        
        # Create UI and add elements.
        self.ui = ui.UI(window_dimensions, button_size, textarea_size, \
            button_font, textearea_font)
        
        savename_textarea_pos = (window_dimensions[0] // 2, \
            window_dimensions[1] // 2)
        savename_textarea = ui.TextArea("savename_textarea", \
            savename_textarea_pos, max_length=41)
        load_button_pos = (window_dimensions[0] // 2, \
            window_dimensions[1] // 8 * 7)
        load_button = ui.Button("load_button", load_button_pos, "Load Save")
        
        self.ui.add_uielement(savename_textarea)
        self.ui.add_uielement(load_button)
    
    def update(self, mouse_position, mouse_pressed, keys_pressed):
        # Call superclass update.
        super().update(mouse_position, mouse_pressed, keys_pressed)
        
        return_dict = self.ui.update(mouse_position, mouse_pressed, \
            keys_pressed)
        
        # Check button presses.
        if return_dict["load_button"]:
            # Get save folder.
            savename = return_dict["savename_textarea"]
            
            # Create solar system view state.
            self.next_state = SolarSystemViewState(self.window_dimensions, \
                savename)
        
        return True
    
    def render(self, display):
        # Render UI.
        self.ui.render(display)

class CreateState(State):
    
    def __init__(self, window_dimensions):
        # Initialize superclass.
        super().__init__()
        
        # Set window dimensions.
        self.window_dimensions = window_dimensions
        
        # Set button size and textarea size.
        button_size = (800, 200)
        textarea_size = (800, 50)
        
        # Create fonts.
        button_font = pygame.font.SysFont("Courier New", 48)
        textearea_font = pygame.font.SysFont("Courier New", 32)
        
        # Create UI and add elements.
        self.ui = ui.UI(window_dimensions, button_size, textarea_size, \
            button_font, textearea_font)
        
        savename_textarea_pos = (window_dimensions[0] // 2, \
            window_dimensions[1] // 2)
        savename_textarea = ui.TextArea("savename_textarea", \
            savename_textarea_pos, max_length=41)
        create_button_pos = (window_dimensions[0] // 2, \
            window_dimensions[1] // 8 * 7)
        create_button = ui.Button("create_button", create_button_pos, \
            "Create Save")
        
        self.ui.add_uielement(savename_textarea)
        self.ui.add_uielement(create_button)
    
    def update(self, mouse_position, mouse_pressed, keys_pressed):
        # Call superclass update.
        super().update(mouse_position, mouse_pressed, keys_pressed)
        
        return_dict = self.ui.update(mouse_position, mouse_pressed, \
            keys_pressed)
        
        # Check button presses.
        if return_dict["create_button"]:
            # Get save folder.
            savename = return_dict["savename_textarea"]
            
            # Create solar system view state.
            self.next_state = SolarSystemViewState(self.window_dimensions, \
                savename)
            print("Create button was pressed.")
        
        return True
    
    def render(self, display):
        # Render UI.
        self.ui.render(display)

class SolarSystemViewState(State):
    
    def __init__(self, window_dimensions, savename):
        # Initialize superclass.
        super().__init__()
        
        # Set window dimensions and savename.
        self.window_dimensions = window_dimensions
        self.savename = savename
        
        # Set button size and textarea size.
        button_size = (500, 80)
        textarea_size = (0, 0)
        
        # Create fonts.
        button_font = pygame.font.SysFont("Courier New", 48)
        textarea_font = pygame.font.SysFont("Courier New", 32)
        
        # Create UI and add elements.
        self.ui = ui.UI(window_dimensions, button_size, textarea_size, \
            button_font, textarea_font)
        
        # TODO: Create menu for when the user presses escape.
        continue_button_pos = (window_dimensions[0] // 2, \
            window_dimensions[1] // 8 * 3)
        continue_button = ui.Button("continue_button", \
            continue_button_pos, "Continue")
        
        enter_vab_button_pos = (window_dimensions[0] // 2, \
            window_dimensions[1] // 8 * 4)
        enter_vab_button = ui.Button("enter_vab_button", \
            enter_vab_button_pos, "Enter VAB")
        
        save_and_exit_button_pos = (window_dimensions[0] // 2, \
            window_dimensions[1] // 8 * 5)
        save_and_exit_button = ui.Button("save_and_exit_button", \
            save_and_exit_button_pos, "Save and Exit")
        
        self.ui.add_uielement(continue_button)
        self.ui.add_uielement(enter_vab_button)
        self.ui.add_uielement(save_and_exit_button)
        
        self.show_ui = False
        
        # Create solar system and load.
        self.solarsystem = ss.SolarSystem(window_dimensions, savename, \
            button_font)
        self.solarsystem.load()
    
    def update(self, mouse_position, mouse_pressed, keys_pressed):
        # Call superclass update.
        super().update(mouse_position, mouse_pressed, keys_pressed)
        
        self.solarsystem.update(0.016, mouse_position, mouse_pressed, \
            keys_pressed)
        
        # Get ui inputs.
        return_dict = self.ui.update(mouse_position, mouse_pressed, \
            keys_pressed)
        
        # Check if show ui needs to be flipped.
        if return_dict["key_escape"] and not return_dict["key_escape_prev"]:
            self.show_ui = not self.show_ui
        
        #self.ui.update(mouse_position, mouse_pressed, \
        #    keys_pressed)
        
        # Handle ui inputs if the ui is shown.
        if self.show_ui:
            if return_dict["continue_button"]:
                self.show_ui = False
            if return_dict["enter_vab_button"]:
                self.solarsystem.save()
                self.next_state = VehicleAssemblyBuildingViewState( \
                    self.window_dimensions, self.savename)
            if return_dict["save_and_exit_button"]:
                self.solarsystem.save()
                self.next_state = MenuState(self.window_dimensions)
        
        return True
    
    def render(self, display):
        # Render solar system.
        self.solarsystem.render(display)
        
        # Render text.
        text_pos = (self.window_dimensions[0] // 2, \
            self.window_dimensions[1] // 2)
        render_text_center(display, "Solar System View", text_pos, \
            self.ui.button_font)
        
        # Render UI.
        if self.show_ui:
            self.ui.render(display)

class VehicleAssemblyBuildingViewState(State):
    
    def __init__(self, window_dimensions, savename):
        # Initialize superclass.
        super().__init__()
        
        # Set window dimensions and savename.
        self.window_dimensions = window_dimensions
        self.savename = savename
        
        # Set button size and textarea size.
        button_size = (500, 40)
        textarea_size = (0, 0)
        
        # Create fonts.
        button_font = pygame.font.SysFont("Courier New", 32)
        textarea_font = pygame.font.SysFont("Courier New", 32)
        
        # Create UI and add elements.
        self.ui = ui.UI(window_dimensions, button_size, textarea_size, \
            button_font, textarea_font)
        
        x1 = button_size[0] // 2 + (button_size[0] + 10) * 0 + 10
        load_button_pos = (x1, 30)
        load_button = ui.Button("load_button", load_button_pos, \
            "Load Existing Vessel")
        
        x2 = button_size[0] // 2 + (button_size[0] + 10) * 1 + 10
        save_button_pos = (x2, 30)
        save_button = ui.Button("save_button", save_button_pos, \
            "Save Vessel")
        
        x3 = button_size[0] // 2 + (button_size[0] + 10) * 2 + 10
        launch_button_pos = (x3, 30)
        launch_button = ui.Button("launch_button", launch_button_pos, \
            "Launch Vessel")
        
        x4 = button_size[0] // 2 + (button_size[0] + 10) * 3 + 10
        return_to_solarsystem_button_pos = (x4, 30)
        return_to_solarsystem_button = ui.Button("return_to_solarsystem", \
            return_to_solarsystem_button_pos, "Return to Solar System")
        
        self.ui.add_uielement(load_button)
        self.ui.add_uielement(save_button)
        self.ui.add_uielement(launch_button)
        self.ui.add_uielement(return_to_solarsystem_button)
        
        # Load solar system.
        self.solarsystem = ss.SolarSystem(window_dimensions, savename, \
            button_font)
        self.solarsystem.load()
        
        # Initialize vab.
        self.vab = vab.VehicleAssemblyBuilding(window_dimensions, button_font)
    
    def update(self, mouse_position, mouse_pressed, keys_pressed):
        # Call superclass update.
        super().update(mouse_position, mouse_pressed, keys_pressed)
        
        # TODO: Possibly remove the last three arguments or set them to no 
        # input.
        self.solarsystem.update(0.016, mouse_position, mouse_pressed, 
            keys_pressed)
        self.vab.update(mouse_position, mouse_pressed, keys_pressed)
        
        # Get ui inputs.
        return_dict = self.ui.update(mouse_position, mouse_pressed, \
            keys_pressed)
        
        # Handle ui inputs.
        if return_dict["load_button"]:
            print("TODO: Load vessel.")
        if return_dict["save_button"]:
            print("TODO: Save vessel.")
        if return_dict["launch_button"]:
            print("TODO: Launch vessel.")
        if return_dict["return_to_solarsystem"]:
            self.solarsystem.save()
            self.next_state = SolarSystemViewState(self.window_dimensions, \
                self.savename)
        
        return True
    
    def render(self, display):
        # Render vab.
        self.vab.render(display)
        
        # Render text.
        text_pos = (self.window_dimensions[0] // 2, \
            self.window_dimensions[1] // 2)
        render_text_center(display, "Vehicle Assembly Building View", \
            text_pos, self.ui.button_font)
        
        # Render ui.
        self.ui.render(display)

def render_text_center(display, text, position, font, color=(255, 255, 255)):
    # Create text surface.
    text_surface = font.render(text, False, color)
    
    # Update position to center the text.
    position_x = position[0] - text_surface.get_width() / 2
    position_y = position[1] - text_surface.get_height() / 2
    
    # Render text/
    display.blit(text_surface, (position_x, position_y))