from pip import main
from PIL import Image
import pyttsx3
import datetime



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good Morning! Hope you are doing well, let us learn numbers")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Hope you doing well, let us learn numbers")

    else:
        speak("Good Evening! Hope you doing well, let us learn numbers") 




if __name__=="__main__":
    wishMe()
    speak("This is one")
    im=Image.open("C:\\animesh\\edrive\\shruti\\ezgif.com-gif-maker.gif")
    im.show()
    im.close()
    speak("This is two")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\2.gif")
    im.show()
    im.close()
    speak("This is three")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\3.gif")
    im.show()
    im.close()
    speak("This is four")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\4.gif")
    im.show()
    im.close()
    speak("This is five")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\5.gif")
    im.show()
    im.close()
    speak("This is six")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\6.gif")
    im.show()
    im.close()
    speak("This is seven")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\7.gif")
    im.show()
    im.close()  
    speak("This is eight")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\8.gif")
    im.show()
    im.close()
    speak("This is nine")
    im=Image.open("C:\\animesh\\edrive\\shruti\\images of 0 to 9\\9.gif")
    im.show()
    im.close()
    speak("This is zero")
    im=Image.open(" C:\\animesh\\edrive\\shruti\\images of 0 to 9\\0.gif")
    im.show()
    im.close()

  

   



  