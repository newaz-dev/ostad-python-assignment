try:
    def greet(name):
        x = name.replace(" ", "")
        if x.isalnum():
            print(f"Hello {name}")
        else: 
            print("Please! Enter a valid name")
    greet(input("Enter name: "))
except Exception as e:
    print("Something happens here: ", e)