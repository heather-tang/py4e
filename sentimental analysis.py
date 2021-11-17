punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
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

def strip_punctuation(str):
    for char in punctuation_chars:
        if char in str:
            str = str.replace(char, '')
    return str

def get_pos(str):
    str = strip_punctuation(str)
    cnt = 0
    for word in str.split():
        if word.lower() in positive_words:
            cnt += 1
    return cnt

def get_neg(str):
    str = strip_punctuation(str)
    cnt = 0
    for word in str.split():
        if word.lower() in negative_words:
            cnt += 1
    return cnt

with open('project_twitter_data.csv', 'r') as twi_f:
    ret = []
    rep = []
    pos = []
    neg = []
    net = []
    count = 0
    lines = twi_f.readlines()
    for line in lines[1:]:
          ret.append(line.split(',')[1])
          rep.append(line.strip().split(',')[2])
          pos.append(get_pos(line))
          neg.append(get_neg(line))
          net.append(get_pos(line)-get_neg(line))
          count += 1

outfile = open('resulting_data.csv', 'w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

for n in range(len(ret)):
    row_string = '{}, {}, {}, {}, {}'.format(ret[n], rep[n], pos[n], neg[n], net[n])
    outfile.write(row_string)
    outfile.write('\n')

with open('resulting_data.csv', 'r') as f:
          for line in f:
            print(line)


    #print('positive words count: ', pos_cnt)
    #print('negative words count: ', neg_cnt)
