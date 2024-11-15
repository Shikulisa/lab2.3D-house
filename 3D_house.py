import cairo
import math


def create_surface(width=800, height=600):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    ctx = cairo.Context(surface)

    # Fill background with white
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    return surface, ctx


def apply_mirror_transformation(ctx, width):
    # Flip the image along the Y-axis
    ctx.translate(width, 0)  # Move the origin to the right edge
    ctx.scale(-1, 1)  # Scale X-axis negatively for mirroring


def draw_main_house(ctx):
    # Main house body - front wall
    ctx.move_to(200, 300)
    ctx.line_to(500, 300)
    ctx.line_to(500, 150)
    ctx.line_to(200, 150)
    ctx.close_path()

    # Fill with beige color
    ctx.set_source_rgb(0.96, 0.87, 0.78)
    ctx.fill_preserve()
    ctx.set_source_rgb(0.4, 0.3, 0.2)
    ctx.stroke()

    # Side wall for 3D effect
    ctx.move_to(500, 300)
    ctx.line_to(600, 250)
    ctx.line_to(600, 100)
    ctx.line_to(500, 150)
    ctx.close_path()

    # Fill with slightly darker beige for shadow
    ctx.set_source_rgb(0.93, 0.84, 0.75)
    ctx.fill_preserve()
    ctx.set_source_rgb(0.4, 0.3, 0.2)
    ctx.stroke()




def draw_windows(ctx):
    # Function to draw a single window
    def draw_window(x, y, width=60, height=70):
        # Window frame
        ctx.rectangle(x, y, width, height)
        ctx.set_source_rgb(0.4, 0.3, 0.2)
        ctx.stroke()

        # Window panes
        ctx.set_source_rgb(0.7, 0.9, 1.0)
        ctx.rectangle(x + 2, y + 2, width - 4, height / 2 - 2)
        ctx.fill()
        ctx.rectangle(x + 2, y + height / 2 + 2, width - 4, height / 2 - 4)
        ctx.fill()

        # Window divider
        ctx.set_source_rgb(0.4, 0.3, 0.2)
        ctx.move_to(x, y + height / 2)
        ctx.line_to(x + width, y + height / 2)
        ctx.stroke()

    # Draw front windows
    draw_window(250, 180)  # Left window
    draw_window(390, 180)  # Right window

    # Side window
    draw_window(520, 160, width=50, height=60)


def draw_dormer_window(ctx):
    # Dormer structure
    ctx.move_to(320, 100)
    ctx.line_to(380, 100)
    ctx.line_to(380, 140)
    ctx.line_to(320, 140)
    ctx.close_path()

    ctx.set_source_rgb(0.96, 0.87, 0.78)
    ctx.fill_preserve()
    ctx.set_source_rgb(0.4, 0.3, 0.2)
    ctx.stroke()

    # Dormer roof
    ctx.move_to(310, 100)
    ctx.line_to(350, 80)
    ctx.line_to(390, 100)
    ctx.close_path()

    ctx.set_source_rgb(0.91, 0.33, 0.13)
    ctx.fill_preserve()
    ctx.set_source_rgb(0.4, 0.3, 0.2)
    ctx.stroke()

    # Dormer window
    ctx.rectangle(330, 110, 40, 25)
    ctx.set_source_rgb(0.7, 0.9, 1.0)
    ctx.fill_preserve()
    ctx.set_source_rgb(0.4, 0.3, 0.2)
    ctx.stroke()


def draw_door(ctx):
    # Door frame
    ctx.rectangle(200, 200, 40, 100)
    ctx.set_source_rgb(0.6, 0.4, 0.2)
    ctx.fill_preserve()
    ctx.set_source_rgb(0.4, 0.3, 0.2)
    ctx.stroke()

    # Door handle
    ctx.arc(210, 250, 3, 0, 2 * math.pi)
    ctx.set_source_rgb(0.7, 0.7, 0.7)
    ctx.fill()


def main():
    # Create surface and context
    surface, ctx = create_surface()

    # Apply mirroring transformation
    apply_mirror_transformation(ctx, width=800)

    # Set line width for all drawings
    ctx.set_line_width(2)

    # Draw house components
    draw_main_house(ctx)
    # draw_roof(ctx)
    draw_windows(ctx)
    draw_dormer_window(ctx)
    draw_door(ctx)

    # Save the drawing
    surface.write_to_png("3d_house.png")


if __name__ == "__main__":
    main()
