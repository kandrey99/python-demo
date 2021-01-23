import pygame

pygame.init()
pygame.font.init()

FPS = 60


class App:
    def __init__(self):
        self.size = self.weight, self.height = 640, 400
        self._running = True
        self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._clock = pygame.time.Clock()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # print(self._player._path._path)

    def update(self):
        pass

    def render(self):
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def run(self):
        while self._running:
            self._clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.update()
            self.render()
        self.cleanup()
