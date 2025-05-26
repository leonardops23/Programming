import pygame
import sys
import random
from enum import Enum, auto
from typing import List, Tuple, Optional
from dataclasses import dataclass

# Constantes del juego
class Config:
    """Configuración del juego"""
    TITLE = "Snake Game"
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    GRID_SIZE = 20
    GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
    GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
    FPS = 10
    
    # Colores (RGB)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (100, 100, 100)
    DARK_GREEN = (0, 150, 0)

class Direction(Enum):
    """Enumeración para las direcciones de movimiento"""
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

@dataclass
class Point:
    """Clase para representar un punto en la cuadrícula"""
    x: int
    y: int
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

class Snake:
    """Clase que representa la serpiente del juego"""
    
    def __init__(self, start_pos: Point):
        """Inicializa la serpiente con una posición inicial"""
        self.body: List[Point] = [start_pos]
        self.direction = Direction.RIGHT
        self.grow_pending = False
        
        # Diccionario para mapear direcciones a cambios de coordenadas
        self.direction_vectors = {
            Direction.UP: Point(0, -1),
            Direction.DOWN: Point(0, 1),
            Direction.LEFT: Point(-1, 0),
            Direction.RIGHT: Point(1, 0)
        }
        
        # Direcciones opuestas (para evitar movimientos inválidos)
        self.opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
    
    def get_head(self) -> Point:
        """Retorna la posición de la cabeza de la serpiente"""
        return self.body[0]
    
    def change_direction(self, new_direction: Direction) -> None:
        """Cambia la dirección de la serpiente si es válida"""
        if new_direction != self.opposite_directions[self.direction]:
            self.direction = new_direction
    
    def move(self) -> None:
        """Mueve la serpiente en la dirección actual"""
        direction_vector = self.direction_vectors[self.direction]
        head = self.get_head()
        
        # Calcular nueva posición de la cabeza
        new_head = Point(
            (head.x + direction_vector.x) % Config.GRID_WIDTH,
            (head.y + direction_vector.y) % Config.GRID_HEIGHT
        )
        
        # Insertar nueva cabeza al inicio del cuerpo
        self.body.insert(0, new_head)
        
        # Si no debe crecer, eliminar la cola
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
    
    def grow(self) -> None:
        """Marca la serpiente para crecer en el próximo movimiento"""
        self.grow_pending = True
    
    def check_collision(self) -> bool:
        """Verifica si la serpiente colisiona consigo misma"""
        head = self.get_head()
        # Verificar si la cabeza está en alguna parte del cuerpo (excepto la cabeza misma)
        return head in self.body[1:]

class Food:
    """Clase que representa la comida en el juego"""
    
    def __init__(self, snake_body: List[Point]):
        """Inicializa la comida en una posición aleatoria válida"""
        self.position = self._generate_position(snake_body)
    
    def _generate_position(self, snake_body: List[Point]) -> Point:
        """Genera una posición aleatoria que no esté ocupada por la serpiente"""
        while True:
            pos = Point(
                random.randint(0, Config.GRID_WIDTH - 1),
                random.randint(0, Config.GRID_HEIGHT - 1)
            )
            # Asegurarse que la comida no aparezca sobre la serpiente
            if pos not in snake_body:
                return pos
    
    def respawn(self, snake_body: List[Point]) -> None:
        """Reposiciona la comida cuando es consumida"""
        self.position = self._generate_position(snake_body)

class Game:
    """Clase principal del juego que maneja la lógica y el renderizado"""
    
    def __init__(self):
        """Inicializa el juego, pygame y los componentes principales"""
        # Inicializar pygame
        pygame.init()
        pygame.display.set_caption(Config.TITLE)
        
        # Crear la ventana del juego
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 36)
        self.small_font = pygame.font.SysFont('Arial', 24)
        
        # Estado del juego
        self.running = True
        self.game_over = False
        self.score = 0
        
        # Crear los objetos del juego
        self._init_game_objects()
    
    def _init_game_objects(self) -> None:
        """Inicializa los objetos del juego (serpiente y comida)"""
        # Posición inicial en el centro
        start_pos = Point(Config.GRID_WIDTH // 2, Config.GRID_HEIGHT // 2)
        self.snake = Snake(start_pos)
        self.food = Food(self.snake.body)
    
    def reset_game(self) -> None:
        """Reinicia el juego a su estado inicial"""
        self.game_over = False
        self.score = 0
        self._init_game_objects()
    
    def process_events(self) -> None:
        """Procesa los eventos de pygame (teclado, ratón, etc.)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Procesar eventos de teclado
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    # Reiniciar el juego con la tecla R
                    if event.key == pygame.K_r:
                        self.reset_game()
                else:
                    # Cambiar dirección de la serpiente
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(Direction.RIGHT)
    
    def update(self) -> None:
        """Actualiza el estado del juego"""
        if self.game_over:
            return
        
        # Mover la serpiente
        self.snake.move()
        
        # Verificar colisión con la comida
        if self.snake.get_head() == self.food.position:
            self.snake.grow()
            self.food.respawn(self.snake.body)
            self.score += 1
        
        # Verificar colisión con sí misma
        if self.snake.check_collision():
            self.game_over = True
    
    def render(self) -> None:
        """Renderiza el estado actual del juego"""
        # Limpiar la pantalla
        self.screen.fill(Config.BLACK)
        
        # Dibujar la cuadrícula (opcional)
        self._draw_grid()
        
        # Dibujar la serpiente
        for i, segment in enumerate(self.snake.body):
            color = Config.GREEN if i == 0 else Config.DARK_GREEN
            pygame.draw.rect(
                self.screen, 
                color, 
                (segment.x * Config.GRID_SIZE, 
                 segment.y * Config.GRID_SIZE, 
                 Config.GRID_SIZE, 
                 Config.GRID_SIZE)
            )
        
        # Dibujar la comida
        pygame.draw.rect(
            self.screen, 
            Config.RED, 
            (self.food.position.x * Config.GRID_SIZE, 
             self.food.position.y * Config.GRID_SIZE, 
             Config.GRID_SIZE, 
             Config.GRID_SIZE)
        )
        
        # Mostrar la puntuación
        score_text = self.font.render(f'Score: {self.score}', True, Config.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Mostrar mensaje de Game Over si corresponde
        if self.game_over:
            self._draw_game_over()
        
        # Actualizar la pantalla
        pygame.display.flip()
    
    def _draw_grid(self) -> None:
        """Dibuja una cuadrícula en el fondo (opcional)"""
        for x in range(0, Config.SCREEN_WIDTH, Config.GRID_SIZE):
            pygame.draw.line(self.screen, Config.GRAY, 
                            (x, 0), (x, Config.SCREEN_HEIGHT), 1)
        for y in range(0, Config.SCREEN_HEIGHT, Config.GRID_SIZE):
            pygame.draw.line(self.screen, Config.GRAY, 
                            (0, y), (Config.SCREEN_WIDTH, y), 1)
    
    def _draw_game_over(self) -> None:
        """Dibuja la pantalla de Game Over"""
        # Crear un overlay semitransparente
        overlay = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        overlay.set_alpha(180)  # Transparencia (0-255)
        overlay.fill(Config.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Texto de Game Over
        game_over_text = self.font.render('¡GAME OVER!', True, Config.RED)
        text_rect = game_over_text.get_rect(center=(Config.SCREEN_WIDTH//2, Config.SCREEN_HEIGHT//2 - 50))
        self.screen.blit(game_over_text, text_rect)
        
        # Texto de puntuación final
        score_text = self.font.render(f'Puntuación final: {self.score}', True, Config.WHITE)
        score_rect = score_text.get_rect(center=(Config.SCREEN_WIDTH//2, Config.SCREEN_HEIGHT//2))
        self.screen.blit(score_text, score_rect)
        
        # Texto para reiniciar
        restart_text = self.small_font.render('Presiona R para reiniciar', True, Config.WHITE)
        restart_rect = restart_text.get_rect(center=(Config.SCREEN_WIDTH//2, Config.SCREEN_HEIGHT//2 + 50))
        self.screen.blit(restart_text, restart_rect)
    
    def run(self) -> None:
        """Bucle principal del juego"""
        while self.running:
            self.process_events()
            self.update()
            self.render()
            self.clock.tick(Config.FPS)
        
        # Limpiar recursos al salir
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    # Crear y ejecutar el juego
    game = Game()
    game.run()
