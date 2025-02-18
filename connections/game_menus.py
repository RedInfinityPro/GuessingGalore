import pygame_menu
from pygame_menu import themes
import pygame

# settings applied to the scene
class Settings_Effects:
    def __init__(self):
        self.Background_volume = 1.0
        self.soundEffect_volume = 1.0
        self.frameRate = 64
        self.brightness = 100  # Start at 100%
        self.brightness_surface = None
        self.create_brightness_surface(700, 700)  # Initial size
        
    def create_brightness_surface(self, width, height):
        # Create an overlay surface for brightness control
        self.brightness_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.adjust_brightness()
    
    def update_brightness_surface(self, width, height):
        """Update brightness surface when window is resized"""
        if self.brightness_surface is None or self.brightness_surface.get_size() != (width, height):
            self.create_brightness_surface(width, height)
    
    def adjust_brightness(self):
        if self.brightness_surface is None:
            return
            
        # Convert brightness from 0-100 scale to alpha value (255-0)
        # Lower alpha = brighter screen, higher alpha = darker screen
        alpha = int(255 * (1 - self.brightness / 100))
        
        # Fill with black and set transparency
        self.brightness_surface.fill((0, 0, 0, alpha))
    
    def apply_brightness(self, screen):
        if self.brightness_surface is not None:
            current_w, current_h = screen.get_size()
            self.update_brightness_surface(current_w, current_h)
            screen.blit(self.brightness_surface, (0, 0))

# main menu
class MainMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.play = False
        # Create single Settings_Effects instance
        self.settings_effects = Settings_Effects()
        # Initialize default values
        self.music_volume_value = 50
        self.sound_effect_value = 50
        self.frame_rate_value = 60
        self.brightness_value = self.settings_effects.brightness
        self.create_main_menu()
    
    def create_main_menu(self):
        self.main_menu = pygame_menu.Menu('Welcome', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.loadGame_screen = pygame_menu.Menu('Load Game', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.settings_screen = pygame_menu.Menu('Settings', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.tutorial_screen = pygame_menu.Menu('Tutorial', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.credits_screen = pygame_menu.Menu('Credits', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.main_menu.add.button('Play', self.Play)
        self.main_menu.add.button('Load Game', self.load_game)
        self.main_menu.add.button('Settings', self.settings)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)
    
    def load_game(self):
        self.loadGame_screen.clear()
        saved_games = [
            "Load Game",
            "Load Game",
            "Load Game"
        ]
        for index, save in enumerate(saved_games):
            self.loadGame_screen.add.button(save, lambda index=index: self.load_game(index))
        self.loadGame_screen.add.button('Return to Main Menu', pygame_menu.events.BACK)
        self.main_menu._open(self.loadGame_screen)

    def settings(self):
        self.settings_screen.clear()
        self.settings_screen.add.range_slider('Music Volume', default=50, range_values=(0, 100), increment=1, onchange=self.update_music_volume)
        self.settings_screen.add.range_slider('Sound Effects', default=50, range_values=(0, 100), increment=1, onchange=self.update_sound_effects)
        self.settings_screen.add.range_slider('Frame Rate', default=60, range_values=(30, 120), increment=1, onchange=self.update_frame_rate)
        self.settings_screen.add.range_slider('Brightness', default=self.brightness_value, range_values=(0, 100), increment=1, onchange=self.update_brightness)
        self.settings_screen.add.button('Return to Main Menu', pygame_menu.events.BACK)
        self.main_menu._open(self.settings_screen)
        print()
    
    # Callback methods for settings changes
    def update_music_volume(self, value):
        self.music_volume_value = value

    def update_sound_effects(self, value):
        self.sound_effect_value = value

    def update_frame_rate(self, value):
        self.frame_rate_value = value

    def update_brightness(self, value):
        self.brightness_value = value
        self.settings_effects.brightness = value
        self.settings_effects.adjust_brightness()

    def quit_menu(self):
        self.main_menu.disable()

    def Play(self):
        self.play = True

# pause menu
class PauseMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.play = True
        self.restart_game = False
        self.exit_game_variable = False
        # Create single Settings_Effects instance
        self.settings_effects = Settings_Effects()
        # Initialize default values
        self.music_volume_value = 50
        self.sound_effect_value = 50
        self.frame_rate_value = 60
        self.brightness_value = self.settings_effects.brightness
        self.create_main_menu()
    
    def create_main_menu(self):
        self.pause_menu_screen = pygame_menu.Menu('Pause Menu', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.options_screen = pygame_menu.Menu('Options', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.pause_menu_screen.add.button('Resume', self.resume)
        self.pause_menu_screen.add.button('Restart', self.restart)
        self.pause_menu_screen.add.button('Options', self.options)
        self.pause_menu_screen.add.button('Exit', self.exit_game)
    
    def resume(self):
        self.play = True
    
    def restart(self):
        self.restart_game = True
        self.play = True
    
    def options(self):
        self.options_screen.clear()
        self.music_volume = self.options_screen.add.range_slider('Music Volume', default=50, range_values=(0, 100), increment=1)
        self.options_screen.add.range_slider('Music Volume', default=50, range_values=(0, 100), increment=1, onchange=self.update_music_volume)
        self.options_screen.add.range_slider('Sound Effects', default=50, range_values=(0, 100), increment=1, onchange=self.update_sound_effects)
        self.options_screen.add.range_slider('Frame Rate', default=60, range_values=(30, 120), increment=1, onchange=self.update_frame_rate)
        self.options_screen.add.range_slider('Brightness', default=self.brightness_value, range_values=(0, 100), increment=1, onchange=self.update_brightness)
        self.options_screen.add.button('Return to Main Menu', pygame_menu.events.BACK)
        self.pause_menu_screen._open(self.options_screen)

    # Callback methods for settings changes
    def update_music_volume(self, value):
        self.music_volume_value = value

    def update_sound_effects(self, value):
        self.sound_effect_value = value

    def update_frame_rate(self, value):
        self.frame_rate_value = value

    def update_brightness(self, value):
        self.brightness_value = value
        self.settings_effects.brightness = value
        self.settings_effects.adjust_brightness()
        
    def exit_game(self):
        self.exit_game_variable = True
        self.play = True

    def quit_menu(self):
        self.pause_menu_screen.disable()