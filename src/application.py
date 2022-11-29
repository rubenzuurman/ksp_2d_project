# Correct window size.
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame

import state

def render_text(display, text, position, font, color=(255, 255, 255)):
    text_surface = font.render(text, False, color)
    display.blit(text_surface, position)

def render_text_center(display, text, position, font, color=(255, 255, 255)):
    # Create text surface.
    text_surface = font.render(text, False, color)
    
    # Update position to center the text.
    position_x = position[0] - text_surface.get_width() / 2
    position_y = position[1] - text_surface.get_height() / 2
    
    # Render text/
    display.blit(text_surface, (position_x, position_y))

def main(title, window_dimensions):
    # Initialize pygame.
    pygame.init()
    pygame.font.init()
    
    # Initialize font.
    font = pygame.font.SysFont("Courier New", 16)
    
    # Create display.
    display = pygame.display.set_mode(window_dimensions, \
        flags=pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption(title)
    
    # Create menu state.
    current_state = state.MenuState(window_dimensions)
    
    # Create clock.
    clock = pygame.time.Clock()
    fps = 60
    
    # Initialize keypress dicts.
    keys_pressed = {chr(n): False for n in range(97, 123)}
    for n in range(10):
        keys_pressed[str(n)] = False
    keys_pressed["space"] = False
    keys_pressed["lalt"] = False
    keys_pressed["ralt"] = False
    keys_pressed["lshift"] = False
    keys_pressed["rshift"] = False
    keys_pressed["lctrl"] = False
    keys_pressed["rctrl"] = False
    keys_pressed["return"] = False
    keys_pressed["backspace"] = False
    keys_pressed["escape"] = False
    
    last_key = ""
    
    # Start update and render loop.
    running = True
    while running:
        # Handle events.
        for event in pygame.event.get():
            # Detect quit event.
            if event.type == pygame.QUIT:
                # This doesn't actually do anything at the moment, as the 
                # running value is updated by the next update call to the 
                # currently active state.
                running = False
            
            if event.type == pygame.KEYDOWN:
                # Check which numbers are pressed.
                for n in range(48, 58):
                    if event.key == n:
                        keys_pressed[str(n-48)] = True
                
                # Check which letters are pressed.
                for n in range(97, 123):
                    if event.key == n:
                        keys_pressed[chr(n)] = True
                
                # Check remaining special keys.
                if event.key == pygame.K_SPACE:
                    keys_pressed["space"] = True
                if event.key == pygame.K_LALT:
                    keys_pressed["lalt"] = True
                if event.key == pygame.K_RALT:
                    keys_pressed["ralt"] = True
                if event.key == pygame.K_LSHIFT:
                    keys_pressed["lshift"] = True
                if event.key == pygame.K_RSHIFT:
                    keys_pressed["rshift"] = True
                if event.key == pygame.K_LCTRL:
                    keys_pressed["lctrl"] = True
                if event.key == pygame.K_RCTRL:
                    keys_pressed["rctrl"] = True
                if event.key == pygame.K_RETURN:
                    keys_pressed["return"] = True
                if event.key == pygame.K_BACKSPACE:
                    keys_pressed["backspace"] = True
                if event.key == pygame.K_ESCAPE:
                    keys_pressed["escape"] = True
                
                if event.key < 128:
                    last_key = chr(event.key)
            
            if event.type == pygame.KEYUP:
                # Check which numbers are pressed.
                for n in range(48, 58):
                    if event.key == n:
                        keys_pressed[str(n-48)] = False
                
                # Check which letters are pressed.
                for n in range(97, 123):
                    if event.key == n:
                        keys_pressed[chr(n)] = False
                
                # Check remaining special keys.
                if event.key == pygame.K_SPACE:
                    keys_pressed["space"] = False
                if event.key == pygame.K_LALT:
                    keys_pressed["lalt"] = False
                if event.key == pygame.K_RALT:
                    keys_pressed["ralt"] = False
                if event.key == pygame.K_LSHIFT:
                    keys_pressed["lshift"] = False
                if event.key == pygame.K_RSHIFT:
                    keys_pressed["rshift"] = False
                if event.key == pygame.K_LCTRL:
                    keys_pressed["lctrl"] = False
                if event.key == pygame.K_RCTRL:
                    keys_pressed["rctrl"] = False
                if event.key == pygame.K_RETURN:
                    keys_pressed["return"] = False
                if event.key == pygame.K_BACKSPACE:
                    keys_pressed["backspace"] = False
                if event.key == pygame.K_ESCAPE:
                    keys_pressed["escape"] = False
        
        # Check if the state has to be switched.
        next_state = current_state.get_next_state()
        if next_state is not None:
            current_state = next_state
        
        # Update state.
        key_press_event = None
        key_release_event = None
        running = current_state.update(pygame.mouse.get_pos(), \
            pygame.mouse.get_pressed()[0], keys_pressed)
        
        # Fill display with black.
        display.fill((0, 0, 0))
        
        # Render state.
        current_state.render(display)
        
        # Render keys pressed.
        """index = 0
        for key, pressed in keys_pressed.items():
            render_text(display, f"{key}: {pressed}", (10, 10 + index * 20), font)
            index += 1
        render_text(display, f"last key: {last_key}", (10, 10 + index * 20), font)"""
        
        # Update display.
        pygame.display.flip()
        
        # Tick clock.
        clock.tick(fps)

if __name__ == "__main__":
    main("KSP 2D", (2560, 1440))