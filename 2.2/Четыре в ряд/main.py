import pygame
import sys
from copy import deepcopy


class Game():

    def __init__(self):
        self.running = True
        pygame.init()
        pygame.display.set_caption("The best game ever")

        self.SCREEN_WIDTH = 560
        self.SCREEN_HEIGHT = 720
        self.FPS = 30

        self.window = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.display = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.battleground = Battleground()
        self.current_col = 0
        self.current_player = 1

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if self.current_col > 0:
                            self.current_col -= 1
                    if event.key == pygame.K_d:
                        if self.current_col < 5:
                            self.current_col += 1
                    if event.key == pygame.K_RETURN:
                        if self.battleground.matrix_of_battleground[self.current_col][-1] == 0:
                            i, j = self.battleground.throw_marble(
                                self.current_col, self.current_player)
                            self.check_victory(i, j)
                            match self.current_player:
                                case 1:
                                    self.current_player = 2
                                case 2:
                                    self.current_player = 1

            self.window.fill('black')
            self.battleground.update(self.current_col)
            self.clock.tick(self.FPS)
            pygame.display.update()

    def check_victory(self, i, j):
        matrix = deepcopy(self.battleground.matrix_of_battleground)
        count = self.__detour(matrix, "LR", i, j)

        for dir in ["UD", "LR", "D2", "D1"]:
            count = self.__detour(matrix, dir, i, j)
            if count >= 3:
                self.victory()

    def __detour(self, matrix, dir, i, j):
        if i > len(matrix)-1 or i < 0:
            return 0
        if j > len(matrix[0])-1 or j < 0:
            return 0
        sum_of = 0
        match dir:
            case "LR":
                if not (matrix[i][j] == self.current_player):
                    return 0
                sum_of += self.__detour(matrix, "L", i-1, j)
                sum_of += self.__detour(matrix, "R", i+1, j)
            case "UD":
                if not (matrix[i][j] == self.current_player):
                    return 0
                sum_of += self.__detour(matrix, "U", i, j+1)
                sum_of += self.__detour(matrix, "D", i, j-1)
            case "L":
                if (matrix[i][j] == self.current_player):
                    sum_of += 1
                    sum_of += self.__detour(matrix, "L", i-1, j)
                else:
                    return 0
            case "R":
                if (matrix[i][j] == self.current_player):
                    sum_of += 1
                    sum_of += self.__detour(matrix, "R", i+1, j)
                else:
                    return 0
            case "D":
                if (matrix[i][j] == self.current_player):
                    sum_of += 1
                    sum_of += self.__detour(matrix, "D", i, j-1)
                else:
                    return 0
            case "D1":
                if not (matrix[i][j] == self.current_player):
                    return 0
                sum_of += self.__detour(matrix, "D1R", i+1, j+1)
                sum_of += self.__detour(matrix, "D1L", i-1, j-1)
            case "D2":
                if not (matrix[i][j] == self.current_player):
                    return 0
                sum_of += self.__detour(matrix, "D2R", i+1, j-1)
                sum_of += self.__detour(matrix, "D2L", i-1, j+1)
            case "D1R":
                if (matrix[i][j] == self.current_player):
                    sum_of += 1
                    sum_of += self.__detour(matrix, "D1R", i+1, j+1)
                else:
                    return 0
            case "D1L":
                if (matrix[i][j] == self.current_player):
                    sum_of += 1
                    sum_of += self.__detour(matrix, "D1L", i-1, j-1)
                else:
                    return 0
            case "D2R":
                if (matrix[i][j] == self.current_player):
                    sum_of += 1
                    sum_of += self.__detour(matrix, "D2R", i+1, j-1)
                else:
                    return 0
            case "D2L":
                if (matrix[i][j] == self.current_player):
                    sum_of += 1

                    sum_of += self.__detour(matrix, "D2L", i-1, j+1)
                else:
                    return 0

        return sum_of

    def victory(self):
        victory = pygame.sprite.Sprite()
        victory.image = pygame.image.load('Victory.png').convert_alpha()
        victory.rect = victory.image.get_rect(
            center=self.display.get_rect().center)
        esc = False
        while not esc:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        esc = True
                        self.current_player = 2
                        self.battleground.restart()
            self.display.blit(victory.image, victory.rect)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
        print("VICTORY")


class Battleground():

    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.matrix_of_battleground = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

    def restart(self):
        self.matrix_of_battleground = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

    def update(self, current_col):
        for col in range(len(self.matrix_of_battleground)):
            for row in range(len(self.matrix_of_battleground[0])):
                self.yellow = pygame.image.load('red.png').convert_alpha()
                self.red = pygame.image.load('yellow.png').convert_alpha()
                if self.matrix_of_battleground[col][::-1][row] == 1:
                    self.surface.blit(
                        self.yellow, (col*(100-8), 50+(row+1)*(100-8)))
                if self.matrix_of_battleground[col][::-1][row] == 2:
                    self.surface.blit(
                        self.red, (col*(100-8), 50+(row+1)*(100-8)))

        for i in range(6):
            for j in range(1, 7):
                cell = pygame.image.load('cell.png').convert_alpha()
                self.surface.blit(cell, (i*(100-8), 50+j*(100-8)))

            pointer = pygame.image.load('pointer.png').convert_alpha()
            self.surface.blit(pointer, (current_col*(100-8), 50))

    def throw_marble(self, col: int, player):
        yellow = pygame.image.load('red.png').convert_alpha()
        red = pygame.image.load('yellow.png').convert_alpha()
        index = 5
        for i in range(len(matrix := self.matrix_of_battleground[col][::-1])):
            if matrix[i] != 0:
                index = i-1
                break

        t_object = pygame.sprite.Sprite()
        if player == 1:
            t_object.image = yellow
        if player == 2:
            t_object.image = red

        y = 50+(index+1)*(100-8)
        for i in self.__anim_func(0, y, None):
            self.surface.fill((0, 0, 0))
            self.surface.blit(t_object.image, ((100-8) * col, i))
            self.update(col)

            pygame.display.update()

        index_ap = self.matrix_of_battleground[col].index(0)
        self.matrix_of_battleground[col][index_ap] = player
        return (col, index_ap)

    def __anim_func(self, start, end, t):
        increment = 23
        for i in range(start, end, increment):
            yield i


if __name__ == "__main__":
    game = Game()
    game.run()
