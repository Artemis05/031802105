import jieba
import jieba.analyse
import numpy as np
import math
import re
import sys




def get_vector(text1,text2):
    # 分词
    words1 = jieba.cut(text1)
    words2 = jieba.cut(text2)
    list_word1 = (','.join(words1)).split(',')
    list_word2 = (','.join(words2)).split(',')

    # 列出所有的词,取并集
    key_word = list(set(list_word1 + list_word2))
    # 给定形状和类型的用0填充的矩阵存储向量
    vector1 = np.zeros(len(key_word))
    vector2 = np.zeros(len(key_word))

    # 计算词频
    # 依次确定向量的每个位置的值
    for i in range(len(key_word)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(list_word1)):
            if key_word[i] == list_word1[j]:
                vector1[i] += 1
        for k in range(len(list_word2)):
            if key_word[i] == list_word2[k]:
                vector2[i] += 1
    # 输出向量
    return vector1,vector2


def numerator(vector1, vector2):
    #分子
    return sum(a * b for a, b in zip(vector1, vector2))

def denominator(vector):
    #分母
    return math.sqrt(sum(a * b for a,b in zip(vector, vector)))

def run(vector1, vector2):
    return numerator(vector1,vector2) / (denominator(vector1) * denominator(vector2))

def get_similarity(text1,text2):
    vectors = get_vector(text1,text2)
    # 相似度
    similarity = run(vector1=vectors[0], vector2=vectors[1])
    return similarity


if __name__ == '__main__':
     text1=input("原文件：")
     text2=input("对比文件：")
     ans = get_similarity(text1, text2)
     print(ans)



      
