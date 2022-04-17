def main():
    # TODO Write File
    # file = open("lco.txt", "w+")
    # for i in range(20):
    #     file.write("this is python code %d \n" % i)
    # file.close()
    # TODO Read File
    # file = open("lco.txt", "r")
    # if file.mode == "r":
    #     file_contents = file.read()
    #     print(file_contents)
    # file.close()
    # TODO Exception
    try:
        file = open("lc.txt", "r")
        print("Success in reading ")
    except IOError:
        print("File does not exist!")
    print("Task Done")


if __name__ == '__main__':
    main()
