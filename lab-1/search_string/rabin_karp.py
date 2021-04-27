def search(text, pattern):
    cmp_count = 0
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return (0, cmp_count)
    if text_size == 0 or pattern_size > text_size:
        return (-1, cmp_count)
    circle_module = 1000000000 + 7
    prime_number = 1007
    pattern_hash = 0
    for i in range(pattern_size):
        pattern_hash = (pattern_hash * prime_number + ord(pattern[i])) % circle_module
    text_hash = 0
    text_decipher = []
    for i in range(text_size):
        text_hash = (text_hash * prime_number + ord(text[i])) % circle_module
        text_decipher.append(text_hash)
    text_decryption = [1]
    for i in range(1, text_size + 1):
        text_decryption.append((text_decryption[i - 1] * prime_number) % circle_module)

    def get_hash(l, r):
        ans = text_decipher[r]
        if l != 0:
            ans -= text_decipher[l - 1] * text_decryption[r - l + 1] % circle_module
            if ans < 0:
                ans += circle_module
        return ans

    for i in range(0, text_size - pattern_size + 1):
        # the slice could be replaces with a loop
        cmp_count += 1
        if get_hash(i, i + pattern_size - 1) == pattern_hash:
            return (i, cmp_count)

    return (-1, cmp_count)