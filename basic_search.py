import wikipedia

search = input("search: ")

wikiPageSummary = wikipedia.summary(search)

print(search)
print(wikiPageSummary)

exit = input("Write 'EXIT' to close the program")
