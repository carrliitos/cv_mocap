import cv2

def main():
  cap = cv2.VideoCapture(4)
  cap.set(3, 640)
  cap.set(4, 480)

  back_sub = cv2.createBackgroundSubtractorMOG2()

  while True:
    ret, img = cap.read()
    if not ret:
      break

    fg_mask = back_sub.apply(img)
    _, thresh = cv2.threshold(fg_mask, 180, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

    # cv2.drawContours(img, filtered, -1, (0, 255, 0), 2)

    frame_out = img.copy()
    for cnt in filtered:
      x, y, w, h = cv2.boundingRect(cnt)
      cv2.rectangle(frame_out, (x, y), (x + w, y + h), (0, 0, 200),3)

    cv2.imshow("Bounding rectangles", frame_out)
    # cv2.imshow("Webcam with Contours", img)
    # cv2.imshow("Foreground Mask", fg_mask)

    if cv2.waitKey(1) == ord("q"):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
