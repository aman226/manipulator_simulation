
import cv2
import numpy as np
import math
import serial as ps

serialMon = ps.Serial('COM7', 9600)
path = set()

def nothing(x):
    pass


cv2.namedWindow('botARM')
cv2.createTrackbar('Length', 'botARM', 0, 120, nothing)
cv2.createTrackbar('Color', 'botARM', 0, 19, nothing)

colHex = [(133,   3,   5),
          (239,  31,  31),
          (255,  76, 132),
          (  0, 104, 135),
          (  0,  35,  62),
          (192, 192, 192),
          (128, 128, 128),
          (128,   0,   0),
          (128, 128,   0),
          (  0, 255,   0),
          (  0, 255, 255),
          (  0, 128, 128),
          (  0,   0, 128),
          (255,   0, 255),
          (128,   0, 128),
          (205,  92,  92),
          (240, 128, 128),
          (250, 128, 114),
          (233, 150, 122),
          (255, 160, 122)]

botArm = np.zeros((500, 500, 3), np.uint8)
botArm = cv2.bitwise_not(botArm)
#######################################################################################################################
length = 60
data = 1
num = 1
pos = 1
x = 1
y = 1
angle1 = 0
angle2 = 0
theta = 0
phi = 0
#######################################################################################################################
while True:
    length = cv2.getTrackbarPos('Length', 'botARM')
    if (serialMon.inWaiting() > 0):
        data = serialMon.readline()
        data = (data.decode('UTF-8'))
        num = int(data[0])
        pos = int(data[1:])
        print(pos)

    botArm_copy = botArm.copy()
    if num == 1:
        x = pos
    elif num == 0:
        y = pos
    j = cv2.getTrackbarPos('Color', 'botARM')
    COLOR = colHex[j]
    cv2.circle(botArm_copy, (250, 250), 2 * length, (200, 130, 150), -9)
    cv2.circle(botArm_copy, (7, 7), 7 , COLOR , -3)
    path2 = list(path)
    print(path)

    for i in range(len(path2)):
        cv2.circle(botArm_copy, (path2[i][0], path2[i][1]), 3, path2[i][2], -3)

    if (x ** 2 + y ** 2 - ((2 * length) ** 2)) <= 0 < y and y:
        angle2 = math.acos(float(x ** 2 + y ** 2) / (2 * (length ** 2)) - 1)
        angle1 = math.atan(float(x) / y) - math.atan(math.sin(angle2) / (1 + math.cos(angle2)))
        theta = angle1
        phi = angle1 + angle2
        cv2.circle(botArm_copy, (250, 250), 7, (0, 0, 255), -9)
        cv2.circle(botArm_copy, (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))), 7,
                   (0, 0, 255), -9)
        cv2.circle(botArm_copy, (250 + int(length * math.cos(theta)) + int(length * math.cos(phi)),
                                 250 - int(length * math.sin(theta) + int(length * math.sin(phi)))), 7, (0, 0, 255), -9)
        cv2.line(botArm_copy, (250, 250), (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))),
                 (150, 150, 0), 5)
        cv2.line(botArm_copy, (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))), (
            250 + int(length * math.cos(theta)) + int(length * math.cos(phi)),
            250 - int(length * math.sin(theta) + int(length * math.sin(phi)))), (200, 0, 255), 5)
        path.add((y + 250, 250 - x, COLOR))

    elif (x ** 2 + y ** 2 - ((2 * length) ** 2)) <= 0 and y < 0 and y:
        t = -x
        angle2 = math.acos(float(t ** 2 + y ** 2) / (2 * (length ** 2)) - 1)
        angle1 = np.pi - math.atan(float(t) / y) - math.atan(math.sin(angle2) / (1 + math.cos(angle2)))
        theta = angle1
        phi = angle1 + angle2

        cv2.circle(botArm_copy, (250, 250), 7, (0, 0, 255), -9)
        cv2.circle(botArm_copy, (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))), 7,
                   (0, 0, 255), -9)
        cv2.circle(botArm_copy, (250 + int(length * math.cos(theta)) + int(length * math.cos(phi)),
                                 250 - int(length * math.sin(theta) + int(length * math.sin(phi)))), 7, (0, 0, 255), -9)
        cv2.line(botArm_copy, (250, 250), (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))),
                 (150, 150, 0), 5)
        cv2.line(botArm_copy, (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))), (
            250 + int(length * math.cos(theta)) + int(length * math.cos(phi)),
            250 - int(length * math.sin(theta) + int(length * math.sin(phi)))), (200, 0, 255), 5)
        path.add((y + 250, 250 - x, COLOR))
    else:
        cv2.circle(botArm_copy, (250, 250), 7, (0, 0, 255), -9)
        cv2.circle(botArm_copy, (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))), 7,
                   (0, 0, 255), -9)
        cv2.circle(botArm_copy, (250 + int(length * math.cos(theta)) + int(length * math.cos(phi)),
                                 250 - int(length * math.sin(theta) + int(length * math.sin(phi)))), 7, (0, 0, 255), -9)
        cv2.line(botArm_copy, (250, 250), (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))),
                 (150, 150, 0), 5)
        cv2.line(botArm_copy, (250 + int(length * math.cos(theta)), 250 - int(length * math.sin(theta))), (
            250 + int(length * math.cos(theta)) + int(length * math.cos(phi)),
            250 - int(length * math.sin(theta) + int(length * math.sin(phi)))), (200, 0, 255), 5)

    cv2.imshow('botARM', botArm_copy)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        path = set()

cv2.destroyAllWindows()
#######################################################################################################################
