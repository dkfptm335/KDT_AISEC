import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract as pyt
import imutils
import sys

# 마우스 클릭 이벤트 콜백 함수
def mouse_callback(event, x, y, flags, param):
        
    # 마우스 왼쪽 버튼을 클릭할 때
    if event == cv.EVENT_LBUTTONDOWN:
        if len(coords) == 0:
            print(f"좌상단: ({x}, {y})")
            coords.append((x, y))
            
        elif len(coords) == 1:
            print(f"우상단: ({x}, {y})")
            coords.append((x, y))
                
        elif len(coords) == 2:
            print(f"좌하단: ({x}, {y})")
            coords.append((x, y))
                
        elif len(coords) == 3:
            print(f"우하단: ({x}, {y})")
            coords.append((x, y))
            
        # 좌표가 4개가 되면
        if len(coords) == 4:
            # 종료
            cv.destroyAllWindows()

if __name__ == "__main__":

    pyt.pytesseract.tesseract_cmd = r'C:\Tools\Tesseract-OCR\tesseract.exe'
    
    # 현재 디렉토리
    current_dir = os.getcwd()

    if len(sys.argv) < 2:
        print("Usage: python OCR.py <img_name>")
        sys.exit(1)
    
    img_name = sys.argv[1]
    img_path = os.path.join(current_dir, img_name)

    # 이미지 읽기
    img = cv.imread(img_path)

    # 이미지의 세로 길이가 1000 되도록 이미지 크기 조절
    img_resized = imutils.resize(img, height=1000)
    
    # 좌표 저장할 리스트
    coords = []

    # 윈도우 생성 및 이미지 표시
    cv.namedWindow("Click on the top left, top right, bottom left, and bottom right.")
    cv.imshow("Click on the top left, top right, bottom left, and bottom right.", img_resized)

    # 마우스 이벤트 콜백 함수 등록
    cv.setMouseCallback("Click on the top left, top right, bottom left, and bottom right.", mouse_callback)
    
    # 키 입력 대기
    cv.waitKey(0)
    # 윈도우 종료
    cv.destroyAllWindows()
    
    # 이미지 투시 변환
    pts1 = np.float32([coords[0], coords[1], coords[2], coords[3]])
    # 해당 좌표로 투시변환 가로 세로 90:50 비율로
    pts2 = np.float32([[0, 0], [900, 0], [0, 500], [900, 500]])
    m = cv.getPerspectiveTransform(pts1, pts2)
    card_image = cv.warpPerspective(img_resized, m, (900, 500))

    # to gray scale
    gray = cv.cvtColor(card_image, cv.COLOR_BGR2GRAY)
    # apply gaussian blur
    blurred = cv.GaussianBlur(gray, (3, 3), 0)
    # adaptive thresholding
    thresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 5)
    # erode
    kernel = np.ones((1, 3), np.uint8)
    erode = cv.erode(thresh, kernel, iterations=1)

    # OCR 수행
    options = "-l kor+eng --oem 3 --psm 6"
    text = pyt.image_to_string(erode, config=options)
    # output
    print(text)
