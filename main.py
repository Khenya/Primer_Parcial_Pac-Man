import arcade
from player import Player
# constantes
WIDTH = 1000
HEIGHT = 600
TITLE = "PAC-MAN"

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

    def on_key_press(self, key, modifiers):
        """Manejo de eventos cuando se presionan teclas"""
        print (key)
        if key == arcade.key.LEFT:
            self.player.change_x = -10
        elif key == arcade.key.RIGHT:
            self.player.change_x = 10
        elif key == arcade.key.UP:
            self.player.change_y = 10
        elif key == arcade.key.DOWN:
            self.player.change_y = -10

    def on_key_release(self, key, modifiers):
        """Manejo de eventos cuando se sueltan teclas"""
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        self.sprites.draw()
    
    

def main():
    app = PacMan()
    arcade.run()


if __name__ == "__main__":
    main()