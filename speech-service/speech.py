import speech_recognition as sr


def recognize_speech(file_path):
    """
    Recognize speech from file
    :param file_path: path to the file
    :return: recognized text
    """
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        text = "Could not request results from Google Speech Recognition service; {0}".format(
            e
        )
    return text
