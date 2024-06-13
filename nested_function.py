def outer(name):
    print("good morning",name)
    def inner(name):
        print("hai ",name)

    inner("deekshay")
outer("akshy")
