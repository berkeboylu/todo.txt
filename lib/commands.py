import os
import datetime

PATH = "./todo.txt"
DONE = "./done.txt"

class todo:
    def add(t):
        if listToString(t) != "": 
            dt = datetime.datetime.today()
            LINE = "{}-{}-{} {}".format(dt.year, dt.month, dt.day, listToString(t))
            write(LINE)
            print(colors.success("{} added on line {}".format(listToString(t), len(open(PATH).readlines()))))
        else:
            print(colors.usage("#USAGE : t add \"THING I NEED TO DO +project @context\""))

    def append(t):
        reader = read()
        if lineExist(reader, t[0]):
            reader[int(t[0]) - 1] = reader[int(t[0]) - 1].replace("\n", " ") + listToString(t[1::])
            reader.reverse()
            write(reader)
            print(colors.success("{} appended to line {}".format(listToString(t[0]), listToString(t[1::]))))

    def list(t):
        reader = read()
        dt = datetime.datetime.today()

        if len(t) > 0:
            TERM = listToString(t)

            for element in range(len(reader)):
                el = reader[element]
                if TERM in el:
                    
                    LINE = el.replace("\n", "").split(" ")
                    #clears date
                    for i in range(len(LINE)):
                        if (LINE[i].startswith(str(dt.year))):
                            del LINE[i]
                            break

                    print(colors.line("{}\t{}".format(str(element + 1),listToString(LINE))))
        else:
            for element in range(len(reader)):
                LINE = reader[element].replace("\n", "").split(" ")
                #clears date
                for i in range(len(LINE)):
                    if (LINE[i].startswith(str(dt.year))):
                        del LINE[i]
                        break

                print(colors.line("{}\t{}".format(str(element + 1), listToString(LINE))))

    def listpri(t):
        ALPHABET = split('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        TERM = ""
        reader = read()
        dt = datetime.datetime.today()
        if (len(t) >= 1):
            if len(t) > 1: TERM = t[1]
            if ("-" in t[0]):
                UNTIL = t[0].split("-")
                for element in range(ALPHABET.index(UNTIL[0].upper()), ALPHABET.index(UNTIL[1].upper()) + 1):
                    for el in reader:
                        if "({})".format(ALPHABET[element]) in el:
                            if TERM != "" and TERM in el:
                                print(el.replace("\n", ""))
                            elif TERM == "":  
                                print(el.replace("\n", ""))
            else:
                for el in reader:
                    LINE = el.replace("\n", "").split(" ")
                    #clears date
                    for i in range(len(LINE)):
                        if (LINE[i].startswith(str(dt.year))):
                            del LINE[i]
                            break
                    if "({})".format(t[0].upper()) in el:
                        print(listToString(LINE))
        else:
            for el in ALPHABET:
                for element in reader:
                    if "({})".format(el) in element:
                        LINE = element.replace("\n", "").split(" ")
                        #clears date
                        for i in range(len(LINE)):
                            if (LINE[i].startswith(str(dt.year))):
                                del LINE[i]
                                break
                        print(listToString(LINE))

class colors:
    def error(t): return "\033[91m" + t + " \033[00m"
    def success(t): return "\033[92m" + t + " \033[00m"
    def usage(t):return  "\033[93m" + t + " \033[00m"
    def line(t): return "\033[94m" + t + " \033[00m"
    def prPurple(t): return "\033[95m" + t + " \033[00m"
    def prCyan(t): return "\033[96m" + t + " \033[00m"



def write(t):
    if (type(t) == list):
        writer = open(PATH, "w")
        for el in t:
            writer.write(el.replace("\n", "") + "\n")
    elif (type(t) == str):
        writer = open(PATH, "a")
        writer.write(t.replace("\n", "") + "\n")
    writer.close()

def read():
    reader = open(PATH).readlines()
    reader.reverse()
    return reader

def listToString(arr): return (" ".join(arr))

def lineExist(arr, line): 
    if (len(arr) >= int(line)):
        return True
    else: return False

def split(word): 
    return [char for char in word]  