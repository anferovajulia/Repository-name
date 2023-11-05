# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
string_= 50
symbols = 25
one_symbol = 4
volume = 1.44
one_book_kb = pages*string_*symbols*one_symbol/1024
one_book_mb = one_book_kb/1024
numbers = volume//one_book_mb
print("Количество книг, помещающихся на дискету:",round(numbers))
