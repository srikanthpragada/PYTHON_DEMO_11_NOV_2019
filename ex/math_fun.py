if __name__ == "__main__":
    print("I am in math_fun. It is run as script!")


def abs(n):
    return n if n >= 0 else -n


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
