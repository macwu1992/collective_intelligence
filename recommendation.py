#coding:utf-8

critics = {
    'Lisa Rose':{
        'Lady in The Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
        'Superman Returns': 3.5, 'You, Me And Dupree': 2.5, 'The Night Listeners': 3.0
    },
    'Gene Seymour':{
        'Lady in The Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,
        'Superman Returns': 5.0, 'You, Me And Dupree': 2.5, 'The Night Listeners': 3.0
    },
    'Michael Phillips':{
        'Lady in The Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5,
        'The Night Listeners': 3.0
    },
    'Claudia Puig':{
        'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listeners': 4.5,
        'Superman Returns': 4.0, 'You, Me And Dupree': 2.5,

    },
    'Mick LaSalle':{
        'Lady in The Water': 3.0, 'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me And Dupree': 2.0,
        'The Night Listeners': 3.0
    },
    'Jack Mathews':{
        'Lady in The Water': 3.0, 'Snakes on a Plane': 4.0, 'Superman Returns': 5.0,
        'You, Me And Dupree': 3.5, 'The Night Listeners': 3.0
    },
    'Toby':{
        'Snakes on a Plane': 4.5, 'Superman Returns': 4.0, 'You, Me And Dupree': 1.0,
    }
}

from math import sqrt

def sim_distance(pref, person1, person2):
    si = {}
    for item in pref[person1]:
        if item in pref[person2]:
            si[item] = 1
    if len(si) == 0: return 0
    sum_pow = sum([pow(pref[person1][item] - pref[person2][item], 2) for item in pref[person1] if item in pref[person2]])

    return 1/(1+sqrt(sum_pow))

def sim_pearson(pref, person1, person2):
    si = {}
    if person1 == person2:
        print("same person!!!")
        return 0
    for item in pref[person1]:
        if item in pref[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0

    n = len(si)

    sum1 = sum(pref[person1][item] for item in si)
    sum2 = sum(pref[person2][item] for item in si)

    pow_sum1 = sum(pow(pref[person1][item], 2) for item in si)
    pow_sum2 = sum(pow(pref[person2][item], 2) for item in si)

    p_sum = sum(pref[person1][item] * pref[person2][item] for item in si)

    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((pow_sum1 - sum1*sum1/n)*(pow_sum2 - sum2*sum2/n))

    if den == 0: return 0

    r = num / den
    return r

def get_Recommdation(pref, person, similarity = sim_pearson):
    sim = {}
    s_sim_sum = {}

    sim_sum = 0

    for other in pref:
        if other != person:
            sim[other] = similarity(pref, person, other)

    #对于每个除了自己的人，都算出相似度，切相似度有可能为负值！
    for other in pref:
        if other != person and sim[other] > 0:
            sim_sum = sum(sim[other] for other in pref if other != person)
            #有评分的item，如果自己没看过，则做出预测评分
            for item in pref[other]:
                if pref[other][item] != 0 and (item not in pref[person] or pref[person][item] == 0):
                    s_sim_sum.setdefault(item, 0)
                    s_sim_sum[item] += pref[other][item] * sim[other]

    for item in s_sim_sum:
        s_sim_sum[item] = s_sim_sum[item] / sim_sum

    result = [(s_sim_sum[item], item) for item in s_sim_sum]
    result.sort()
    result.reverse()
    return result

def topMathes(pref, person, n, similarity = sim_pearson):
    score = [(similarity(pref, person, other), other) for other in pref if other != person]

    score.sort()
    score.reverse()
    return score[0:n]

print(get_Recommdation(critics, 'Toby'))

import pydelicious

pydelicious.get_popular(tag = "music")
