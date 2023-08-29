import cv2
video_path = "C://Users//STAR//Videos//v1.mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video file")
    exit()
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(f"Frame count: {frame_count}")
print(f"Frame dimensions: {frame_width}x{frame_height}")
print(f"Frames per second: {fps}")
for frame_number in range(frame_count):
    ret, frame = cap.read()
    if not ret:
        print(f"Error reading frame {frame_number}")
        break
    frame_filename = f"frame_{frame_number:04d}.jpg"
    cv2.imwrite(frame_filename, frame)
    print(f"Saved frame {frame_filename}")
cap.release()
cv2.destroyAllWindows()