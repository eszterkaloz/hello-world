import sys

def main(argv):
    if argv == sys.argv[:0]:
    #if len(sys.argv) == 1:
        print("Hello World!")
    #if len(sys.argv) > 0:
    else:
        print ("Hello " + sys.argv[1] + "!")



if __name__ == "__main__":
    main(sys.argv[1:])
