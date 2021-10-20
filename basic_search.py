import wikipedia

search = input("search: ")

wikiPageSummary = wikipedia.summary(search)

print(search)
print(wikiPageSummary)