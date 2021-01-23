import pygame as pg


class App:
    def __init__(self):
        pg.init()
        self.fps = 60
        self.size = self.width, self.height = 640, 400
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self._display = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._clock = pg.time.Clock()
        self._running = True

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            # print(self._player._path._path)

    def update(self):
        pass

    def render(self):
        self._display.fill(pg.Color('darkslategray'))
        pg.display.flip()

    def cleanup(self):
        pg.quit()

    def run(self):
        while self._running:
            self._clock.tick(self.fps)
            pg.display.set_caption(str(self._clock.get_fps()))
            for event in pg.event.get():
                self.on_event(event)
            self.update()
            self.render()
        self.cleanup()


if __name__ == '__main__':
    app = App()
    app.run()
