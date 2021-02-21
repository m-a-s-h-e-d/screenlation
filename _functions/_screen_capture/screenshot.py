from PIL import ImageGrab

class ScreenCapture:
    def __init__(self):
        self.x1
        self.y1
        self.x2
        self.y2

    def set_mouse_pos_1(self, x, y):
        self.x1, self.y1 = x, y

    def set_mouse_pos_2(self, x, y):
        self.x2, self.y2 = x, y

    def grab_image(self):
        # print("Outputs: " + str(self.x1) + " " + str(self.y1) + " " + str(self.x2) + " "+ str(self.y2))
        img = ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2))
        img.show()

    def fullscreen_image(self, x, y):
        img = ImageGrab.grab(bbox=(0, 0, x, y))
        img.show()
