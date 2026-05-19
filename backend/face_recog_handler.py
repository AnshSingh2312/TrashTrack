# backend/face_recog_handler.py

import os
import face_recognition

KNOWN_USERS_DIR = os.path.join(os.path.dirname(__file__), 'users')
known_encodings = []
known_names = []

# Load known faces
for filename in os.listdir(KNOWN_USERS_DIR):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        try:
            image = face_recognition.load_image_file(os.path.join(KNOWN_USERS_DIR, filename))
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
        except Exception as e:
            print(f"Error processing {filename}: {e}")

def identify_face(image_path):
    """
    Identifies a face in the given image against known users.
    """
    try:
        unknown_image = face_recognition.load_image_file(image_path)
        unknown_encodings = face_recognition.face_encodings(unknown_image)
        for unknown_encoding in unknown_encodings:
            results = face_recognition.compare_faces(known_encodings, unknown_encoding)
            for i, match in enumerate(results):
                if match:
                    return known_names[i]
    except Exception as e:
        print(f"Error identifying face: {e}")
    return None
