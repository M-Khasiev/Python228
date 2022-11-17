def decor(fn):
    def wrap(*f_args):
        fn(*f_args)
        print("Среднее арифметическое чисел ", end="")
        for i in range(len(f_args)):
            if i == len(f_args) - 1:
                print(f_args[i], " ", sep="", end="")
            else:
                print(f_args[i], ", ", sep="", end="")
        print("=", sum(f_args) / len(f_args))

    return wrap


@decor
def func(*args):
    print("Сумма чисел ", end="")
    for i in range(len(args)):
        if i == len(args) - 1:
            print(args[i], " ", sep="", end="")
        else:
            print(args[i], ", ", sep="", end="")
    print("=", sum(args))


func(2, 3, 3, 4)
func(2, 3, 3, 4, 10, 3, 5, 6)



