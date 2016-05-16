import sys

def main(argv):
    if argv == sys.argv[:0]:
        print("Hello World!")
    else:
        print ("Hello " + sys.argv[1] + "!")



if __name__ == "__main__":
    main(sys.argv[1:])
