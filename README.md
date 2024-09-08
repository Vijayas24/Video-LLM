<<<<<<< HEAD
<h1>YOLOv8 Person Detection and Tracking using DeepSORT</h1>
=======
<h1>YOLOv8 Person Detection and Tracking using DeepSORT</h1>
<p>This project implements person detection and tracking in videos using YOLOv8 for object detection and DeepSORT for tracking. The code processes a video file, detects people in each frame, and assigns unique IDs to each detected person, tracking their movement throughout the video.</p>
<h3>Table of Contents</h3>
<ul>
  <li>
    Installation
  </li>
  <li>How to run the code</li>
  <li>Code explanation</li>
  <li>Output</li>
  <li>Requirements</li>
  <li>Credits</li>
</ul>
<h3>Installation</h3>
<ul>
  <li>Clone this repository or download the script to your local machine.</li>
  <li>Install the necessary dependencies:</li>
  <p>!pip install ultralytics<br>
!pip install deep_sort_realtime<br>
!pip install opencv-python<br>
                            
</p>
</ul>
<h3>How to run the code</h3>
<ul>
  <li>Upload the video to Colab or your working environment. Modify the video_path variable in the script to point to your video file.</li>
  <li>Run the process_video() function with the correct path to process the video:</li>
  <p>video_path = '/content/01.mp4'  # Path to your input video<br>
process_video(video_path)</p>
  <li>Output Video: The output video with detected persons and tracking IDs will be saved as output_with_tracking.mp4.</li>
  <li>Download the Output: After processing, you can download the output video using:</li>
  <p>from google.colab import files<br>
files.download('output_with_tracking.mp4')</p>
</ul>
<h3>Code Explanation</h3>
<h4>1.Yolov8 Model:</h4>
<ul><li>The script uses the YOLOv8 model from the ultralytics library, pre-trained on the COCO dataset. The model detects persons in each video frame.</li>
<li>You can choose a different YOLO model by changing the file (e.g., yolov8n.pt for YOLOv8 Nano, yolov8s.pt for Small).</li>
<p>yolo_model = YOLO('yolov8n.pt')
</p>
<h4>DeepSORT Tracker</h4>
<li>DeepSORT (Simple Online and Realtime Tracking with a Deep Association Metric) is used for tracking detected persons across frames.</li>
<li>It assigns a unique ID to each person and tracks their movement using their bounding boxes and appearance features.</li>
<p>tracker = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0, max_cosine_distance=0.7)
</p>
<h4>Video Processing</h4>
<li>The video is processed frame by frame. YOLO detects persons in each frame, and the DeepSORT tracker assigns unique IDs to track the persons across the frames.</li>
<li>Bounding boxes are drawn around detected persons, and the person’s unique ID is displayed.</li>
<p>results = yolo_model(frame)<br>
tracks = tracker.update_tracks(detections, frame=frame)
</p>
<h4>Output Video</h4>
  <li>The processed video with bounding boxes and IDs is written to an output file using cv2.VideoWriter.</li>
  <p>out = cv2.VideoWriter('output_with_tracking.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))</p>
  <h4>Displaying Frames (Optional in Colab):</h4>
  <li>The frame with bounding boxes can be displayed during processing using cv2_imshow(), which is specific to Google Colab.</li>
  <p>cv2_imshow(frame)</p>
  
</ul>
<h3>Output</h3>
<ul>
  <li>The output video will have bounding boxes drawn around detected persons with unique tracking IDs displayed above the boxes. The file will be saved as output_with_tracking.mp4.</li>
  
</ul>
<h3>Requirements</h3>
<ul>
  <li>Python 3.x</li>
  <li>YOLOv8 model (pre-trained on COCO)</li>
  <li>DeepSORT for tracking</li>
  <li>OpenCV for video processing</li>
  <p>Install these libraries using the following commands:<br>
  !pip install ultralytics<br>
!pip install deep_sort_realtime<br>
!pip install opencv-python<br>
</p>
</ul>
<h3>Acclaim</h3>
<ul>
  <li>YOLOv8: Provided by the ultralytics library.</li>
  <li>DeepSORT: Simple Online and Realtime Tracking algorithm using a deep association metric.</li>
  <li>OpenCV: Open Source Computer Vision Library used for video and image processing.</li>
</ul>
>>>>>>> bb3bfbb78908d701375b0de93b94824012f6c359
