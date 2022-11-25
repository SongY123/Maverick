import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Hint: usage \"python main.py xxx.m\"")
        print("Please input maverick file path: ")
        filename = input()
    else:
        filename = sys.argv[1]
