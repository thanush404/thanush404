def create_name(first , last):
    first = first.capitalize()
    last = last.capitalize()

    return first + " " + last

full_name = create_name('giga' , 'chad')
print(full_name)