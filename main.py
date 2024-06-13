from time import perf_counter as clock
from HAND_TRACKING_MODULE import HandTracker
import cv2
from math import sqrt
import pyautogui


def map_value(value, left_min, left_max, right_min, right_max):

    left_span = left_max - left_min
    right_span = right_max - right_min
    value_scaled = float(value - left_min) / float(left_span)
    return right_min + (value_scaled * right_span)


def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    w, h = pyautogui.size()
    zone = 100  
    smoothing = 5
    plocx, plocy = 0, 0
    clockx, clocky = 0, 0
    tracker = HandTracker(detect_conf=0.5, track_conf=0.5)

    TEXT_FACE = cv2.FONT_HERSHEY_DUPLEX
    TEXT_SCALE = 1.5
    TEXT_THICKNESS = 2
    TEXT = "clicked"

    while cap.isOpened():  
        success, img = cap.read()
        if not success:
            break
        img = cv2.flip(img, 1)

        tracker.find_hands(img)
        li = tracker.findPosition(img, draw=False)
        if len(li):
            _, x4, y4 = li[4]
            _, x8, y8 = li[8]
            _, x12, y12 = li[12]
            if li[8][2] < li[6][2]:
                xmouse = map_value(x8, zone, 640 - zone, 0, w)
                ymouse = map_value(y8, zone, 480 - zone, 0, h)

                clockx = plocx + (xmouse - plocx) / smoothing
                clocky = plocy + (ymouse - plocy) / smoothing

                dist = sqrt((x4 - x8) ** 2 + (y4 - y8) ** 2)
                dist1 = sqrt((x12 - x4) ** 2 + (y12 - y4) ** 2)

                pyautogui.moveTo(clockx, clocky)
                cv2.circle(img, (x8, y8), 15, (230, 255, 0), cv2.FILLED)
                plocx, plocy = clockx, clocky

                if dist < 30:
                    pyautogui.click()
                    cv2.circle(img, (x8, y8), 15, (0, 0, 255), cv2.FILLED)
                    cv2.putText(
                        img,
                        TEXT,
                        (x8, y8),
                        TEXT_FACE,
                        TEXT_SCALE,
                        (127, 255, 127),
                        TEXT_THICKNESS,
                        cv2.LINE_AA,
                    )
                    print("clicked")

                if dist1 < 110:
                    pyautogui.scroll(-50)

        cv2.imshow("Live", img)
        key = cv2.waitKey(1)
        if key == ord("q") or key == 27: 
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
