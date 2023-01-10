import arcade

class World(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="kiya game_test")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.Square = Square(self)

class Square(arcade.Sprite):
    def __init__(self,World):
        super().__init__()
        for r in range(9):
            for i in range(9):
                x = i * 20 + 400
                y = r * 20 + 240
                
                if r % 2 == 1:
                    l = i+1
                    if l % 2 == 0:
                        arcade.draw_rectangle_filled(x,y,10,10,arcade.color.BLUE,45)
                    else:
                        arcade.draw_rectangle_filled(x,y,10,10,arcade.color.RED,45)
                else:
                    if i % 2 == 0:
                        arcade.draw_rectangle_filled(x,y,10,10,arcade.color.BLUE,45)
                    else:
                        arcade.draw_rectangle_filled(x,y,10,10,arcade.color.RED,45)


window = World()
arcade.run()
