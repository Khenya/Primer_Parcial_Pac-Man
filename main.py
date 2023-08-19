import arcade
from player import Player
# constantes
WIDTH = 1000
HEIGHT = 600
TITLE = "PAC-MAN"
SPEED = 1

class PacMan(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # sprite list para dibujar
        self.sprites = arcade.SpriteList()
        self.player = Player(
            "img/player.png", 
            1, 
            center_x=WIDTH / 2, 
            center_y=HEIGHT / 2
        )
        self.sprites.append(self.player)
        self.distance = 0


    def on_key_press(self, symbol: int, modifiers: int):
        """Metodo para detectar teclas que han sido presionada
        El punto se movera con las teclas de direccion.
        Argumentos:
            symbol: tecla presionada
            modifiers: modificadores presionados
        """
        if symbol == arcade.key.UP:
            self.player.change_y = SPEED
        if symbol == arcade.key.DOWN:
            self.player.change_y = -SPEED

        if symbol == arcade.key.LEFT:
            self.player.change_x = -SPEED
        if symbol == arcade.key.RIGHT:
            self.player.change_x= SPEED


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_x = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_y = 0

    def on_update(self, delta_time: float):
        """Metodo para actualizar objetos de la app"""
        self.sprites.update()


    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()

def main():
    app = PacMan()
    arcade.run()


if __name__ == "__main__":
    main()