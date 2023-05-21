import os

#os.system("say -r 720 [[volm 5]] bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song bling blong ding dong ping pong bing bong king kong sing song")

def speak(text, rate=200, volm=1):
    text = text.replace("'","\\'")
    text = text.replace('"', '\\"')
    command = "say -r " + str(rate) + " [[volm " + str(volm) + "]] " + text
    os.system(command)
    


speak("", 1, 0.9)


