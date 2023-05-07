#PROJECT NAME--- "WORD PUZZLE GAME"
import random 

def shuffleWord(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)

def printPuzzleQusetion(word,score):
    problemWord=shuffleWord(word)
    print("\nArrange the Letter to form a valid word")
    print(problemWord)
    userWord=input()
    print()
    if(userWord.upper()==word):
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1
    return score

def main():
    score=0
    words=["FATHER","BREAK","COUNTRY","INDIA"]
    words=random.sample(words,k=len(words))
    print(words)

    for word in words:
        score=printPuzzleQusetion(word,score)


    print("Your Score Is",score)
    print()

print("Game End",main())
