import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_snowball(center_x, center_y, radius):
    """Draw a white snowball on screen"""
    snowball = arcade.draw_circle_filled(center_x, center_y, radius, arcade.color.WHITE)
    return snowball


def draw_eye(center_x, center_y, radius):
    """Draw an eye on screen"""
    eye = arcade.draw_circle_filled(center_x, center_y, radius, arcade.color.BLACK)
    return eye


def draw_snowman(x, y):
    """Draw a snow person"""

    # Snow
    draw_snowball(300 + x, 200 + y, 60)
    draw_snowball(300 + x, 280 + y, 50)
    draw_snowball(300 + x, 340 + y, 40)

    # Eyes
    draw_eye(285 + x, 350 + y, 5)
    draw_eye(315 + x, 350 + y, 5)


def draw_ground():
    """Draw the ground"""
    ground = arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)
    return ground


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_ground()
    draw_snowman(on_draw.snowman1_x, 10)
    draw_snowman(220, 30)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snowman1_x += 0.25


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snowman1_x = 25


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


if __name__ == "__main__":
    main()
