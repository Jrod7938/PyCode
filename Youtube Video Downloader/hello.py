def main():
    name = input("What is your name?")
    if name == "":
        quit()
    else:
        for i in range(len(name)):
            print(name[i])

main()