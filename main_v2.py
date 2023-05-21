import random

def read_books(books, k, current=[], result=[]):
    if len(current) == k:
        result.append(current)
    else:
        for i in range(len(books)):
            if books[i] not in current:
                read_books(books, k, current + [books[i]], result)
    return result

def rating_and_pages(books):
    for book in books:
        rating = round(random.uniform(1.0, 5.0), 1)
        pages = random.randint(50, 500)
        book['rating'] = rating
        book['pages'] = pages
    return books

def get_permutations(books, r):
    if r == 0:
        return [[]]
    permutations = []
    for i in range(len(books)):
        for permutation in get_permutations(books[:i] + books[i+1:], r-1):
            permutations.append([books[i]] + permutation)
    return permutations

k = int(input("Введите количество книг: "))
books = [{'title': f"Book{i+1}"} for i in range(k)]

all_book_sequences = read_books(books, k)
print("Все возможные последовательности книг:")
for sequence in all_book_sequences:
    print([book['title'] for book in sequence])

books = rating_and_pages(books)

print("Список книг с присвоенными рейтингом и количеством страниц:")
for book in books:
    print(book)

books = [book for book in books if 100 <= book['pages'] <= 300]

if books:
    min_rating_book = min(books, key=lambda x: x['rating'])
else:
    min_rating_book = None
max_rating_book = max(books, key=lambda x: x['rating'])

sequences = []
for i in range(2, len(books) + 1):
    for sequence in get_permutations(books, i):
        sequence = list(sequence)
        if min_rating_book in sequence:
            sequence.remove(min_rating_book)
            sequence.append(min_rating_book)
        if max_rating_book in sequence:
            sequence.remove(max_rating_book)
            sequence.insert(1, max_rating_book)
        for j in range(2, len(sequence)):
            if sequence[j] in [min_rating_book, max_rating_book]:
                continue
            for k in range(j-1, 0, -1):
                if sequence[k] in [min_rating_book, max_rating_book]:
                    continue
                if sequence[k]['rating'] < sequence[j]['rating']:
                    sequence[k+1:j+1] = sequence[k:j]
                    sequence[k] = sequence[j]
                    break
        if sequence not in sequences:
            sequences.append(sequence)

print("Уникальные возможные последовательности книг после фильтрации:")
for sequence in sequences:
    avg_rating = sum([book['rating'] for book in sequence]) / len(sequence)
    print([book['title'] for book in sequence], f"Средний рейтинг: {avg_rating:.2f}")

if sequences:
    max_avg_rating = max([sum([book['rating'] for book in sequence]) / len(sequence) for sequence in sequences])
    print("Максимальный средний рейтинг:", max_avg_rating)
else:
    print("Список последовательностей пустой, невозможно вычислить максимальный средний рейтинг.")
