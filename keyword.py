from gTTS import *
import os
mytext='auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while'
language='en'
myobj=gTTS(text=mytext,lang=language, show=False)
myobj.save("keywords.mp")
