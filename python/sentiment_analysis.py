
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(chars):
    a = list(chars)
    for i in range(len(a)):
        if a[i] in punctuation_chars:
            a[i] = ''
    return ''.join(a)

def get_neg(chars):
    global negative_words
    a = chars.split()
    c = 0
    for i in a:
        i = strip_punctuation(i)
        if i.lower() in negative_words:
            c += 1
    return c
def get_pos(chars):
    global positive_words
    a = chars.split()
    c = 0
    for i in a:
        i = strip_punctuation(i)
        if i.lower() in positive_words:
            c += 1
    return c

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

f = open('project_twitter_data.csv','r')
o = open('resulting_data.csv','w')
o.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')

b = f.readlines()
for line in b[1:]:
    a = line.split(',')
    p_s = get_pos(a[0])
    n_s = get_neg(a[0])
    net_s = p_s - n_s
    o.write('{},{},{},{},{}\n'.format(a[1],a[2].strip(),p_s,n_s,net_s))
