# Design a Python Program for Creating Random Story Generator.

import random

sentence_starter=['About 100 Years ago','In the 20 BC','Once upon a time']

character=[' there lived a king,',' there was a man named jack,',' there lived a farmer,']

time=[' One Day',' One full Moon night']

story_plot=[' he was passing by',' he was going for a picnic to']

place=[' the Mountains',' the Garden']

Second_character=[' he saw a man',' he saw a lady']

age=[' who seemed to be in late 20s',' Who seem very old and feeble']

Work=[' searcing somthing.',' digging a well on roadside.']

print(random.choice(sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(Second_character)+
      random.choice(age)+random.choice(Work))
