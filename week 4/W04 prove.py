import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    draw_grass(canvas, 0, 0, 800, 350)
    draw_sun(canvas, 70, 50)
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 300
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    tree_center = scene_left + 600
    tree_top = scene_top + 100
    tree_height = 300
    draw_pine_tree2(canvas, tree_center, tree_top, tree_height)
    draw_snow_man(canvas, 300, 250, 200, 355)
    draw_cloud(canvas, 250, 100, 400, -50)
    draw_fence(canvas, scene_left, scene_top, scene_right, scene_bottom, 70)
    draw_fence(canvas, scene_left, scene_top - 20, scene_right, scene_bottom + 20, 50)

        
def draw_sun(canvas, x , y):
    #create the Sun
    canvas.create_oval(x, y, x + 100, y + 100, outline="yellow",fill="Yellow")

def draw_grass(canvas, grass_left, grass_top, grass_right, grass_bottom):
    #create a grass
    canvas.create_rectangle(grass_left, grass_top, grass_right, grass_bottom, fill="#92DCE0")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="green2")

def draw_pine_tree2(canvas, peak_x, peak_y, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="green2")

def draw_snow_man(canvas, man_left, man_top, man_right, man_bottom):
    #create two circle in order to make a snowman
    canvas.create_oval(man_left, man_top, man_right, man_bottom, outline="grey", width=1, fill="white")
    canvas.create_oval(man_left, man_top - 80, man_right, man_bottom - 80, outline="grey", width=1, fill="white")

def draw_cloud(canvas, c_left, c_top, c_right, c_bottom):
    #put some circles together and make a cloud
    canvas.create_oval(c_left, c_top, c_right, c_bottom, outline="white", fill="white")
    canvas.create_oval(c_left + 100, c_top, c_right + 100, c_bottom, outline="white", fill="white")
    canvas.create_oval(c_left + 200, c_top, c_right + 200, c_bottom, outline="white", fill="white")

def draw_fence(canvas, left, top, right, bottom, fence_spacing):
    #using "while" make fences
    i = 0
    while i < 800:
        i = i + 70
        canvas.create_oval(i, 250, i + 20 , 220, fill="white", outline="grey")

main()