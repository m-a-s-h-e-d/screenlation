import tkinter as tk

from _functions._screen_capture.Screenshot import ScreenCapture

# Creates the container for all the frames / windows
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, CaptureScreen):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")
    
    # Allows buttons to bring page to the top of stack
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# Home Screen
class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.root = controller
        self.root.geometry("500x50")
        self.root.winfo_toplevel().title("Screenlation")
        label1 = tk.Label(self, text="Hold left mouse button and drag to draw a region for capture. Press alt-f4 to exit.")
        label1.pack(pady=10)
        button1 = tk.Button(self, text="Region Capture", command=lambda: controller.show_frame("ScreenCapture"))
        button1.pack(pady=5)
        max_width = self.root.winfo_screenwidth() * CaptureScreen.get_factor_x(self)
        max_height = self.root.winfo_screenheight() * CaptureScreen.get_factor_y(self)
        button2 = tk.Button(self, text="Fullscreen Capture", command=lambda: ScreenCapture.fullscreen_image(self, max_width, max_height))
        button2.pack(pady=5)

# Capture Screenshot Screen
class CaptureScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.root = controller
        self.lmb_down = False
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-fullscreen", True)
        self.root.bind("<ButtonPress-1>", self.on_mouse_down)
        self.root.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.root.bind("<B1-Motion>", self.on_motion)
        self.root.bind("<Escape>", controller.show_frame("Home"))

    # Calculate the width factor of monitor to 1080 pixels
    def get_factor_x(self):
        width = self.root.winfo_screenwidth()
        if width >= 1920:
            factor = width / 1920
        else:
            factor = 1920 / width
        return factor

    # Calculate the height factor of monitor to 1080 pixels
    def get_factor_y(self):
        height = self.root.winfo_screenheight()
        if height >= 1080:
            factor = height / 1080
        else:
            factor = 1080 / height
        return factor

    # Mouse button pressed, set first corner for image capture
    def on_mouse_down(self, temp):
        # print(temp)
        self.lmb_down = True
        x1 = self.root.winfo_pointerx()  * self.get_factor_x()
        y1 = self.root.winfo_pointery() * self.get_factor_y()
        ScreenCapture.set_mouse_pos_1(self, x1, y1)

    # Mouse button released, set second corner for image capture and invoke the image capture
    def on_mouse_up(self, temp):
        # print(temp)
        x2 = self.root.winfo_pointerx() * self.get_factor_x()
        y2 = self.root.winfo_pointery() * self.get_factor_y()
        ScreenCapture.set_mouse_pos_2(self, x2, y2)
        ScreenCapture.grab_image(self)

    # Mouse movement shows visual input
    def on_motion(self, temp):
        if self.lmb_down:
            pass

app = App()
app.mainloop()