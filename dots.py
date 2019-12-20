import numpy as np
import cv2
import imutils
import dlib
from imutils import face_utils

predictor_model = "shape_predictor_68_face_landmarks.dat"
face_predictor = dlib.shape_predictor(predictor_model)
face_detector = dlib.get_frontal_face_detector()

def angry(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector(gray, 1)
    for c in detected_faces:
        shape = face_predictor(gray, c)
        shape = face_utils.shape_to_np(shape)
        dotlef = shape[17]
        dot1x = dotlef[0]
        dot1y = dotlef[1]
        dotrig = shape[18]
        dot2x = dotrig[0]
        dot2y = dotrig[1]
        dotup = shape[19]
        dotupx = dotup[0]
        dotupy = dotup[1]
        dotdo = shape[20]
        dotdox = dotdo[0]
        dotdoy = dotdo[1]
        dotlef1 = shape[21]
        dot1x1 = dotlef1[0]
        dot1y1 = dotlef1[1]
        dotrig1 = shape[22]
        dot2x1 = dotrig1[0]
        dot2y1 = dotrig1[1]
        dotup1 = shape[23]
        dotupx1 = dotup1[0]
        dotupy1 = dotup1[1]
        dotdo1 = shape[24]
        dotdox1 = dotdo1[0]
        dotdoy1 = dotdo1[1]
        dotlef2 = shape[25]
        dot1x2 = dotlef2[0]
        dot1y2 = dotlef2[1]
        dotrig2 = shape[26]
        dot2x2 = dotrig2[0]
        dot2y2 = dotrig2[1]
        dotlefe = shape[48]
        dot1xe = dotlefe[0]
        dot1ye = dotlefe[1]
        dotrige = shape[54]
        dot2xe = dotrige[0]
        dot2ye = dotrige[1]
        dotupe = shape[51]
        dotupxe = dotupe[0]
        dotupye = dotupe[1]
        dotdoe = shape[57]
        dotdoxe = dotdoe[0]
        dotdoye = dotdoe[1]
        cv2.circle(img, (dot1xe, dot1ye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2xe, dot2ye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotupxe, dotupye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotdoxe, dotdoye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot1x, dot1y), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2x, dot2y), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotupx, dotupy), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotdox, dotdoy), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot1x1, dot1y1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2x1, dot2y1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotupx1, dotupy1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotdox1, dotdoy1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot1x2, dot1y2), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2x2, dot2y2), 3, (0, 30, 175), -1)


def surprise(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector(gray, 1)
    for c in detected_faces:
        shape = face_predictor(gray, c)
        shape = face_utils.shape_to_np(shape)
        dotlefey = shape[36]
        dotlefeyx = dotlefey[0]
        dotlefeyy = dotlefey[1]
        dotlefey1 = shape[37]
        dotlefeyx1 = dotlefey1[0]
        dotlefeyy1 = dotlefey1[1]
        dotlefey2 = shape[38]
        dotlefeyx2 = dotlefey2[0]
        dotlefeyy2 = dotlefey2[1]
        dotlefey3 = shape[39]
        dotlefeyx3 = dotlefey3[0]
        dotlefeyy3 = dotlefey3[1]
        dotlefey4 = shape[40]
        dotlefeyx4 = dotlefey4[0]
        dotlefeyy4 = dotlefey4[1]
        dotlefey5 = shape[41]
        dotlefeyx5 = dotlefey5[0]
        dotlefeyy5 = dotlefey5[1]
        dotrigey = shape[42]
        dotrigeyx = dotrigey[0]
        dotrigeyy = dotrigey[1]
        dotrigey1 = shape[43]
        dotrigeyx1 = dotrigey1[0]
        dotrigeyy1 = dotrigey1[1]
        dotrigey2 = shape[44]
        dotrigeyx2 = dotrigey2[0]
        dotrigeyy2 = dotrigey2[1]
        dotrigey3 = shape[45]
        dotrigeyx3 = dotrigey3[0]
        dotrigeyy3 = dotrigey3[1]
        dotrigey4 = shape[46]
        dotrigeyx4 = dotrigey4[0]
        dotrigeyy4 = dotrigey4[1]
        dotrigey5 = shape[47]
        dotrigeyx5 = dotrigey5[0]
        dotrigeyy5 = dotrigey5[1]
        dotlef = shape[17]
        dot1x = dotlef[0]
        dot1y = dotlef[1]
        dotrig = shape[18]
        dot2x = dotrig[0]
        dot2y = dotrig[1]
        dotup = shape[19]
        dotupx = dotup[0]
        dotupy = dotup[1]
        dotdo = shape[20]
        dotdox = dotdo[0]
        dotdoy = dotdo[1]
        dotlef1 = shape[21]
        dot1x1 = dotlef1[0]
        dot1y1 = dotlef1[1]
        dotrig1 = shape[22]
        dot2x1 = dotrig1[0]
        dot2y1 = dotrig1[1]
        dotup1 = shape[23]
        dotupx1 = dotup1[0]
        dotupy1 = dotup1[1]
        dotdo1 = shape[24]
        dotdox1 = dotdo1[0]
        dotdoy1 = dotdo1[1]
        dotlef2 = shape[25]
        dot1x2 = dotlef2[0]
        dot1y2 = dotlef2[1]
        dotrig2 = shape[26]
        dot2x2 = dotrig2[0]
        dot2y2 = dotrig2[1]
        dotlefe = shape[48]
        dot1xe = dotlefe[0]
        dot1ye = dotlefe[1]
        dotrige = shape[54]
        dot2xe = dotrige[0]
        dot2ye = dotrige[1]
        dotupe = shape[51]
        dotupxe = dotupe[0]
        dotupye = dotupe[1]
        dotdoe = shape[57]
        dotdoxe = dotdoe[0]
        dotdoye = dotdoe[1]
        cv2.circle(img, (dotlefeyx, dotlefeyy), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotlefeyx1, dotlefeyy1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotlefeyx2, dotlefeyy2), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotlefeyx3, dotlefeyy3), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotlefeyx4, dotlefeyy4), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotlefeyx5, dotlefeyy5), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotrigeyx, dotrigeyy), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotrigeyx1, dotrigeyy1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotrigeyx2, dotrigeyy2), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotrigeyx3, dotrigeyy3), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotrigeyx4, dotrigeyy4), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotrigeyx5, dotrigeyy5), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2xe, dot2ye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot1xe, dot1ye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2xe, dot2ye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotupxe, dotupye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotdoxe, dotdoye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot1x, dot1y), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2x, dot2y), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotupx, dotupy), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotdox, dotdoy), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot1x1, dot1y1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2x1, dot2y1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotupx1, dotupy1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotdox1, dotdoy1), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot1x2, dot1y2), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2x2, dot2y2), 3, (0, 30, 175), -1)


def happy(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector(gray, 1)
    for c in detected_faces:
        shape = face_predictor(gray, c)
        shape = face_utils.shape_to_np(shape)
        dotlefe = shape[48]
        dot1xe = dotlefe[0]
        dot1ye = dotlefe[1]
        dotrige = shape[54]
        dot2xe = dotrige[0]
        dot2ye = dotrige[1]
        dotupe = shape[51]
        dotupxe = dotupe[0]
        dotupye = dotupe[1]
        dotdoe = shape[57]
        dotdoxe = dotdoe[0]
        dotdoye = dotdoe[1]
        cv2.circle(img, (dot1xe, dot1ye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dot2xe, dot2ye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotupxe, dotupye), 3, (0, 30, 175), -1)
        cv2.circle(img, (dotdoxe, dotdoye), 3, (0, 30, 175), -1)


def dots(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector(gray, 1)
    for c in detected_faces:
        shape = face_predictor(gray, c)
        shape = face_utils.shape_to_np(shape)
        dotlef1 = shape[21]
        dot1x1 = dotlef1[0]
        dot1y1 = dotlef1[1]
        dotlef = shape[17]
        dot1xb = dotlef[0]
        dot1yb = dotlef[1]
        dotrig2 = shape[26]
        dot2x2 = dotrig2[0]
        dot2y2 = dotrig2[1]
        dotrig1 = shape[22]
        dot2x1 = dotrig1[0]
        dot2y1 = dotrig1[1]
        dot1 = shape[48]
        dot1x = dot1[0]
        dot1y = dot1[1]
        dotr = shape[51]
        dotrx = dotr[0]
        dotry = dotr[1]
        dot2 = shape[54]
        dot2x = dot2[0]
        dot2y = dot2[1]
        dotrigey = shape[42]
        dotrigeyx = dotrigey[0]
        dotrigeyy = dotrigey[1]
        dotdoe = shape[57]
        dotdoxe = dotdoe[0]
        dotdoye = dotdoe[1]
        dotlefey3 = shape[39]
        dotlefeyx3 = dotlefey3[0]
        dotlefeyy3 = dotlefey3[1]

        rustym = dotdoye - dotry
        rustxm = dot2x - dot1x
        rustxlef = dot2x1 - dot1xb
        cv2.circle(img, (dotlefeyx3, dotlefeyy3), 3, (0, 255, 0), -1)
        cv2.circle(img, (dotdoxe, dotdoye), 3, (0, 255, 0), -1)
        cv2.circle(img, (dotrigeyx, dotrigeyy), 3, (0, 255, 0), -1)
        cv2.circle(img, (dot2x1, dot2y1), 3, (0, 255, 0), -1)
        cv2.circle(img, (dot1x1, dot1y1), 3, (0, 255, 0), -1)
        cv2.circle(img, (dot2x2, dot2y2), 3, (0, 255, 0), -1)
        cv2.circle(img, (dot1x, dot1y), 3, (0, 255, 0), -1)
        cv2.circle(img, (dot1xb, dot1yb), 3, (0, 255, 0), -1)
        cv2.circle(img, (dot2x, dot2y), 3, (0, 255, 0), -1)
        cv2.circle(img, (dotrx, dotry), 3, (0, 255, 0), -1)
        if rustxm >= rustym * 5:
            cv2.putText(img, 'радость', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
        elif dot2x1 - dot1x1 <= rustxlef / 3.7:
            cv2.putText(img, 'злость', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
        elif dotrigeyy - dot2y1 >= rustxlef / 3.3:
            cv2.putText(img, 'удивление', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
        else:
            cv2.putText(img, 'точки не совпадают', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

