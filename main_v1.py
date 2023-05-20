def read_books(books, k, current=[], result=[]):

    if len(current) == k:
        result.append(current)
    else:
        for i in range(len(books)):
            if books[i] not in current:
                read_books(books, k, current + [books[i]], result)
    return result

k = int(input("Введите количество книг: "))
books = [f" Book{i}" for i in range(1, k + 1)]

result = read_books(books, k)
print(result)
