import cv2
cap = cv2.VideoCapture("exp7.mp4")
if not cap.isOpened():
    print("Error: Cannot open input.mp4")
    exit()
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()
print("Frames read:", len(frames))
if len(frames) == 0:
    print("No frames found. Check your video file.")
    exit()
height, width = frames[0].shape[:2]
fps = 30
out = cv2.VideoWriter(
    "reverse_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)
for frame in reversed(frames):
    out.write(frame)
out.release()
print("Reverse video saved successfully.")
