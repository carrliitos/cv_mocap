import cv2 as cv

class MultiCameraCapture:
  def __init__(self, sources: dict) -> None:
    assert sources
    print(sources)

    self.captures = {}
    for camera_name, camera_link in sources.items():
      cap = cv.VideoCapture(camera_link)
      cap.set(cv.CAP_PROP_BUFFERSIZE, 1)
      
      print(camera_name)
      assert cap.isOpened()
      
      self.captures[camera_name] = cap

  @staticmethod
  def read_frame(capture):
    if not capture.grab():
      print("[WARN] grab() failed.")
      return None

    ret, frame = capture.retrieve()
    if not ret or frame is None:
      print("[WARN] retrieve() failed or empty frame.")
      return None

    return frame
