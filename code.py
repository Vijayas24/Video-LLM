
#installations
!pip install ultralytics
!pip install deep_sort_realtime
!pip install opencv-python


import cv2
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort
from ultralytics import YOLO
from google.colab.patches import cv2_imshow  


yolo_model = YOLO('yolov8n.pt')  


tracker = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0, max_cosine_distance=0.7)

def process_video(video_path):
   
    cap = cv2.VideoCapture(video_path)

    
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    
    out = cv2.VideoWriter('output_with_tracking.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        
        results = yolo_model(frame)

        
        detections = []
        for result in results:  
            boxes = result.boxes  
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  
                conf = box.conf.cpu().numpy()  
                cls = box.cls.cpu().numpy()    

                if cls == 0:  
                    detections.append([x1, y1, x2 - x1, y2 - y1, conf])

        
        tracks = tracker.update_tracks(detections, frame=frame)

        
        for track in tracks:
            if track.is_confirmed():
                x1, y1, x2, y2 = track.to_tlbr()  
                track_id = track.track_id

                
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"ID: {track_id}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        
        out.write(frame)

        
        cv2_imshow(frame)  

        

    
    cap.release()
    out.release()


video_path = '/content/5330440-uhd_3840_2160_25fps.mp4' 
process_video(video_path)


from google.colab import files
files.download('output_with_tracking.mp4')
