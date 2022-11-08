import arcade

# Open up a window
arcade.open_window(600, 600, "Lab 02")

# Set background color
arcade.set_background_color(arcade.color_from_hex_string("#79D2EF"))

# Get ready to draw
arcade.start_render()

# Draw grass (rectangle)
arcade.draw_rectangle_filled(300, 75, 600, 150, (128, 128, 0))

# Draw house front (5-sided polygon)
arcade.draw_polygon_filled((
    (324, 49),
    (324, 309),
    (476, 413),
    (589, 304),
    (586, 81)
),
    arcade.color_from_hex_string("#FFFFFF"))

# Draw house side (4-sided polygon)
arcade.draw_polygon_filled((
    (324, 49),
    (324, 309),
    (60, 335),
    (60, 98)
),
    arcade.color_from_hex_string("#DDDDDD"))

# Draw window side (4-sided polygon)
arcade.draw_polygon_filled((
    (225, 165),
    (225, 245),
    (135, 255),
    (135, 175)
),
    arcade.color_from_hex_string("#1A1A1A"))

# Draw house top (4-sided polygon)
arcade.draw_polygon_filled((
    (324, 309),
    (60, 335),
    (170, 430),
    (476, 413)
),
    arcade.color_from_hex_string("#CCCCCC"))

# Draw house door (5-sided polygon)
arcade.draw_polygon_filled((
    (430, 73),
    (430, 251),
    (495, 250),
    (495, 79)
),
    arcade.color_from_hex_string("#552200"))

# Draw doorknob
arcade.draw_circle_filled(484, 160, 5, arcade.color_from_hex_string("#D4AA00"))

# Draw sun
arcade.draw_circle_filled(342, 575, 60, arcade.color_from_hex_string("#FFD500"))

# Draw sample text
# arcade.draw_text("Hello", 30, 30)

# Finish drawing
arcade.finish_render()

# Keep window open
arcade.run()
