#!/usr/bin/python3

import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	print("speak")
	audio=r.listen(source,timeout=1,phrase_time_limit=5)

try:
     print("You said   " + r.recognize_google(audio))
except sr.UnknownValueError:
     print("could not understand audio")
except sr.RequestError as e:
     print("cpuld not request results;{0}".format(e))
