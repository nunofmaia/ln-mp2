# -*- coding: utf-8 -*- 

import sys
import re


bigramsFile = sys.argv[1]
ambiguityFile = sys.argv[2]
corpus = sys.argv[3]
lineBeginning = '<s>'

regexp = re.compile('([a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ]+)(-[a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ]+)*')

bigrams = {}
ambiguities = [line.strip() for line in open(ambiguityFile)]
lines = [line.strip() for line in open(corpus)]

for line in open(bigramsFile):
    line = line.strip().replace('\t', ' ').split(' ')
    bigram = (line[0], line[1])
    prob = float(line[2])
    bigrams[bigram] = prob

verb = ambiguities[0]
verbs = []
tags = ambiguities[1].split(' ')
verbalForms = ambiguities[2].split(' ')

lowestProb = min(bigrams.values())


for line in lines:
    print '\n' + line

    line = lineBeginning + ' ' + line
    line = re.sub(r'([\.,?!:;"()])', r' \1 ', line)
    line = re.sub(r'([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])', r'\1 - \2', line)
    line = re.sub(r' +', r' ', line)
    line = re.sub(r'\. \. \.', r'\.\.\.', line)
    
    words = line.strip().split(' ')
    lastWord = lineBeginning
    findings = []
    probs = {}
    
    def rec(d, l):
        if len(d) == 0:
            c = sorted(l, key=lambda tup: tup[0])
            s = ''
            p = 1.0
            for v in c:
                s += v[1] + ' '
                p *= probs[v]
            print s, p
        
        else:
            el = d.keys()[0]
            n = dict((key,value) for key, value in d.iteritems() if key[0] != el[0])
            m = dict((key,value) for key, value in d.iteritems() if key[0] == el[0])
            for key, val in m.iteritems():
                t = l
                t.append(key)
                rec(n, t)
                t.pop()

    for index, word in enumerate(words):
        lower = word.lower()
        if (lower in verbalForms) or (lower == verb):
            b = [words[index - 1], word, words[index + 1]]
            findings.append(b)

    for index, result in enumerate(findings):
        for tag in tags:
            tagged = verb + '/' + tag
            p1 = lowestProb if not bigrams.get((result[0], tagged)) else bigrams.get((result[0], tagged))
            p2 = lowestProb if not bigrams.get((tagged, result[2])) else bigrams.get((tagged, result[2]))
            prob = p1 * p2
            probs[(index, result[1] + '/' + tag)] = prob

        
    #for choice, prob in probs.iteritems():
    #    other = dict((key,value) for key, value in probs.iteritems() if key[0] != choice[0])
    #    if len(other) > 0:
    #        for otherChoice, otherProb in other.iteritems():
    #            if choice[0] < otherChoice[0]:
    #                print choice[1], otherChoice[1], prob * otherProb
    #    else:
    #        same = dict((key,value) for key, value in probs.iteritems() if key[0] == choice[0])
    #        for sameChoice, sameProb in same.iteritems():
    #            print sameChoice[1], sameProb

    #    #print choice[0], other
    
    rec(probs, [])
