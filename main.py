import arcade

my_window = arcade.open_window(800,600, "First Window Demo")
arcade.set_background_color(arcade.color.AERO_BLUE)

arcade.start_render()
#everything else goes here

for xloc in range(100,900,80):
        arcade.draw_line(xloc, 50, xloc, 70, arcade.color.BABY_POWDER, 10)
for yloc in range(100,900,80):
        arcade.draw_line(70, yloc, 900, yloc, arcade.color.BABY_POWDER, 10)

arcade.finish_render()


arcade.run()
