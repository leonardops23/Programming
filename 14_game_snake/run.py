import pygame

# --- Configuración del Juego ---
# Usamos una clase para organizar las constantes, ¡es una buena práctica!
class Config:
    TITLE = "Solo la Cuadrícula"
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    GRID_SIZE = 20  # Tamaño de cada celda (20x20 píxeles)
    # GRID_WIDTH y GRID_HEIGHT se calculan automáticamente
    GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
    GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
    FPS = 60 # Un FPS más alto para una ventana más fluida

# Colores (RGB)
BLACK = (0, 0, 0) # Fondo de la pantalla
GRAY = (50, 50, 50) # Color de las líneas de la cuadrícula

# 1. Inicializar Pygame
pygame.init()

# 2. Configurar la pantalla
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
pygame.display.set_caption(Config.TITLE)

# 3. Crear un reloj para controlar la velocidad del juego (aunque aquí no haya movimiento)
clock = pygame.time.Clock()

# --- Función para dibujar la cuadrícula ---
def draw_grid():
    # Dibujar líneas verticales
    for x in range(0, Config.SCREEN_WIDTH, Config.GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, Config.SCREEN_HEIGHT))
    # Dibujar líneas horizontales
    for y in range(0, Config.SCREEN_HEIGHT, Config.GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (Config.SCREEN_WIDTH, y))

# --- Bucle principal de la aplicación ---
running = True
while running:
    # 1. Manejo de Eventos: ¡Importante para poder cerrar la ventana!
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Si el usuario hace clic en la 'X' de la ventana
            running = False

    # 2. Lógica del Juego (en este caso, no hay lógica de movimiento o interacción)
    # No hay nada que actualizar aquí, solo una pantalla estática.

    # 3. Dibujar en Pantalla
    screen.fill(BLACK) # Limpiar la pantalla con un color de fondo (negro)
    draw_grid() # Dibujar la cuadrícula sobre el fondo negro

    # 4. Actualizar la Pantalla
    pygame.display.flip() # Mostrar todo lo que se ha dibujado en este fotograma

    # Controlar el FPS para asegurar que la ventana se mantenga responsiva
    clock.tick(Config.FPS)

# 5. Salir de Pygame cuando el bucle termina
pygame.quit()
print("Ventana de cuadrícula cerrada.")