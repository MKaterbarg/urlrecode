import urllib.parse
import sys


def main():

    if len(sys.argv) == 3:

        if sys.argv[1] == "-e":
            print(urllib.parse.quote(str(sys.argv[2])))

        if sys.argv[1] == "-d":
            print(urllib.parse.unquote(str(sys.argv[2])))

    elif len(sys.argv) == 2:

        if sys.argv[1] == "-h":
            help()

        elif(sys.stdin is not None):
            if sys.argv[1] == "-e":
                print(urllib.parse.quote(str(sys.stdin.readline())))

            if sys.argv[1] == "-d":
                print(urllib.parse.unquote(str(sys.stdin.readline())))


        else:
            print("Incorrect Syntax. Please see 'urlrecode -h' for usage and help")
            print()
            help()

    elif len(sys.argv) == 1:
        help()

    else:
        print("Incorrect Syntax. Please see 'urlrecode -h' for usage and help")
        print()
        help()


def help():
    print("urlrecode")
    print("Usage Syntax: urlrecode <parameter> \"<string to process>\""
          "\n\n"
          "Parameters: \n"
          "     -d      URL Decode string\n"
          "     -e      URL Encode string\n\n"
          "urlrecode expects two command line parameters to be given. Either -d or -e to specify the required action, followed by the string which it should process\n\n"
          "urlrecode version 1.0.9\n"
          "Created by Martijn Katerbarg as a simple way to get urlencode / urldecode functionality in linux cli")


if __name__ == "__main__":
    main()
