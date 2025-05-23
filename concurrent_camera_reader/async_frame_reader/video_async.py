def read_frame(capture):
  capture.grab()

  ret, frame = capture.retrieve()
  print(frame)

  if not ret:
    print("Empty frame")
    return

  return frame
