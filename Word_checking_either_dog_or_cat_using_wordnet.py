from nltk.corpus import wordnet


def go(inp) :
    for i in range(len(inp)) :
        if inp[i].name().split('.')[0] == "cat" :
          return 1
        if inp[i].name().split('.')[0] == "dog" :
          return 2
        go(inp[i].hypernyms())
    return 0


inp = input()
syns = wordnet.synsets(inp)


if len(syns) > 0 and go(syns[0].hypernyms()) == 1 :
    print("Cat")
elif len(syns) > 0 and go(syns[0].hypernyms()) == 2 :
    print("Dog")
else :
    print("Neither Cat Nor Dog")
