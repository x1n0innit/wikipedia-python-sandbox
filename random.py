import wikipedia
import random

randPage = wikipedia.random(pages=1)
print(randPage)
print(wikipedia.summary(randPage, sentences = 3))

pageObj = wikipedia.page(randPage)
linksArray = pageObj.links
lengthArr = len(linksArray)
randInt = random.randint(0, lengthArr - 1)

otherWikiPage = wikipedia.summary(linksArray[randInt], sentences = 3)

print(linksArray[randInt])
print(otherWikiPage)

exit = input("Write 'EXIT' to close the program")
