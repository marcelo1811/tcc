import cv2
import numpy as np

def main():
  def takePicture():
    # Trocar o número dentro do parentesis até encontrar a câmera
    cam = cv2.VideoCapture(0)

    camOn = True
    count = 0
    while camOn:
      ret, img = cam.read()

      if not ret: 
        break

      if count == 2:
        imgName = "images/screenshot.png"
        print(img.shape)
        # Recortando a imagem para obter apenas o tabuleiro
        # 1º valor um range de pixels da altura considerando 0 como o topo da imagem
        # 2º valor um range de pixels da largura considerando 0 como o lado esquerdo a imagem
        img = img[55:380, 230:560]
        cv2.imwrite(imgName, img)
        camOn = False
      
      count = count + 1

  def placeGrid(x, y, size, shape, matrix):
    w = size[0] / 3
    h = size[1] / 3
    if (x <= w):
      col = 1
    elif (x <= 2*w):
      col = 2
    else:
      col = 3

    if (y <= h):
      row = 1
    elif (y <= 2*h):
      row = 2
    else:
      row = 3

    matrix[row - 1][col - 1] = shape
    return matrix

  def createPattern(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([0,79,120])
    upper = np.array([179,255,255])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    imgCanny = cv2.Canny(imgResult, 100, 500)

    return imgCanny

  def createPatternItem(path):
    img = cv2.imread(path)
    img = cv2.resize(cv2.imread(path), (500, 500))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, 100, 500)

    return imgCanny

  def getContours(img, patternX, patternO):
    matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cntX, _ = cv2.findContours(patternX, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cntO, _ = cv2.findContours(patternO, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
      area = cv2.contourArea(cnt)
      # print(area)
      if area < 20000 and area > 10:
        cv2.drawContours(imgContour, cnt, -1, (0, 0, 255), 3)
        peri = cv2.arcLength(cnt, False)
        approx = cv2.approxPolyDP(cnt, 0.01 * peri, False)
        # print(approx[0])
        
        resX = cv2.matchShapes(cntX[0], cnt, 3, 0.0)
        # print('x = ' + str(resX))
        resO = cv2.matchShapes(cntO[0], cnt, 3, 0.0)
        # print('o = ' + str(resO))

        x, y, w, h = cv2.boundingRect(approx)
        
        if resX >= 0 and resX <= 0.3 and resX > resO:
          shape = 'O'
          # print(shape)
          matrix = placeGrid(x + w, y + h, img.shape, shape, matrix)
          cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
          cv2.putText(
            imgContour, 
            shape, 
            (x + (w // 2) - 10, y - 10), 
            cv2.FONT_HERSHEY_COMPLEX, 
            1, 
            (0, 155, 0), 
            2
          )
        elif resO >= 0 and resO <= 0.3 and resO > resX:
          shape = 'X'
          # print(shape)
          matrix = placeGrid(x + w, y + h, img.shape, shape, matrix)
          cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
          cv2.putText(
            imgContour, 
            shape, 
            (x + (w // 2) - 10, y - 10), 
            cv2.FONT_HERSHEY_COMPLEX, 
            1, 
            (0, 155, 0), 
            2
          )

    # print(matrix)
    return matrix

  def getMask():
    def empty(a):
      pass

    path = 'teste2.jpg'
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,240)
    cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
    cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
    cv2.createTrackbar("Sat Min","TrackBars",8,255,empty)
    cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
    cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
    cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

    while True:
      img = cv2.imread(path)
      imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
      h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
      h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
      s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
      s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
      v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
      v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
      print(h_min,h_max,s_min,s_max,v_min,v_max)
      lower = np.array([h_min,s_min,v_min])
      upper = np.array([h_max,s_max,v_max])
      mask = cv2.inRange(imgHSV,lower,upper)
      imgResult = cv2.bitwise_and(img,img,mask=mask)

      cv2.imshow("Original",img)
      cv2.imshow("HSV",imgHSV)
      cv2.imshow("Mask", mask)
      cv2.imshow("Result", imgResult)

      cv2.waitKey(1)
    
  # getMask()

  # Descomentar para tirar a foto com câmera
  takePicture()
  Xpath = 'images/ex.jpg'
  Opath = 'images/circle.png'
  # Trocar path para 'images/screenshot.png' para analisar foto da câmera
  path = 'images/screenshot.png'
  imgContour = cv2.imread(path)
  # imgContour = imgContour[55:380, 230:560]
  imgCanny = createPattern(imgContour)
  # imgContour = cv2.resize(cv2.imread(path), (500, 500))
  cv2.imshow('Original', imgContour)
  cv2.imshow('Canny', imgCanny)

  patternX = createPatternItem(Xpath)
  patternO = createPatternItem(Opath)

  matrix = getContours(imgCanny, patternX, patternO)

  cv2.imshow('Contour', imgContour)

  cv2.waitKey(0)
  return matrix

if __name__ == "__main__":
  main()