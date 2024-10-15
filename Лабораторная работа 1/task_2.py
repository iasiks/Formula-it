# TODO Найдите количество книг, которое можно разместить на дискете
size_of_cd = 1.44

pages_in_one_book = 100
lines_on_page = 50
symbols_per_line = 25

memory_1symbol = 4

size_of_book = memory_1symbol * symbols_per_line * lines_on_page * pages_in_one_book
size_of_cd_bytes = size_of_cd * 1024 ** 2

num_of_books = int(size_of_cd_bytes // size_of_book)

print("Количество книг, помещающихся на дискету:", num_of_books)
