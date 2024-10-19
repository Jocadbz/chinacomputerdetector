import keyboard
import cv2


class Logger:
    def __init__(self):
        self.log = ""

    def add_key(self, key_name):
        self.log += key_name if len(key_name) == 1 else f"[{key_name.upper()}]"
        self.check_for_china()
        self.check_for_america()

    def check_for_china(self):
        if self.log.lower().endswith("china"):
            print("CHINA WINS")
            my_img = cv2.imread("+socialcredit.jpg", cv2.IMREAD_COLOR)
            cv2.imshow("+ SOCIAL CREDIT, CONGRATS!!!", my_img)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()

    def check_for_america(self):
        if self.log.lower().endswith("america"):
            print("FUK AMERICA!")
            my_img = cv2.imread("-socialcredit.png", cv2.IMREAD_COLOR)
            cv2.imshow("- SOCIAL CREDIT, YOU NEED TO BE EXECUTED, GLORY TO THE CCP!!!", my_img)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()

    def clear_log(self):
        self.log = ""

def on_key_release(event):
    logger.add_key(event.name)

if __name__ == "__main__":
    logger = Logger()

    keyboard.on_release(on_key_release)
    keyboard.wait()
