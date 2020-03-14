
## A program to debug
def simple_function(div):
    simple_x = 2
    simple_y = div

    return fancy_function(simple_x, simple_y)


def fancy_function(x, y):
    r = x / y
    return r


def main():
    print(simple_function(2))


if __name__ == "__main__":
    main()
