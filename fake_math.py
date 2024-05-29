

def divide(first, second):

    if second == 0:
        return 'Ошибка'
    else:
        div = first / second
        return div


result1 = divide(69, 3)
result2 = divide(3, 0)
print(result1)
print(result2)

if __name__ == '__fake_math__':
    fake_math()