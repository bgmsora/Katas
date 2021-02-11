def top_3_words(text):
    quitar=['//','/',';',':','_','-','!','?',',','..','...',".","'''"," ' "]
    text=text.lower()
    for x in quitar:
        text=text.replace(x,' ')
    words=text.split()
    a=sorted([(w, words.count(w)) for w in set(words)], key = lambda x:x[1], reverse=True)[:3]
    regreso=[]
    for x in a:
        regreso.append(x[0])
    return regreso