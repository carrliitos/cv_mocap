import cv2 as cv
import datetime
import json
from async_frame_reader.video_async import MultiCameraCapture

def main():
  with open("./cameras.json") as json_file:
    cameras = json.load(json_file)
  captured = MultiCameraCapture(sources=cameras)

  while True:
    for camera_name, cap in captured.captures.items():
      frame = captured.read_frame(cap)
      if frame is None:
        continue
    
      font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
      dt = str(datetime.datetime.now())
      frame = cv.putText(frame, dt, 
                         (10, 100), 
                         font, 1, 
                         (210, 155, 155), 
                         4, cv.LINE_8)

      cv.imshow(camera_name, frame)

      if cv.waitKey(1) == ord("q"):
        break

if __name__ == '__main__':
  main()
