import pygame

LEN_SNAKE = 13

class Snake:

    def __init__(self, color, position_x, position_y):

        self.color = color
        self._position_x = position_x
        self._position_y = position_y
        self.width = LEN_SNAKE
        self.height = LEN_SNAKE
        self.direction = 'direita'
        self._speed = 240
        self.snake_body = [pygame.Rect(
            self.position_x, self.position_y, self.width, self.height)]

        self.clock = pygame.time.Clock()

    def move_snake(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[i].x = self.snake_body[i-1].x
            self.snake_body[i].y = self.snake_body[i-1].y

        if self.direction == 'direita':
            self.snake_body[0].x += LEN_SNAKE
        elif self.direction == 'esquerda':
            self.snake_body[0].x -= LEN_SNAKE
        elif self.direction == 'cima':
            self.snake_body[0].y -= LEN_SNAKE
        elif self.direction == 'baixo':
            self.snake_body[0].y += LEN_SNAKE

    def draw_snake(self, screen):
        for i in range(len(self.snake_body)):
            body = self.snake_body[i]
            pygame.draw.rect(screen, self.color, body)

    def add_cell_to_snake(self):
        last_cell = self.snake_body[-1]
        if self.direction == 'direita':
            cell = pygame.Rect(last_cell.x - LEN_SNAKE,
                               last_cell.y, self.width, self.height)
            self.snake_body.append(cell)
        elif self.direction == 'esquerda':
            cell = pygame.Rect(last_cell.x + LEN_SNAKE,
                               last_cell.y, self.width, self.height)
            self.snake_body.append(cell)
        elif self.direction == 'cima':
            cell = pygame.Rect(last_cell.x, last_cell.y +
                               LEN_SNAKE, self.width, self.height)
            self.snake_body.append(cell)
        elif self.direction == 'baixo':
            cell = pygame.Rect(last_cell.x, last_cell.y -
                               LEN_SNAKE, self.width, self.height)
            self.snake_body.append(cell)

    # ----------- Getters e Setters -----------------

    @property
    def position_x(self):
        return self._position_x

    @position_x.setter
    def position_x(self, valor):
        self._position_x = valor

    @property
    def position_y(self):
        return self._position_y

    @position_y.setter
    def position_y(self, valor):
        self._position_y = valor

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, valor):
        self._speed -= valor
