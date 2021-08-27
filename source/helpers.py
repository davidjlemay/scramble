from tkinter import dnd

class DragManager():
    def make_draggable(self, widget):
        widget.bind("<Button-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def on_drag(self, event):
        widget = event.widget
        x = widget.winfo_x() + event.x
        y = widget.winfo_y() + event.y
        widget.place(x=x, y=y)

    def on_drop(self, event):
#       Player.place_tile(i, j, tile)
        pass


def press(self, event):
    if dnd.dnd_start(self, event):
        # where the pointer is relative to the label widget:
        self.x_off = event.x
        self.y_off = event.y
        # where the widget is relative to the canvas:
        self.x_orig, self.y_orig = self.canvas.coords(self.id)