def shout(*words, sep=" ", end="!", times=1):
    text = sep.join(str(w) for w in words)
    for _ in range(times):
        print(text.upper() + end)

shout("hello", "class")                 
shout("python", "is", "fun", sep="-")    
shout("namaste", end="!!!")              
shout(5, 10)                             
shout("go", times=3)                     

words = ["we", "love", "momo"]
shout(*words)                           