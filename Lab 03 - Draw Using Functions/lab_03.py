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


def draw_ground():
    """Draw the ground"""
    ground = arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)
    return ground


def main():
    """Run the main program"""

    # Create window, set background color, and start rendering
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw ground
    draw_ground()

    # Draw a snow person

    # Snow
    draw_snowball(300, 200, 60)
    draw_snowball(300, 280, 50)
    draw_snowball(300, 340, 40)

    # Eyes
    draw_eye(285, 350, 5)
    draw_eye(315, 350, 5)

    #  Finish and run
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()
