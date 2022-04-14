import numpy as np
import cv2
import os
from mss import mss
from PIL import Image
import argparse

max_value = 255
max_value_H = 360 // 2
low_H = 0
low_S = 0
low_V = 0
min_mask_tomate=(112,117,158)
max_mask_tomate=(118,255,254)
min_mask_cheese=(93,76,218)
max_mask_cheese=(97,106,243)
min_mask_grape=(83,0,0)
max_mask_grape=(93,255,255)
min_mask_mozzarella=(0,0,216)
max_mask_mozzarella=(180,32,255)
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'


def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H - 1, low_H)
    cv2.setTrackbarPos(low_H_name, window_detection_name, low_H)


def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H + 1)
    cv2.setTrackbarPos(high_H_name, window_detection_name, high_H)


def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S - 1, low_S)
    cv2.setTrackbarPos(low_S_name, window_detection_name, low_S)


def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S + 1)
    cv2.setTrackbarPos(high_S_name, window_detection_name, high_S)


def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V - 1, low_V)
    cv2.setTrackbarPos(low_V_name, window_detection_name, low_V)

def on_button(id,val):
    print(val)
    if val == 0:
        cv2.setTrackbarPos(low_H_name, window_detection_name, min_mask_tomate[0])
        cv2.setTrackbarPos(low_S_name, window_detection_name, min_mask_tomate[1])
        cv2.setTrackbarPos(low_V_name, window_detection_name, min_mask_tomate[2])
        cv2.setTrackbarPos(high_H_name, window_detection_name, max_mask_tomate[0])
        cv2.setTrackbarPos(high_S_name, window_detection_name, max_mask_tomate[1])
        cv2.setTrackbarPos(high_V_name, window_detection_name, max_mask_tomate[2])
    if val == 1:
        cv2.setTrackbarPos(low_H_name, window_detection_name, min_mask_cheese[0])
        cv2.setTrackbarPos(low_S_name, window_detection_name, min_mask_cheese[1])
        cv2.setTrackbarPos(low_V_name, window_detection_name, min_mask_cheese[2])
        cv2.setTrackbarPos(high_H_name, window_detection_name, max_mask_cheese[0])
        cv2.setTrackbarPos(high_S_name, window_detection_name, max_mask_cheese[1])
        cv2.setTrackbarPos(high_V_name, window_detection_name, max_mask_cheese[2])
    if val == 2:
        cv2.setTrackbarPos(low_H_name, window_detection_name, min_mask_grape[0])
        cv2.setTrackbarPos(low_S_name, window_detection_name, min_mask_grape[1])
        cv2.setTrackbarPos(low_V_name, window_detection_name, min_mask_grape[2])
        cv2.setTrackbarPos(high_H_name, window_detection_name, max_mask_grape[0])
        cv2.setTrackbarPos(high_S_name, window_detection_name, max_mask_grape[1])
        cv2.setTrackbarPos(high_V_name, window_detection_name, max_mask_grape[2])
    if val == 3:
        cv2.setTrackbarPos(low_H_name, window_detection_name, min_mask_mozzarella[0])
        cv2.setTrackbarPos(low_S_name, window_detection_name, min_mask_mozzarella[1])
        cv2.setTrackbarPos(low_V_name, window_detection_name, min_mask_mozzarella[2])
        cv2.setTrackbarPos(high_H_name, window_detection_name, max_mask_mozzarella[0])
        cv2.setTrackbarPos(high_S_name, window_detection_name, max_mask_mozzarella[1])
        cv2.setTrackbarPos(high_V_name, window_detection_name, max_mask_mozzarella[2])


def show_image(image):
    cv2.imshow('HSV image', image);
    cv2.waitKey(0);
    cv2.destroyAllWindows();
    cv2.waitKey(1)
    pass

def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V + 1)
    cv2.setTrackbarPos(high_V_name, window_detection_name, high_V)


parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv2.VideoCapture(args.camera)
bounding_box = {'top': 100, 'left': 100, 'width': 800, 'height': 800}
sct = mss()
cv2.namedWindow(window_capture_name)
cv2.namedWindow(window_detection_name)
cv2.createButton("tomato", on_button, 0)
cv2.createButton("cheese", on_button, 1)
cv2.createButton("grape", on_button, 2)
cv2.createButton("mozzarella", on_button, 3)

cv2.createTrackbar(low_H_name, window_detection_name, low_H, max_value_H, on_low_H_thresh_trackbar)
cv2.createTrackbar(high_H_name, window_detection_name, high_H, max_value_H, on_high_H_thresh_trackbar)
cv2.createTrackbar(low_S_name, window_detection_name, low_S, max_value, on_low_S_thresh_trackbar)
cv2.createTrackbar(high_S_name, window_detection_name, high_S, max_value, on_high_S_thresh_trackbar)
cv2.createTrackbar(low_V_name, window_detection_name, low_V, max_value, on_low_V_thresh_trackbar)
cv2.createTrackbar(high_V_name, window_detection_name, high_V, max_value, on_high_V_thresh_trackbar)
while True:
    detector = cv2.SimpleBlobDetector()
    screenshot = sct.grab(bounding_box)
    frame = np.asarray(screenshot.pixels)
    frame = frame.astype(np.uint8)
    keypoints = detector.detect(frame)
    ret, frame_cam = cap.read()
    if frame is None:
        break
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow(window_capture_name, frame)
    cv2.imshow(window_capture_name,frame_with_keypoints)
    cv2.imshow("Keypoints", frame_threshold)

    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
        break



def recognize(img):
    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,0,0) ~ (70, 255,255)
    mask_green = cv2.inRange(hsv, (36, 0, 0), (70, 255, 255))
    ## mask o yellow (15,0,0) ~ (36, 255, 255)
    #mask_yellow = cv2.inRange(hsv, (15, 0, 0), (36, 255, 255))
    ## mask o red rgb(252,193,154) ~ rgb(224,65,17)
    mask_tomato = cv2.inRange(hsv,  (14,86,47),(24, 94, 80))
    ## final mask and masked
    mask = cv2.bitwise_or(mask_tomato, mask_green)
    #mask = cv2.bitwise_or(mask, mask_tomato)
    target = cv2.bitwise_and(img, img, mask=mask)
    show_image(mask_tomato)
    cv2.imwrite("target.png", target)

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    image = cv2.imread(".//res//ingredients.png")
    #show_image(image)

#    recognize(image)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
