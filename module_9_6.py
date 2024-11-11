def all_variants(text):
    l = len(text)
    for k in range(l):
        for z in range(l - k):
            yield text[k:k+1+z]

a = all_variants("abc")
for i in a:
    print(i)