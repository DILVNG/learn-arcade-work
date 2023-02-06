"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a new window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Samples"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Samples")

# Set the background color for Sky
arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

# Get ready to draw the Forest
arcade.start_render()

# Draw the grass and levels
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.APPLE_GREEN)

# Tree trunk Base
# Center of 100, 320
# Width of 40
# Height of 250
arcade.draw_rectangle_filled(100, 320, 40, 250, arcade.csscolor.ROSY_BROWN)

# Tree top of Tree
# Center of 100
# Height of 400
# Radius of 100
arcade.draw_circle_filled(100, 400, 100,  arcade.csscolor.DARK_GREEN)

# Tree trunk Base #2 (Right Side)
# Center of 700, 320
# Width of 40
# Height of 250
arcade.draw_rectangle_filled(700, 320, 40, 250, arcade.csscolor.SANDY_BROWN)

# Tree top of Tree #2 (Right Side)
# Center of 700
# Height of 400
# Radius of 100
arcade.draw_circle_filled(700, 400, 100,  arcade.csscolor.SEA_GREEN)

# Draw and write out a Text
arcade.draw_text("Dillon's - Night Forest Drawing",
                 10, 530,
                 arcade.color.RED_VIOLET, 25)

# Draw a Moon
arcade.draw_circle_filled(600, 550, 80, arcade.color.GHOST_WHITE)

# Tree trunk Base
# Center of 500, 200
# Width of 20
# Height of 250
arcade.draw_rectangle_filled(500, 200, 20, 250, arcade.csscolor.SIENNA)

# Tree top of Tree
# Center of 500
# Height of 350
# Radius of 100
arcade.draw_circle_filled(500, 350, 100, arcade.csscolor.DARK_OLIVE_GREEN)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()