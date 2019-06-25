import jieba

def fenci(sentence):
    seg_list = jieba.cut(sentence, cut_all = False)
    return " ".join(seg_list)