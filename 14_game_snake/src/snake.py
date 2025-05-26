from config import Direction
from points import Point
from typing import List
from config import ConfigGame


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
            (head.x + direction_vector.x) % ConfigGame.GRID_WIDTH,
            (head.y + direction_vector.y) % ConfigGame.GRID_HEIGHT
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
