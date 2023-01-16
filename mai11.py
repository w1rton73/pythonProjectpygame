import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.queue = 1

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        wcolor = pygame.Color("white")
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, wcolor, (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                   self.cell_size, self.cell_size), 1 if self.board[i][j] == 0 else 0)

    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords is None:
            return

        self.on_click(cell_coords)

    def get_cell(self, mouse_pos):
        board_width = self.width * self.cell_size
        board_height = self.height * self.cell_size
        if self.left < mouse_pos[0] < self.left + board_width:
            if self.top < mouse_pos[1] < self.top + board_height:
                cell_coords = (mouse_pos[1] - self.left) // self.cell_size, \
                              (mouse_pos[0] - self.top) // self.cell_size
                return cell_coords
        return None

    def on_click(self, cell_coords):

        i = cell_coords[0] // 30 - self.left // 30
        j = cell_coords[1] // 30 - self.top // 30
        if (i >= 0 and j >= 0) and (i < self.width and j < self.height):
            i = cell_coords[0] // 30 - self.left // 30
            j = cell_coords[1] // 30 - self.top // 30
            if self.queue:
                pygame.draw.lines(screen, pygame.Color('red'), False, [[i * 30 + 5, j * 30 + 15],
                                                                       [i * 30 + 25, j * 30 + 15]], 20)
                self.queue = 0
            else:
                pygame.draw.lines(screen, pygame.Color('blue'), False, [[i * 30 + 5, j * 30 + 15],
                                                                       [i * 30 + 25, j * 30 + 15]], 20)
                self.queue = 1
        else:
            print(None)


pygame.init()
size = 1000, 1000
screen = pygame.display.set_mode(size)
board = Board(30, 30)
board.set_view(0, 0, 30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
        board.render(screen)
        pygame.display.flip()
pygame.quit()