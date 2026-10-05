import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("House Drawing - Tkinter")
root.geometry("600x600")

# Create Canvas widget
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack(fill="both", expand=True)

# Configuration for house style
LINE_COLOR = "red"
ROOF_COLOR = "brown"  # Solid brown color for roof
LINE_WIDTH = 3

# 1. Main House Body (Square base)
canvas.create_rectangle(
    200, 300, 400, 500, outline=LINE_COLOR, width=LINE_WIDTH
)

# 2. Roof (Solid brown fill, red outline, no inner lines or chimney)
canvas.create_polygon(
    200, 300, 300, 180, 400, 300, fill=ROOF_COLOR, outline=LINE_COLOR, width=LINE_WIDTH
)

# 3. Left Window
canvas.create_rectangle(
    225, 335, 270, 380, outline=LINE_COLOR, width=LINE_WIDTH
)
# Left Window Cross Pane
canvas.create_line(225, 357.5, 270, 357.5, fill=LINE_COLOR, width=LINE_WIDTH)
canvas.create_line(247.5, 335, 247.5, 380, fill=LINE_COLOR, width=LINE_WIDTH)

# 4. Right Window
canvas.create_rectangle(
    330, 335, 375, 380, outline=LINE_COLOR, width=LINE_WIDTH
)
# Right Window Cross Pane
canvas.create_line(330, 357.5, 375, 357.5, fill=LINE_COLOR, width=LINE_WIDTH)
canvas.create_line(352.5, 335, 352.5, 380, fill=LINE_COLOR, width=LINE_WIDTH)

# 5. Front Door
canvas.create_rectangle(
    275, 420, 325, 500, outline=LINE_COLOR, width=LINE_WIDTH
)
# Vertical Door Divider
canvas.create_line(300, 420, 300, 500, fill=LINE_COLOR, width=LINE_WIDTH)

# Run Tkinter event loop
root.mainloop()