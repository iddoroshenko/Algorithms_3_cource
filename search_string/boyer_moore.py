def search(text, pattern):
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return 0
    if text_size == 0 or pattern_size > text_size:
        return -1

    shift_distance = [pattern_size for x in range(256)]
    for i in range(pattern_size - 1):
        shift_distance[ord(pattern[i])] = pattern_size - i - 1
    i = 0
    while i != text_size - pattern_size + 1:
        flag = True
        for j in range(pattern_size - 1, -1, -1):
            if text[i+j] != pattern[j]:
                if j != pattern_size and shift_distance[ord(pattern[-1])] != pattern_size:
                    i += shift_distance[ord(pattern[-1])]
                else:
                    i += shift_distance[ord(text[i+j])]
                flag = False
                break
        if flag:
            return i
    return -1
