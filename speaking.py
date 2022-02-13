import pyttsx3

#invoke the factory function to ref the module
engine_object = pyttsx3.init() 

# set rate at which engine speaks
engine_object.setProperty('rate', 150)

# sets the voice
engine_object.setProperty('voice', 'f1')

engine_object.say('Hello World')

# call to the say() function
engine_object.runAndWait()