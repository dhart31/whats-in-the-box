from pynput import mouse, keyboard
import pyautogui
import threading
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
class CaptureRegion:
    def __init__(self):
        self.start_point = None
        self.end_point = None
        self.drag_started = False

    def on_move(self, x, y):
        if self.drag_started:
            self.end_point = (x, y)

    def on_click(self, x, y, button, pressed):
        print(f"Mouse {'pressed' if pressed else 'released'} at ({x}, {y}) with {button}")

        if button == mouse.Button.left:
            if pressed:
                self.start_point = (x, y)
                self.drag_started = True
            else:
                self.drag_started = False
        
        if button == mouse.Button.right and not pressed:
            return False

    def on_press(self, key):
        if key == keyboard.Key.ctrl_l and self.start_point and self.end_point:
            self.capture_region()

    def capture_region(self):
        if self.start_point and self.end_point:
            region = (self.start_point[0], self.start_point[1], self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])
            screenshot = pyautogui.screenshot(region=region)
            text = pytesseract.image_to_string(screenshot,lang='jpn')
            with open('output.txt', 'w', encoding='utf-8') as f:
                f.write(text)            
            screenshot.save('region_capture.png')



capture = CaptureRegion()

keyboard_listener = keyboard.Listener(on_press=capture.on_press)
keyboard_thread = threading.Thread(target=keyboard_listener.start)
keyboard_thread.start()

with mouse.Listener(on_move=capture.on_move, on_click=capture.on_click) as listener:
    listener.join()

def capture_region(self):
    if self.start_point and self.end_point:
        region = (self.start_point[0], self.start_point[1], self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])
        print(region)
        screenshot = pyautogui.screenshot(region=region)
        text = pytesseract.image_to_string(screenshot)
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        screenshot.save('region_capture.png')