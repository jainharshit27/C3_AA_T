import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

rect = pygame.Rect(100, 250, 64, 64)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect.y = rect.y - 5
                if event.key == pygame.K_DOWN:
                    rect.y = rect.y + 5
                if event.key == pygame.K_LEFT:
                    rect.x = rect.x - 5         
                if event.key == pygame.K_RIGHT:
                    rect.x = rect.x + 5
                    
    pygame.draw.rect(screen, (100, 100, 100), rect)
      
    pygame.display.update()
