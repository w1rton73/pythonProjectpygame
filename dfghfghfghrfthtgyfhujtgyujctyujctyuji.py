import pygame

def draw(screen, width1, height1):
    screen.fill(pygame.Color('black'))
    pygame.display.set_caption('Крест')
    pygame.draw.lines(screen, pygame.Color('white'), False, [[35, 30], [55100, 30]], 20)




if __name__ == '__main__':
    pygame.init()
    x = input().split()
    if len(x) > 2:
        print('Неправильный формат ввода')
    try:
        size = int(x[0]), int(x[1])
        screen = pygame.display.set_mode(size)
        draw(screen, int(x[0]), int(x[1]))
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
    except:
        print('Неправильный формат ввода')