import jieba

def fenci(sentence):
    seg_list = jieba.cut(sentence, cut_all = True)
    return seg_list