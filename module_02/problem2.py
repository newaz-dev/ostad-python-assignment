try:
    x = input("Enter your name: ")
    with open("name.txt", 'a') as f:
        f.write(x)
        f.close()
    print("Name saved successfully")
except Exception as e:
    print("Something is wrong at here: ",e)
