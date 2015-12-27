def happy(number):
    next_ = sum(pow(int(char), 2) for char in str(number))
    return number in (1, 7) if number < 10 else happy(next_)
