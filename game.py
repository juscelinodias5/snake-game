import sys
import time
import pygame
from snake import Snake
from fruit import Fruit
import random

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HIGHT = 640, 480
KEY_DIRECTION_MAP = {
    pygame.K_LEFT: 'esquerda',
    pygame.K_RIGHT: 'direita',
    pygame.K_UP: 'cima',
    pygame.K_DOWN: 'baixo'
}


class Game:

    def __init__(self) -> None:
        pygame.init()
        self.score = 0
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Jogo da Cobrinha')
        self.clock = pygame.time.Clock()
        POSITION_CENTER = self.screen.get_rect().center

        self.snake = Snake(WHITE, POSITION_CENTER[0], POSITION_CENTER[1])
        self.fruit = Fruit(RED, random.randint(
            1, SCREEN_WIDTH), random.randint(1, SCREEN_HIGHT))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.snake.direction = KEY_DIRECTION_MAP.get(event.key)

    def update(self):
        self.snake.move_snake()
        self.screen.fill(BLACK)
        self.snake.draw_snake(self.screen)
        self.fruit.draw_fruit(self.screen)
        if self.check_collision_fruit():
            self.fruit.change_position(SCREEN_SIZE)
            self.snake.add_cell_to_snake()
            self.snake.speed = 9
            self.score += 10
        if self.check_collision_game_over():
            self.running = False

    def draw_game(self):
        if not self.running:
            font = pygame.font.SysFont('Arial', 60)
            game_over_text = font.render('Game Over', True, (255, 0, 0))
            self.screen.blit(game_over_text, (SCREEN_WIDTH //
                                              2 - 120, SCREEN_HIGHT // 2 - 30))
            pygame.display.flip()
            time.sleep(2)

        # desenhando o score
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        # atualizando a tela
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)
            pygame.time.delay(self.snake.speed)
            self.handle_events()
            self.update()
            self.draw_game()

    def check_collision_fruit(self):
        if self.snake.snake_body[0].colliderect(self.fruit.fruit_rect):
            return True

    def check_collision_game_over(self):
        if self.snake.snake_body[0].left < 0 or self.snake.snake_body[0].right > SCREEN_WIDTH or self.snake.snake_body[0].top < 0 or self.snake.snake_body[0].bottom > SCREEN_HIGHT:
            return True
        for i in range(1, len(self.snake.snake_body)):
            if self.snake.snake_body[0].colliderect(self.snake.snake_body[i]):
                return True


if __name__ == '__main__':
    jogo = Game()
    jogo.run()
