import copy

import pygame

class UI:
    
    def __init__(self, window_dimensions, button_size, textarea_size, \
        button_font, textarea_font):
        assert isinstance(window_dimensions, tuple), "Window dimensions " \
            "must be a tuple of two integers"
        assert len(window_dimensions) == 2, "Window dimensions must be a " \
            "tuple of two integers"
        for dimension in window_dimensions:
            assert isinstance(dimension, int), "Window dimensions must be " \
                "a tuple of two integers"
        
        assert isinstance(textarea_size, tuple), "Textarea size must be a " \
            "tuple of two integers"
        assert len(textarea_size) == 2, "Textarea size must be a " \
            "tuple of two integers"
        for dimension in textarea_size:
            assert isinstance(dimension, int), "Textarea size must be a " \
                "tuple of two integers"
        
        assert isinstance(button_size, tuple), "Button size must be a " \
            "tuple of two integers"
        assert len(button_size) == 2, "Button size must be a " \
            "tuple of two integers"
        for dimension in button_size:
            assert isinstance(dimension, int), "Button size must be a " \
                "tuple of two integers"
        
        assert isinstance(button_font, pygame.font.Font), "Button font " \
            "must a pygame Font"
        assert isinstance(textarea_font, pygame.font.Font), "Textarea " \
            "font must a pygame Font"
        
        self.window_dimensions = window_dimensions
        self.button_size = button_size
        self.textarea_size = textarea_size
        self.button_font = button_font
        self.textarea_font = textarea_font
        
        self.uielements = []
        self.textarea_focus = ""
        
        self.prev_mouse_pressed = True
        self.prev_keys_pressed = {chr(n): False for n in range(97, 123)}
        for n in range(10):
            self.prev_keys_pressed[str(n)] = False
        self.prev_keys_pressed["space"] = False
        self.prev_keys_pressed["lalt"] = False
        self.prev_keys_pressed["ralt"] = False
        self.prev_keys_pressed["lshift"] = False
        self.prev_keys_pressed["rshift"] = False
        self.prev_keys_pressed["lctrl"] = False
        self.prev_keys_pressed["rctrl"] = False
        self.prev_keys_pressed["return"] = False
        self.prev_keys_pressed["backspace"] = False
        self.prev_keys_pressed["escape"] = False
    
    def add_uielement(self, uielement):
        assert isinstance(uielement, UIElement), "UI element must be an " \
            "instance of the UIElement class"
        
        self.uielements.append(uielement)
        
        # Update textarea focus.
        if self.textarea_focus == "":
            self.textarea_focus = uielement.get_name()
    
    def set_textarea_focus(self, uielement_name):
        assert isinstance(uielement_name, str), "UIElement name must be a " \
            "string"
        
        # Check if the specified name is an empty string, meaning remove 
        # focus completely.
        if uielement_name == "":
            self.textarea_focus = uielement_name
            return
        
        # Check if the textarea with the specified name exists.
        uielement_exists = False
        for uielement in self.uielements:
            if isinstance(uielement, TextArea):
                if uielement.get_name() == uielement_name:
                    uielement_exists = True
                    break
        
        # Set textarea focus if the element exists.
        if uielement_exists:
            self.textarea_focus = uielement_name
    
    def update(self, mouse_position, mouse_pressed, \
        keys_pressed):
        # Update element mouse hover modes in the future.
        
        # Capture 'escape' and 'return' key presses.
        local_pressed = {}
        local_pressed["key_escape"] = keys_pressed["escape"]
        local_pressed["key_return"] = keys_pressed["return"]
        local_pressed["key_escape_prev"] = self.prev_keys_pressed["escape"]
        local_pressed["key_return_prev"] = self.prev_keys_pressed["return"]
        
        # Update text of focused textarea if applicable.
        if not self.textarea_focus == "":
            for uielement in self.uielements:
                if not isinstance(uielement, TextArea):
                    continue
                
                if not uielement.get_name() == self.textarea_focus:
                    continue
                
                for key, pressed in keys_pressed.items():
                    if pressed and not self.prev_keys_pressed[key]:
                        if key == "space":
                            uielement.add_text(" ")
                            continue
                        elif key == "backspace":
                            uielement.backspace()
                            continue
                        elif key in ["lalt", "ralt", "lshift", "rshift", \
                            "lctrl", "rctrl", "return", "escape"]:
                            continue
                        else:
                            uielement.add_text(key)
        
        # Update prev keys pressed.
        self.prev_keys_pressed = copy.deepcopy(keys_pressed)
        
        # Initialize return dict.
        return_dict = {}
        for uielement in self.uielements:
            if not isinstance(uielement, TextArea):
                continue
            
            return_dict[uielement.get_name()] = uielement.get_current_text()
        
        # Add potentially useful key presses to return dict (for now only 
        # escape and return for menu showing/hiding and return in the create 
        # menu).
        for key, value in local_pressed.items():
            return_dict[key] = value
        
        # Check if the mouse is clicked and the mouse was not clicked during 
        # the previous update.
        if not mouse_pressed or self.prev_mouse_pressed:
            # Update prev mouse pressed.
            self.prev_mouse_pressed = mouse_pressed
            
            # Add all buttons to dict with false as the status.
            for uielement in self.uielements:
                if not isinstance(uielement, Button):
                    continue
                
                return_dict[uielement.get_name()] = False
        else:
            # Update prev mouse pressed.
            self.prev_mouse_pressed = mouse_pressed
            
            # The mouse was clicked this update. Check where the click was.
            reset_textarea_focus = True
            for uielement in self.uielements:
                if isinstance(uielement, Button):
                    pos_x = uielement.get_position()[0] - self.button_size[0] // 2
                    pos_y = uielement.get_position()[1] - self.button_size[1] // 2
                    width = self.button_size[0]
                    height = self.button_size[1]
                elif isinstance(uielement, TextArea):
                    pos_x = uielement.get_position()[0] - self.textarea_size[0] // 2
                    pos_y = uielement.get_position()[1] - self.textarea_size[1] // 2
                    width = self.textarea_size[0]
                    height = self.textarea_size[1]
                
                if mouse_position[0] > pos_x and mouse_position[0] < pos_x + width \
                    and mouse_position[1] > pos_y and mouse_position[1] < pos_y + height:
                    if isinstance(uielement, Button):
                        return_dict[uielement.get_name()] = True
                        reset_textarea_focus = False
                    elif isinstance(uielement, TextArea):
                        self.set_textarea_focus(uielement.get_name())
                        reset_textarea_focus = False
                else:
                    if isinstance(uielement, Button):
                        return_dict[uielement.get_name()] = False
                    elif isinstance(uielement, TextArea):
                        pass
            
            # Reset textarea focus if needed.
            if reset_textarea_focus:
                self.set_textarea_focus("")
        
        # Return the return dict so the parent state can handle button 
        # presses.
        return return_dict
    
    def render_text(self, display, text, position, font, \
        color=(255, 255, 255)):
        text_surface = font.render(text, False, color)
        display.blit(text_surface, position)
    
    def render_text_middle(self, display, text, position, font, \
        color=(255, 255, 255)):
        text_surface = font.render(text, False, color)
        display.blit(text_surface, \
            (position[0] - text_surface.get_width() // 2, \
                position[1] - text_surface.get_height() // 2))
    
    def render(self, display):
        # Render UI elements.
        for uielement in self.uielements:
            if isinstance(uielement, Button):
                uielement.render(display, self.button_font, self.button_size)
            elif isinstance(uielement, TextArea):
                uielement.render(display, self.textarea_font, self.textarea_size)

class UIElement:
    
    def __init__(self, name, position):
        assert isinstance(name, str), "Name must be a string"
        
        assert isinstance(position, tuple), "Position must a tuple of two " \
            "integers"
        assert len(position) == 2, "Position must a tuple of two integers"
        for dimension in position:
            assert isinstance(dimension, int), "Position must a tuple of " \
                "two integers"
        
        self.name = name
        self.position = position
    
    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position
    
    def render_text_middle(self, display, text, position, font, \
        color=(255, 255, 255)):
        text_surface = font.render(text, False, color)
        display.blit(text_surface, \
            (position[0] - text_surface.get_width() // 2, \
                position[1] - text_surface.get_height() // 2))
    
    def render_text_middle_y(self, display, text, position, font, \
        color=(255, 255, 255)):
        text_surface = font.render(text, False, color)
        display.blit(text_surface, \
            (position[0], position[1] - text_surface.get_height() // 2))

class Button(UIElement):
    
    def __init__(self, name, position, label):
        super().__init__(name, position)
        
        assert isinstance(label, str), "Button label must be a string"
        
        self.label = label
    
    def get_label(self):
        return self.label
    
    def render(self, display, font, button_size):
        # Render button background.
        pos_x = self.position[0] - button_size[0] / 2
        pos_y = self.position[1] - button_size[1] / 2
        pygame.draw.rect(display, (100, 100, 100), \
            (pos_x, pos_y, button_size[0], button_size[1]))
        
        # Render button label.
        text_pos_x = self.position[0]
        text_pos_y = self.position[1]
        self.render_text_middle(display, self.label, \
            (text_pos_x, text_pos_y), font)

class TextArea(UIElement):
    
    def __init__(self, name, position, max_length=255):
        super().__init__(name, position)
        
        self.current_text = ""
        self.max_length = max_length
    
    def get_current_text(self):
        return self.current_text
    
    def set_current_text(self, current_text):
        assert isinstance(current_text, str), "Current text must be a string"
        
        if len(current_text) > self.max_length:
            self.current_text = current_text[:self.max_length]
        else:
            self.current_text = current_text
    
    def add_text(self, text_extension):
        assert isinstance(text_extension, str), "Text extension must be a string"
        
        if len(self.current_text) == self.max_length:
            return
        
        self.current_text += text_extension
    
    def backspace(self):
        self.current_text = self.current_text[:-1]
    
    def render(self, display, font, textarea_size):
        # Render textarea border.
        pos_x = self.position[0] - textarea_size[0] / 2
        pos_y = self.position[1] - textarea_size[1] / 2
        pygame.draw.rect(display, (200, 200, 200), \
            (pos_x - 2, pos_y - 2, \
                textarea_size[0] + 4, textarea_size[1] + 4))
        
        # Render textarea background.
        pygame.draw.rect(display, (100, 100, 100), \
            (pos_x, pos_y, textarea_size[0], textarea_size[1]))
        
        # Render text.
        text_pos_x = self.position[0] - textarea_size[0] / 2 + 10
        text_pos_y = self.position[1]
        self.render_text_middle_y(display, self.current_text, \
            (text_pos_x, text_pos_y), font)