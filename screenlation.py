import tkinter

from _functions._screen_capture.Screenshot import ScreenCapture

class App:
    def __init__(self, root):
        self.root = root
        self.lmb_down = False
        self.root = tkinter.Tk()
        # self.root.attributes("-alpha", 0.3) --- Fullscreen for selection
        self.root.bind("<ButtonPress-1>", self.on_mouse_down)
        self.root.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.root.bind("<B1-Motion>", self.motion)

    def get_coordinate(self):
        x1 = self.root.winfo_pointerx()
        y1 = self.root.winfo_pointery()
        ScreenCapture.set_mouse_pos_1(self, x1, y1)

    def on_mouse_down(self):
        self.lmb_down = True
        self.get_coordinate()

    def on_mouse_up(self):
        self.root.after_cancel(self.after_id)
        x2 = self.root.winfo_pointerx() - self.root.winfo_rootx()
        y2 = self.root.winfo_pointery() - self.root.winfo_rooty()
        ScreenCapture.set_mouse_pos_2(self, x2, y2)
        ScreenCapture.grab_image(self)

    def motion(self):
        if self.lmb_down:
            self.after_id = self.root.after(250, self.motion)

root = tkinter.Tk()
app = App(root)
root.mainloop()