import cv2
import numpy as np
from keras.models import model_from_json
import time
import pyttsx3
import speech_recognition as sr

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "neutral", 5: "Sad", 6: "Surprised"}

# load json and create model
json_file = open('model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("model/emotion_model.h5")
print("Loaded model from disk")

# start the webcam feed
address = "http://192.168.1.40:8080/video"
cap = cv2.VideoCapture(address)

# pass here your video path
# you may download one from here : https://www.pexels.com/video/three-girls-laughing-5273028/
# cap = cv2.VideoCapture("C:\\JustDoIt\\ML\\Sample_videos\\emotion_sample6.mp4")

start_time = time.time()
emotion_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    if not ret:
        break
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces available on camera
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # take each face available on the camera and Preprocess it
    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

        # predict the emotions
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        emotion_count[maxindex] += 1
        cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time > 5:
        break

cap.release()
cv2.destroyAllWindows()

# calculate the average emotion and dominant emotion
total_emotions = sum(emotion_count.values())
average_emotion = {key: value / total_emotions for key, value in emotion_count.items()}
dominant_emotion = emotion_dict[max(emotion_count, key=emotion_count.get)]
print(f"Average emotion: {average_emotion}")
print(f"Dominant emotion: {dominant_emotion}")


# use text-to-speech to speak out the dominant emotion
engine = pyttsx3.init()
engine.say(f"You are feeling {dominant_emotion}")
engine.runAndWait()

# use speech recognition to get user response
r = sr.Recognizer()
with sr.Microphone() as source:
    print(f"Are you feeling {dominant_emotion}?")
    engine.say(f"Are you feeling {dominant_emotion}?")
    engine.runAndWait()
    audio = r.listen(source)

try:
    user_response = r.recognize_google(audio)
    print(f"You said: {user_response}")
    if user_response.lower() == "yes":
        chosen_emotion = dominant_emotion
    else:
        # find the second largest emotion count
        sorted_emotions = sorted(emotion_count.items(), key=lambda x: x[1], reverse=True)
        second_largest_emotion = emotion_dict[sorted_emotions[1][0]]

        # use text-to-speech to speak out the second largest emotion
        engine.say(f"You are feeling {second_largest_emotion}")
        engine.runAndWait()

        with sr.Microphone() as source:
            print(f"Are you feeling {second_largest_emotion}?")
            engine.say(f"Are you feeling {second_largest_emotion}?")
            engine.runAndWait()
            audio = r.listen(source)

        user_response = r.recognize_google(audio)
        print(f"You said: {user_response}")
        if user_response.lower() == "yes":
            chosen_emotion = second_largest_emotion
        else:
            print("Sorry, I didn't understand your response.")
            chosen_emotion = None

except sr.UnknownValueError:
    print("Sorry, I didn't understand your response.")
    chosen_emotion = None

# use the chosen emotion in your other Python program
if chosen_emotion is not None:
    print(f"Emotion you are feeling: {chosen_emotion}")
    with open('chosen_emotion.txt', 'w') as f:
        f.write(chosen_emotion)

