from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pyjokes
import randfacts
import requests
import random
from nltk.corpus import words

ctr=0
exiter=0
PATH = "/Applications/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://web.whatsapp.com/")
time.sleep(20)

search = driver.find_element_by_class_name("_3FRCZ")
search.send_keys("Myself")
search.send_keys(Keys.RETURN)

time.sleep(2)
while exiter==0:
    texts = driver.find_element_by_class_name("z_tTQ")
    a = texts.text
    b = a.split()
    print(b[len(b)-2])
    try:
        message = driver.find_element_by_class_name("_3uMse _118Ah")
    except:
        message = driver.find_element_by_class_name("_3uMse")

    if b[len(b)-2] == "/time":
        now = datetime.datetime.now()
        crtime= now.strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(2)

        message.send_keys(crtime)
        message.send_keys(Keys.RETURN)

    elif b[len(b)-2] == "/exit":
        driver.close()
        exiter=1

    elif b[len(b)-2] == "/jash":
        jmess="Jash is one of the greatest people alive and has designed this entire platform... He is the elected leader of the world and shall go down in history as the greatest soldier in the duck army..."
        message.send_keys(jmess)
        message.send_keys(Keys.RETURN)
    elif b[len(b)-2] == "/help":
        search = driver.find_element_by_class_name("_3FRCZ")
        search.send_keys("myself")
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            message = driver.find_element_by_class_name("_3uMse _118Ah")
        except:
            message = driver.find_element_by_class_name("_3uMse")
        message.send_keys("Someone has triggered Help on the group: ", "Your group here")
        message.send_keys(Keys.RETURN)
    elif b[len(b)-2] == ("/search"):
        message.send_keys("Please write what you would like to search after this :")
        message.send_keys(Keys.RETURN)
        texts = driver.find_element_by_class_name("z_tTQ")
        message.send_keys("search it yourself on google dumass")
        message.send_keys((Keys.RETURN))



    elif b[len(b)-2] == ("/joke"):
        joke= pyjokes.get_joke()
        message.send_keys(joke)
        message.send_keys(Keys.RETURN)
    elif b[len(b)-2]==("/fact"):
        fact = randfacts.getFact()
        message.send_keys(fact)
        message.send_keys(Keys.RETURN)

    elif b[len(b)-2]==("/news"):
        def NewsFromBBC():
            main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=28761f98c19940c78675c38d6babb8b7"
            open_bbc_page = requests.get(main_url).json()
            article = open_bbc_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                message.send_keys(i + 1, results[i])
                message.send_keys(Keys.RETURN)
        if __name__ == '__main__':
            NewsFromBBC()

    elif b[len(b)-2]==("/hangman"):
        word_list = words.words()
        vowels = ["a", "e", "i", "o", "u"]
        message.send_keys("welcome to hangman ")
        time.sleep(1)
        message.send_keys(Keys.RETURN)
        chosenword = random.choice(word_list)
        message.send_keys("the length of the chosen word is: ", len(chosenword))
        time.sleep(1)
        message.send_keys(Keys.RETURN)
        lettersleft = len(chosenword)

        print(chosenword)
        for windex in range(len(chosenword)):
            for windexer in range(5):
                if chosenword[windex] == vowels[windexer]:
                    message.send_keys("Letter number ", windex + 1, " is the letter ", vowels[windexer])
                    message.send_keys(Keys.RETURN)
                    time.sleep(1)
                    lettersleft = lettersleft - 1

        message.send_keys("you have seven guesses")
        message.send_keys(Keys.RETURN)
        guesses = 1
        correct = 0
        alreadyguessed = ["a", "e", "i", "o", "u"]
        while guesses <= 7:
            message.send_keys(" guess ")
            message.send_keys(Keys.RETURN)
            time.sleep(8)
            texts = driver.find_element_by_class_name("z_tTQ")
            a = texts.text
            b = a.split()

            guessedword= (b[len(b) - 2])
            for wordsel in range(len(alreadyguessed)):
                if guessedword == alreadyguessed[wordsel]:
                    message.send_keys("you already guessed this word...")
                    message.send_keys(Keys.RETURN)
                    message.send_keys("please reinput")
                    message.send_keys(Keys.RETURN)
                    time.sleep(4)
                    texts = driver.find_element_by_class_name("z_tTQ")
                    a = texts.text
                    b = a.split()
                    guessedword = (b[len(b) - 2])
                    wordsel = 0

            numofcorrect = 0
            for wordchosen in range(len(chosenword)):
                if chosenword[wordchosen] == guessedword:
                    time.sleep(1)
                    message.send_keys("congrats your guess ", guessedword, " was right")
                    message.send_keys(Keys.RETURN)
                    message.send_keys("It was letter number ", wordchosen + 1)
                    message.send_keys(Keys.RETURN)
                    numofcorrect = numofcorrect + 1
                    correct = 1
                    alreadyguessed.append(guessedword)
            if correct == 0:
                time.sleep(1)
                message.send_keys("oops you got it wrong, you now have ", 7 - guesses, " guesses left ")
                message.send_keys(Keys.RETURN)
                guesses = guesses + 1
                if guesses == 8:
                    message.send_keys("Game over!!")
                    message.send_keys(Keys.RETURN)
                    message.send_keys("the word was ", chosenword)
                    message.send_keys(Keys.RETURN)

            else:
                lettersleft = lettersleft - numofcorrect
                time.sleep(1)
                message.send_keys("You have to guess ", lettersleft, " more letters")
                message.send_keys(Keys.RETURN)
                if lettersleft == 0:
                    message.send_keys("congrats you won!!")
                    message.send_keys(Keys.RETURN)
                    message.send_keys("you guessed the word ", chosenword)
                    message.send_keys(Keys.RETURN)
                    guesses = 8
            wordchosen = 0
            correct = 0

    elif b[len(b)-2] == "/note":
        message.send_keys("Please write the note for Jash now and enter a full stop in the next message after your message is over.:")
        message.send_keys(Keys.RETURN)
        texts = driver.find_element_by_class_name("z_tTQ")
        a = texts.text
        b = a.split()
        crlen= len(b)
        while b[len(b)-2]!= ".":
            texts = driver.find_element_by_class_name("z_tTQ")
            a = texts.text
            b = a.split()
        texts = driver.find_element_by_class_name("z_tTQ")
        a = texts.text
        b = a.split()
        print(b)
        aflen = len(b)
        print(aflen)
        print(crlen)

        lenofstring= aflen-crlen
        print(lenofstring)
        startpos= crlen
        print(b[startpos])
        endpos= aflen - 3

        note= b[startpos:endpos]
        print(b[startpos:endpos])
        notestring = ' '.join([str(elem) for elem in note])
        time.sleep(1)
        note_object = open("notes", "a+")
        note_object.write(notestring)
        note_object.write("\n")
        note_object.close()

    else:
        ctr=ctr+1