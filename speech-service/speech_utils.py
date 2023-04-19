import speech_recognition as sr


def recognize_speech(file_path):
    """
    Recognize speech from audio data
    :param file_path: path to the file
    :return: recognized text
    """
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
    try:
        text = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        text = "Sphinx could not understand audio"
    except sr.RequestError as e:
        text = "Sphinx error; {0}".format(e)
    return text
