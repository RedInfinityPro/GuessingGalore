import pygame
import random, sys, math, time
from connections import game_menus
pygame.init()
# window
screenWidth, screenHeight = 700, 700
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
pygame.display.set_caption("Guessing Games")
clock = pygame.time.Clock()
# Function checked if the window is resized.
menu = game_menus.MainMenu(screen, screenWidth, screenHeight)
pause_menu = game_menus.PauseMenu(screen, screenWidth, screenHeight)
def on_resize() -> None:
    window_size = screen.get_size()
    new_w, new_h = window_size[0], window_size[1]
    # main menu
    menu.main_menu.resize(new_w, new_h)
    menu.loadGame_screen.resize(new_w, new_h)
    menu.settings_screen.resize(new_w, new_h)
    menu.credits_screen.resize(new_w, new_h)
    # pause menu
    pause_menu.pause_menu_screen.resize(new_w, new_h)
    pause_menu.options_screen.resize(new_w, new_h)
on_resize()

settings_effects = game_menus.Settings_Effects()
# main
def main():
    global screen
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                on_resize()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if menu.play:
                        pause_menu.play = not(pause_menu.play)
        # Apply brightness effect after drawing everything else
        settings_effects.update_brightness_surface(screenWidth, screenHeight)
        settings_effects.apply_brightness(screen)
        # display
        screen.fill(pygame.Color('white'))
        if not menu.play:
            menu.main_menu.update(events)
            menu.main_menu.draw(screen)
        elif not pause_menu.play:
            pause_menu.pause_menu_screen.update(events)
            pause_menu.pause_menu_screen.draw(screen)
        if pause_menu.exit_game_variable:
            menu.play = False
            pause_menu.exit_game_variable = False
        # This is to update the scene
        clock.tick(64)
        pygame.display.flip()
        pygame.display.update()
# loop
if __name__ == "__main__":
    main()