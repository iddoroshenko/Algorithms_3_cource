def search(text, pattern):
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return 0
    if text_size == 0 or pattern_size > text_size:
        return -1

    def compute_prefix_function():
        prefix_function = [0 for x in range(text_size)]
        for i in range(1, text_size):
            j = prefix_function[i-1]
            while j > 0 and text[i] != text[j]:
                j = prefix_function[j-1]
            if text[i] == text[j]:
                j += 1
            prefix_function[i] = j
        return prefix_function

    prefix_function = compute_prefix_function()

    i = 0
    j = 0
    while j != text_size - pattern_size + 1:
        if i >= pattern_size:
            return j
        if text[j + i] != pattern[i]:
            if i == 0:
                j += 1
            elif prefix_function[i-1] == 0:
                j += i
                i = 0
            else:
                temp = j + i - prefix_function[i-1]
                i = prefix_function[i-1]
                j = temp
        else:
            i += 1
    if i == pattern_size:
        return text_size - pattern_size - 1
    else:
        return -1
