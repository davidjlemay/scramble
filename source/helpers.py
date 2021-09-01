from tkinter import Canvas, dnd, Label, Toplevel


class Draggable:

    def __init__(self, name):
        self.name = name
        self.canvas = self.label = self.id = None

    def attach(self, canvas, x=10, y=10):
        if canvas is self.canvas:
            self.canvas.coords(self.id, x, y)
            return
        if self.canvas:
            self.detach()
        if not canvas:
            return
        label = Label(canvas, width=4, height=2, text=self.name, borderwidth=2, relief="raised", bg="brown")
        id = canvas.create_window(x, y, window=label, anchor="nw")
        self.canvas = canvas
        self.label = label
        self.id = id
        label.bind("<ButtonPress>", self.press)

    def detach(self):
        canvas = self.canvas
        if not canvas:
            return
        id = self.id
        label = self.label
        self.canvas = self.label = self.id = None
        canvas.delete(id)
        label.destroy()

    def press(self, event):
        if dnd.dnd_start(self, event):
            # where the pointer is relative to the label widget:
            self.x_off = event.x
            self.y_off = event.y
            # where the widget is relative to the canvas:
            self.x_orig, self.y_orig = self.canvas.coords(self.id)

    def move(self, event):
        x, y = self.where(self.canvas, event)
        self.canvas.coords(self.id, x, y)

    def putback(self):
        self.canvas.coords(self.id, self.x_orig, self.y_orig)

    def where(self, canvas, event):
        # where the corner of the canvas is relative to the screen:
        x_org = canvas.winfo_rootx()
        y_org = canvas.winfo_rooty()
        # where the pointer is relative to the canvas widget:
        x = event.x_root - x_org
        y = event.y_root - y_org
        # compensate for initial pointer offset
        return x - self.x_off, y - self.y_off

    def dnd_end(self, target, event):
        pass


class DndManager:

    def __init__(self, root):
        self.top = Toplevel(root)
        self.canvas = Canvas(self.top, width=500, height=500)
        self.canvas.pack(fill="x", expand=1)
        self.canvas.dnd_accept = self.dnd_accept
        self.dnd_id = None

    def dnd_accept(self, source, event):
        return self

    def dnd_enter(self, source, event):
        self.canvas.focus_set() # Show highlight border
        x, y = source.where(self.canvas, event)
        x1, y1, x2, y2 = source.canvas.bbox(source.id)
        dx, dy = x2-x1, y2-y1
        self.dnd_id = self.canvas.create_rectangle(x, y, x + dx, y + dy)
        self.dnd_motion(source, event)

    def dnd_motion(self, source, event):
        x, y = source.where(self.canvas, event)
        x1, y1, x2, y2 = self.canvas.bbox(self.dnd_id)
        self.canvas.move(self.dnd_id, x - x1, y - y1)

    def dnd_leave(self, source, event):
        self.top.focus_set() # Hide highlight border
        self.canvas.delete(self.dnd_id)
        self.dnd_id = None

    def dnd_commit(self, source, event):
        self.dnd_leave(source, event)
        x, y = source.where(self.canvas, event)
        source.attach(self.canvas, x, y)


def press(self, event):
    if dnd.dnd_start(self, event):
        # where the pointer is relative to the label widget:
        self.x_off = event.x
        self.y_off = event.y
        # where the widget is relative to the canvas:
        self.x_orig, self.y_orig = self.canvas.coords(self.id)
