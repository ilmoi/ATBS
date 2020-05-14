with open('text_to_read.txt', 'r') as f:
    txt = f.read()
    L = ['ADJECTIVE', 'NOUN', 'VERB']
    for l in L:
        if l in txt:
            user_input = input(f'{l} detected! Enter a replacement: ')
            txt = txt.replace(l, user_input)
    # r.write(txt)
    print(txt)
