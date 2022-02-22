# Java
# @autor Kenneth Castillo
# @param Int, strings, list
# Librerias
import pygame

# Kenneth Castillo
# Proyecto Programable Basico
# Tutorias I Semestre 2022
# Instituto Tecnologico de Costa Rica

# Esta seccion contiene la ventana inicial de la aplicacion.


def MainWindow():
    pygame.init()
    pygame.display.set_caption("Proyecto Basico Programable")
    # Dibujamos la pantalla
    screen = pygame.display.set_mode([1280, 720])

    # Mientras se este corriendo mostramos pantalla
    running = True
    while running:

        # El ususario dio click en el boton cerrar?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Completamos la ventana con el conlor elegido
        screen.fill((12, 183, 242)) # No existe el transparente

        # Dibujamos un circulo
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.draw.rect(screen, (0, 0, 255), [0, 640, 1280, 80], 0)

        # Mostramos la pantalla
        pygame.display.update() # Actualizar toda la pantalla
        pygame.display.flip() # Ahorrar memoria

    # Salimos de python
    pygame.quit()

# Esctructura del main
if __name__ == '__main__':
    MainWindow()
