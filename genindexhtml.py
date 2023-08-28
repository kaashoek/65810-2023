#!/usr/bin/env python

anchor='</a>'
token='#paper#'

papers = []
with open("papers.txt", "r") as f:
    txt = f.read()
    while len(txt) > 0:
        i = txt.find('<a ')
        if i < 0:
            break
        j = txt.find(anchor)
        if j < 0:
            print("missing anchor")
        l = len(anchor)
        p = txt[i:j+l]
        papers.append(p)
        txt = txt[j+l:]

pi = 0
with open("index.txt", "r") as f:
    txt = f.read()
    while True:
        i = txt.find(token)
        if i < 0:
            break
        txt = txt[0:i]+papers[pi]+txt[i+len(token):]
        pi += 1
        if pi >= len(papers):
            break
        
print(txt)
