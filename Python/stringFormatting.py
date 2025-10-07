def greeting(name):
    # both are same
    print("hello {},how r u?".format(name))
    print("hello {name},how r u?".format(name=name))
greeting("Mahin")