def division(a,b):
    try:
        div=a/b
        print(a,"divided by",b,"is : ",div)

    except Exception as e:
        print("Error : ",e)


def openFile():
    try: 
        with open("mod1.py","r") as f:
            content=f.read
            print("Done")

    except FileNotFoundError:
        print("File not found, sorry !")

    else:
        print("Closing file")
        f.close()

    finally:
        print("This work with or without error both time")


division(10,0)
openFile()