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
    prob = line[2]
    bigrams[bigram] = prob

verb = ambiguities[0]
verbs = []
tags = ambiguities[1].split(' ')
verbalForms = ambiguities[2].split(' ')


for line in lines:
    print '\n' + line

    line = re.sub(r'([\.,?!:;"()])', r' \1 ', line)
    line = re.sub(r'([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])', r'\1 - \2', line)
    line = re.sub(r' +', r' ', line)
    line = re.sub(r'\. \. \.', r'\.\.\.', line)
    
    words = line.split(' ')
    lastWord = lineBeginning
    probsPerTag = {}
    originalForm = ''

    for word in words:
        lower = word.lower()
        match = regexp.match(lower)
        if (lastWord in verbalForms) or (lastWord == verb):
            if match and ((match.group(1) in verbalForms) or (match.group(1) == verb)):
                originalForm = word
                temp = {}
                for bigram, prob in probsPerTag.iteritems():
                    tag = bigram[1].split('/')[1]
                    for tag in tags:
                        newBigram = (bigram[1], verb + '/' + tag)
                        temp[newBigram] = float(bigrams[newBigram])
                        totalProb = temp[newBigram] * prob
                        print '\t' + originalForm, tag, totalProb

                probsPerTag = temp

            else:
                for bigram, prob in probsPerTag.iteritems():
                    tag = bigram[1].split('/')[1]
                    newBigram = (bigram[1], lower)
                    totalProb = float(bigrams[newBigram]) * prob
                    print '\t' + originalForm, tag, totalProb
                    probsPerTag = {}

                    
        else: 
            if match and ((match.group(1) in verbalForms) or (match.group(1) == verb)):
                originalForm = word
                for tag in tags:
                    bigram = (lastWord, verb + '/' + tag)
                    probsPerTag[bigram] = float(bigrams[bigram])

        lastWord = lower

