import cv2
import pafy
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n-pose.pt')

# Open youtube
#video_url = "https://youtu.be/d4kWY_omBp0"
#video = pafy.new(video_url)
#best = video.getbest(preftype="mp4")

# Open Video
video_path = "video1.mov"

#open
#cap = cv2.VideoCapture(best.url) # or video_path
cap = cv2.VideoCapture(video_path) # or video_path

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # view size
        cv2.namedWindow("YOLOv8 Tracking", cv2.WINDOW_NORMAL)
        
        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
