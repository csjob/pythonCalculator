import pyttsx3

class play_audio:
    def __init__(self, voice = 'male', speakstatus = True):
        self.voice = 'male'
        self.speakstatus = speakstatus
        self.speakwords={
            '1' : 'one',
            '2' : 'two',
            '3' : 'three',
            '4' : 'four',
            '5' : 'five',
            '6' : 'six',
            '7' : 'seven',
            '8' : 'eight',
            '9' : 'nine',
            '0' : 'zero',
            '.' : 'point',
            '+' : 'plus',
            '-' : 'minus',
            'x' : 'multiplied by',
            '/' : 'divided by',
            '=' : 'hello job, your calculated value is displayed in the above field',
            'AC' : 'you have cleared the text field',
            '<-' : 'deleted last digit',

            '√' : 'square root is'
        }
        self.engine = pyttsx3.init()
        v = self.engine.getProperty('voices')
        self.engine.setProperty('voice', v[1].id)
        #we can change v[0] to v[1] for female voice.
        #print(v)

    def speak(self,content):
        if self.speakstatus == True:
            self.engine.say(self.speakwords[content])
            self.engine.runAndWait()



if __name__ == '__main__':
    ob = play_audio()
    #ob.speak('content')
