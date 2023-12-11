def a(phrase):
    words = phrase.split()
    return len(words)


def b(phrase):
    words = phrase.split()
    some_list = []
    max_length = 0
    max_word = ""

    loops = len(words)
    while loops != 0:
        for i in words:
            if len(i) > max_length:
                max_length = len(i)
                max_word = i
        words.remove(max_word)
        some_list.append(max_word)
        max_length = 0
        max_word = ""
        loops -= 1

    var = f"{some_list[0]}"
    for i in some_list[1:]:
        var += f", {i}"
    return var


def c(phrase):
    words = phrase.split()
    words.sort()

    var = f"{words[0]}"
    for i in words[1:]:
        var += f", {i}"
    return var
