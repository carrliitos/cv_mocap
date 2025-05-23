import cv2 as cv
from async_frame_reader import video_async

def main():
  cap = cv.VideoCapture(4)
  assert cap.isOpened()
  print(f"Captured object: {cap}")

  while True:
    frame = video_async.read_frame(cap)
    cv.imshow("Logi 720p Camera", frame)

    if cv.waitKey(1) == ord("q"):
      break

if __name__ == '__main__':
  main()
