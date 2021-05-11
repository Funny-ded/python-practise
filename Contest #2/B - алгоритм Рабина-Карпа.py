HASH_MODULE = 2 ** 61 - 1
HASH_BASE = 1013
R_OF_POWER = None


def get_hash(s, start=0, end=None):
    if end is None:
        end = len(s)
    p = 0
    for i in range(start, end):
        p = (p * HASH_BASE + ord(s[i])) % HASH_MODULE
    return p


def recalculate_hash(h, s, i_del, l_sub):
    return ((h - ord(s[i_del]) * R_OF_POWER) * HASH_BASE + ord(s[i_del + l_sub])) % HASH_MODULE


def compare(h_s, h_sub, s, sub, i_s_start):
    if h_s != h_sub:
        return False
    for i in range(len(sub)):
        if s[i + i_s_start] != sub[i]:
            return False
    return True


def get_entries(sub, s):
    l_sub = len(sub)
    l_s = len(s)
    global R_OF_POWER
    if R_OF_POWER is None:
        R_OF_POWER = 1
        for i in range(l_sub - 1):
            R_OF_POWER = (R_OF_POWER * HASH_BASE) % HASH_MODULE
    if l_sub > l_s:
        return []
    if l_sub == l_s:
        for i in range(l_sub):
            if s[i] != sub[i]:
                return []
        return [0]
    h_sub = get_hash(sub)
    result = []
    h_s = get_hash(s, end=l_sub)
    if compare(h_s, h_sub, s, sub, 0):
        result.append(0)
    for i in range(1, l_s - l_sub + 1):
        h_s = recalculate_hash(h_s, s, i - 1, l_sub)
        if compare(h_s, h_sub, s, sub, i):
            result.append(i)
    return result


if __name__ == '__main__':
    substring = input()
    string = input()
    arr = get_entries(substring, string)
    if not arr:
        print(-1)
    else:
        print(" ".join(map(str, arr)))