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
        self.blue = []
        self.red = []
        self.bluefuturestep = []
        self.redfuturestep = []
        self.menu = 1

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
        global pict
        self.tridsat = []
        for i in range(30):
            self.tridsat.append(i)
        i = cell_coords[0] // 30 - self.left // 30
        j = cell_coords[1] // 30 - self.top // 30
        if (i >= 0 and j >= 0) and (i < self.width and j < self.height):
            i = cell_coords[0] // 30 - self.left // 30
            j = cell_coords[1] // 30 - self.top // 30
            if [i, j] not in self.blue and [i, j] not in self.red:
                if self.queue:
                    if [i, j] in self.redfuturestep or not self.red:
                        pygame.draw.lines(screen, pygame.Color('red'), False,
                                          [[i * 30 + 5, j * 30 + 15], [i * 30 + 25, j * 30 + 15]], 20)
                        self.queue = 0
                        self.red.append([i, j])
                        for q in self.redfuturestep:
                            if q not in self.blue and q not in self.red:
                                pygame.draw.lines(screen, pygame.Color('black'), False,
                                                  [[q[0] * 30 + 5, q[1] * 30 + 15],
                                                   [q[0] * 30 + 25, q[1] * 30 + 15]], 20)
                        self.redfuturestep = []
                        for i in self.blue:
                            if [i[0] + 1, i[1]] not in self.blue and [i[0] + 1, i[1]] not in self.red and\
                                    i[0] + 1 in self.tridsat and i[1] in self.tridsat:
                                self.bluefuturestep.append([i[0] + 1, i[1]])
                            if [i[0] - 1, i[1]] not in self.blue and [i[0] - 1, i[1]] not in self.red and\
                                    i[0] - 1 in self.tridsat and i[1] in self.tridsat:
                                self.bluefuturestep.append([i[0] - 1, i[1]])
                            if [i[0], i[1] + 1] not in self.blue and [i[0], i[1] + 1] not in self.red and\
                                    i[0] in self.tridsat and i[1] + 1 in self.tridsat:
                                self.bluefuturestep.append([i[0], i[1] + 1])
                            if [i[0], i[1] - 1] not in self.blue and [i[0], i[1] - 1] not in self.red and\
                                    i[0] in self.tridsat and i[1] - 1 in self.tridsat:
                                self.bluefuturestep.append([i[0], i[1] - 1])
                        for i in self.bluefuturestep:
                            if i[0] not in self.tridsat or i[1] not in self.tridsat:
                                self.bluefuturestep.remove(i)
                        if not self.bluefuturestep and self.blue:
                            if len(self.blue) < len(self.red):
                                pict = "Red.png"
                                scene1()
                    for d in self.bluefuturestep:
                        pygame.draw.lines(screen, pygame.Color('white'), False,
                                          [[d[0] * 30 + 5, d[1] * 30 + 15], [d[0] * 30 + 25, d[1] * 30 + 15]], 20)
                else:
                    if [i, j] in self.bluefuturestep or not self.blue:
                        pygame.draw.lines(screen, pygame.Color('blue'), False,
                                          [[i * 30 + 5, j * 30 + 15], [i * 30 + 25, j * 30 + 15]], 20)
                        self.queue = 1
                        self.blue.append([i, j])
                        for q in self.bluefuturestep:
                            if q not in self.blue and q not in self.red:
                                pygame.draw.lines(screen, pygame.Color('black'), False,
                                                  [[q[0] * 30 + 5, q[1] * 30 + 15],
                                                   [q[0] * 30 + 25, q[1] * 30 + 15]], 20)
                        self.bluefuturestep = []
                        for i in self.red:
                            if [i[0] + 1, i[1]] not in self.blue and [i[0] + 1, i[1]] not in self.red and\
                                    i[0] + 1 in self.tridsat and i[1] in self.tridsat:
                                self.redfuturestep.append([i[0] + 1, i[1]])
                            if [i[0] - 1, i[1]] not in self.blue and [i[0] - 1, i[1]] not in self.red and\
                                    i[0] - 1 in self.tridsat and i[1] in self.tridsat:
                                self.redfuturestep.append([i[0] - 1, i[1]])
                            if [i[0], i[1] + 1] not in self.blue and [i[0], i[1] + 1] not in self.red and\
                                    i[0] in self.tridsat and i[1] + 1 in self.tridsat:
                                self.redfuturestep.append([i[0], i[1] + 1])
                            if [i[0], i[1] - 1] not in self.blue and [i[0], i[1] - 1] not in self.red and\
                                    i[0] in self.tridsat and i[1] - 1 in self.tridsat:
                                self.redfuturestep.append([i[0], i[1] - 1])
                        for i in self.redfuturestep:
                            if i[0] not in self.tridsat or i[1] not in self.tridsat:
                                self.redfuturestep.remove(i)
                    for d in self.redfuturestep:
                        pygame.draw.lines(screen, pygame.Color('white'), False,
                                          [[d[0] * 30 + 5, d[1] * 30 + 15], [d[0] * 30 + 25, d[1] * 30 + 15]], 20)
                    if not self.redfuturestep:
                        if len(self.red) == len(self.blue) and len(self.red) != 450:
                            pict = "Blue.png"
                            scene1()
                        if len(self.red) == 450:
                            pict = "Tie.png"
                            scene1()
        else:
            print(None)


pygame.init()
pict = "startmenu.png"
size = 900, 900
screen = pygame.display.set_mode(size)
scene = None


def switch101(sc):
    global scene
    scene = sc


def scene2():
    pygame.init()
    size = 900, 900
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

def scene1():
    global pict
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch101(None)
            if event.type == pygame.MOUSEBUTTONDOWN:
                scene2()
                running = False
            image = pygame.image.load(pict).convert_alpha()
            screen.blit(image, (0, 0))
            pygame.display.flip()


switch101(scene1)
while scene is not None:
    scene()
pygame.quit()
