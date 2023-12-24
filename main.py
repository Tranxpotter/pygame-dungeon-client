import os
import json
import asyncio

import pygame
import pygame_gui

from network import Network

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
manager = pygame_gui.UIManager(SCREEN_SIZE)
offline_manager = pygame_gui.UIManager(SCREEN_SIZE)

clock = pygame.time.Clock()
dt = 0


#Not online display
not_online_label = pygame_gui.elements.UILabel(pygame.Rect(-100, -50, 200, 100), "Server not online", 
                            manager=offline_manager, 
                            anchors={"centerx":"centerx", "centery":"centery"})
def not_connected_display():
    global running, dt
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    offline_manager.update(dt)
    screen.fill((0,0,0))
    offline_manager.draw_ui(screen)
    pygame.display.flip()
    dt = clock.tick(60)



async def main():
    network = Network("ws://localhost:8765")
    try:
        await network.connect()
    except ConnectionRefusedError:
        connected = False
        

    global running, dt
    running = True
    while running:
        if not connected:
            not_connected_display()
            continue
        
        #Event checking
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            manager.process_events(event)
        
        manager.update(dt)


        #Draw stuff on screen
        screen.fill((0,0,0))
        manager.draw_ui(screen)


        pygame.display.flip()
        
        dt = clock.tick(60)

    
    

    










asyncio.run(main())

pygame.quit()