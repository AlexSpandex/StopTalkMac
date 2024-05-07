import speech_recognition as sr

def listen_from_microphone(device_index):
    # Initialize the recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=device_index)

    with microphone as source:
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        # Continuously listen and perform speech recognition
        while True:
            try:
                # Capture audio from the microphone
                audio = recognizer.listen(source)
                
                # Recognize speech using Google's speech recognition
                text = recognizer.recognize_google(audio)
                print("You said:", text)
            except sr.UnknownValueError:
                # Speech was unintelligible
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                # Could not request results; check your network connection
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                # Other errors
                print(f"An error occurred: {e}")

# Use the correct index for your USB microphone or sound card
listen_from_microphone(device_index=2)
