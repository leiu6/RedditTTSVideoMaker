import pyttsx3


def talk_to_file(script, path):
    engine = pyttsx3.init()
    engine.save_to_file(script, path)
    engine.runAndWait()
