from norfair.drawing import Paths
from norfair import Detection, Tracker, draw_tracked_boxes, Paths, draw_boxes


def centroid_distance(detection, tracked_object):
    return np.linalg.norm(detection.points - tracked_object.estimate)

def get_norfair_detections(detections):
    face_norfair_detections = []

    for bbox in detections:
        bbox = np.array(bbox).reshape(2, 2)
        face_norfair_detections.append(Detection(points=bbox))

    return face_norfair_detections



  norfair_detections = get_norfair_detections(face_detections)
  tracked_objects = tracker.update(detections=norfair_detections)





