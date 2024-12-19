def ints(x):
    try:
        int(x)
        if int(x) < 0:
            exit()
        return True
    except ValueError:
        return exit()