import sys
import re

def check():
    if (len(sys.argv) != 1):
        print("This function accepts no arguments")
        return True
    return False

def main():
    if not check():
        res = True
        regList = [re.compile('\*[^\*]{3}\*'), \
                   re.compile('\*\*[^\*]\*\*'), \
                   re.compile('\*[^\*]\*[^\*]\*')]
        counter = 0
        for str_ in sys.stdin:
            if len(str_.strip()) != 5 or counter == 3 or not regList[counter].search(str_):
                res = False
                break
            counter += 1
        print(res)
    
if __name__ == "__main__":
    main()