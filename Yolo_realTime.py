from ultralytics import YOLO
import cv2
import math
import pyautogui
from screen_brightness_control import set_brightness, get_brightness
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def start_application():
    model = YOLO("C:\\Users\\modih\\Desktop\\FYP2\\Code\\best.pt")  # make sure to change the correct path
    class_names = list(model.names.values())

    screen_width, screen_height = pyautogui.size()

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 60)

    prev_pos = None
    smooth_factor = 0.2

    def increase_volume():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume_range = volume.GetVolumeRange()
        current_volume = volume.GetMasterVolumeLevel()
        max_volume = volume_range[1]
        volume.SetMasterVolumeLevel(min(current_volume + 1.0, max_volume), None)

    def decrease_volume():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume_range = volume.GetVolumeRange()
        current_volume = volume.GetMasterVolumeLevel()
        min_volume = volume_range[0]
        volume.SetMasterVolumeLevel(max(current_volume - 1.0, min_volume), None)

    def increase_brightness():
        new_brightness_point = 10
        current_brightness = get_brightness()
        set_brightness(new_brightness_point + current_brightness[0])

    def decrease_brightness():
        new_brightness_point = -10
        current_brightness = get_brightness()
        set_brightness(new_brightness_point + current_brightness[0])

    def close_app():
        pyautogui.hotkey("q")  

    while True:
        start_time = time.time()
        success, img = cap.read()
        img = cv2.flip(img, 1)
        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                current_class = class_names[cls]

                if conf > 0.2:
                    index_finger_x = (x1 + x2) // 2
                    index_finger_y = (y1 + y2) // 2
                    scaled_x = int(index_finger_x * screen_width / img.shape[1])
                    scaled_y = int(index_finger_y * screen_height / img.shape[0])

                    if current_class == "cursor":
                        increase_volume()
                    elif current_class == "leftclick":
                        decrease_volume()
                    elif current_class == "rightclick": 
                        close_app()    
                    elif current_class == "scrollup":
                        pause_key = "space"
                        pyautogui.press(pause_key)
                    elif current_class == "increasebrightness":
                        increase_brightness()
                    elif current_class == "decreasebrightness":
                        decrease_brightness()

        cv2.imshow("Image", img)

        end_time = time.time()
        fps = 1 / (end_time - start_time)
        print(f"FPS: {fps:.2f}")

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_application()
