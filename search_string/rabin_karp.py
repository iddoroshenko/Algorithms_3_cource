def search(text, pattern):
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return 0
    if text_size == 0 or pattern_size > text_size:
        return -1
    circle_module = 1000000000 + 7
    prime_number = 1007
    pattern_hash = 0
    prime_number_step = 1
    for i in range(pattern_size):
        pattern_hash = (pattern_hash + prime_number_step * ord(pattern[i])) % circle_module
        prime_number_step *= prime_number
    text_hash = 0
    prime_number_step = 1
    for i in range(pattern_size):
        text_hash = (text_hash + prime_number_step * ord(text[i])) % circle_module
        prime_number_step *= prime_number

    for i in range(0, text_size - pattern_size + 1):
        # the slice could be replaces with a loop
        if text_hash == pattern_hash and text[i:i+pattern_size] == pattern:
            return i
        if i != text_size - pattern_size:
            text_hash = (text_hash - ord(text[i])) / prime_number
            text_hash += ord(text[i+pattern_size]) * prime_number**(pattern_size-1)
    return -1
