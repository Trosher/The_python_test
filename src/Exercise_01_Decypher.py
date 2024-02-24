import sys

def check():
    if (len(sys.argv) != 2):
        print("The argument cannot be empty and there must be only one argument")
        return True
    return False

def main():
    if not check():
        list_ = sys.argv[1].split(' ')
        for word in list_:
            print(word[0], end='')

if __name__ == "__main__":
    main()