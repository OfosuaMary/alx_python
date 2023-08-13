if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 1:
        print("0 arguments.")
    elif l == 2:
        print("{} argument:".format(l-1))
        print("1: {}".format(argv[1]))
    else :
        a = 1
        print("{} arguments:".format(l-1))
        while a < l:
            print("{}: {} ".format((a),argv[a]))
            a +=1
