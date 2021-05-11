input_text = input()
d = dict()
for i in range(len(input_text)):
    if input_text[i] != ' ':
        if input_text[i] in d:
            d[input_text[i]] += 1
        else:
            d[input_text[i]] = 1
for k in sorted(d):
    print(k, d[k])
