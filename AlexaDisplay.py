import speech_recognition as sr
import re
import os
from gtts import gTTS 
r = sr.Recognizer()
mytext = 'Ok Playing Happy Birthday Song!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3")
with sr.Microphone() as source:
     print ("Say Something");
     audio = r.listen(source)
     print ("Time Over")

try:
    print ("TEXT:"+r.recognize_google(audio,language ='US-EN'));
    voiceCmd=r.recognize_google(audio,language ='US-EN');
    print("voiceCmd is",voiceCmd);
    if ( re.match("wish happy birthday",voiceCmd)):
        os.system("play welcome.mp3") 
        os.system("play happy.mp3")
    elif (re.match("shut",voiceCmd)):
        os.system("reboot now")

    else:
        print("Command not understood");

except:
    pass;
