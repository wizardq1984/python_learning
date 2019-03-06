# -*- coding: utf-8 -*-
with open('e:/GitHub/python_learning/student_score.txt') as scores:
    ori_score = []
    for line in scores.readlines():
        if line[-1] == '\n':
            line = line.replace('\n', '')  # remove \n from every lines
        line = line.split(' ')
        ori_score.append(line)
ori_score[0].append('总分')
ori_score[0].append('平均分')
ori_score[0].insert(0, '名次')
title = ori_score.pop(0)
print(title)


def ave_score(score_list):
    name = score_list.pop(0)
    sum_scores = 0
    for i in score_list:
        sum_scores += int(i)
    ave_scores = round(sum_scores/len(score_list), 1)
    score_list.append(str(sum_scores))
    score_list.append(str(ave_scores))
    score_list.insert(0, name)
    return score_list


result_score = []
for single_score in ori_score:
    result_score.append(ave_score(single_score))
print(result_score)

ave_single_score = []
ave_single_score[0] = '平均'
