import sys
import re

def check():
    error = False;
    if len(sys.argv) != 2:
        print("The number of arguments must be equal to one")
        error = True
    elif not re.fullmatch(r'\d*', sys.argv[1]):
        print("The argument must be a number")
        error = True
    return error

def main():
    if not check():
        counter = int(sys.argv[1]);
        for str_ in sys.stdin:
            if counter == 0:
                print("The output lines have run out")
                break
            if len(str_.strip()) == 32 and str_[:5] == "00000" and str_[5] != '0':
                print(str_)
            counter -= 1

if __name__=="__main__": 
    main() 