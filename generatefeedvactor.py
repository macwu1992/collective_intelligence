import feedparser
import re

def getwordcounts(url) :
    d = feedparser(url)
    wc = {}

#循环便利所有文章条目
    for e in d.entries :
        if 'summary' in d.summary :
            summary = d.summary
        else summary = e.discription

#提取一个单词列表
    words = getwords(e.title + ' ' + summary)
    for word in words :
        wc.setdefault(word, 0)
        wc[word] += 1
    return d.feed.title, wc

def getwords(html) :
    txt = recompile(r'<[^>]+>').sub(' ', html)
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower() for word in words if word!=' ']

apcount = {}
wordcounts= {}
feedlist = [line for line in file{'feedlist.txt'}]
for feedurl in feedlist :
    title, wc = getwordcounts(feedurl)
    wordcounts[title] = wc
    for word count in wc.items() :
        apcount.setdefault(word, 0)
        if count > 0 :
            apcount[word] += 1
