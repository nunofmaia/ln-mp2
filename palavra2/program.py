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

lowestProb = min(bigrams.values())


for line in lines:
    print '\n' + line

    line = re.sub(r'([\.,?!:;"()])', r' \1 ', line)
    line = re.sub(r'([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])', r'\1 - \2', line)
    line = re.sub(r' +', r' ', line)
    line = re.sub(r'\. \. \.', r'\.\.\.', line)
    
    words = line.split(' ')
    lastWord = lineBeginning
    otherWord = lineBeginning
    probsPerTag = {}
    originalForm = ''

    for word in words:
        lower = word.lower()
        lastLower = lastWord.lower()
        otherLower = otherWord.lower()
        match = regexp.match(lower)
        if (lastLower in verbalForms) or (lastLower == verb):
            originalForm = lastWord
            if match and ((match.group(1) in verbalForms) or (match.group(1) == verb)):
                temp = {}
                for bigram, prob in probsPerTag.iteritems():
                    tagin = bigram[1].split('/')[1]
                    for tag in tags:
                        tagged = verb + '/' + tag
                        newBigram = (bigram[1], tagged)
                        temp[newBigram] = 1.0
                        newProb = bigrams.get(newBigram)
                        if newProb:
                            temp[newBigram] *= float(bigrams[newBigram])
                        else:
                            temp[newBigram] *= float(lowestProb)

                        totalProb = temp[newBigram] * prob
                        if (otherLower in verbalForms) or (otherLower == verb):
                            otherTag = bigram[0].split('/')[1]
                            print '\t' + otherWord+'/'+otherTag, originalForm+'/'+tagin, word+'/'+tag, '\t'+str(totalProb)
                        else:
                            print '\t' + otherWord, originalForm+'/'+tagin, word+'/'+tag, '\t'+str(totalProb)

                probsPerTag = temp

            else:
                for bigram, prob in probsPerTag.iteritems():
                    tag = bigram[1].split('/')[1]
                    newBigram = (bigram, lower)
                    newProb = bigrams.get(newBigram)
                    if newProb:
                        totalProb = float(bigrams[newBigram]) * prob
                    else:
                        totalProb = float(lowestProb) * prob
                    if (otherLower in verbalForms) or (otherLower == verb):
                        otherTag = bigram[0].split('/')[1]
                        print '\t' + otherWord+'/'+otherTag, originalForm+'/'+tag, word, '\t'+str(totalProb)
                    else:
                        print '\t' + otherWord, originalForm+'/'+tag, word, '\t'+str(totalProb)
                    probsPerTag = {}

                    
        else: 
            if match and ((match.group(1) in verbalForms) or (match.group(1) == verb)):
                originalForm = word
                for tag in tags:
                    tagged = verb + '/' + tag
                    bigram = (lastLower, tagged)
                    prob = bigrams.get(bigram)
                    if prob:
                        probsPerTag[bigram] = float(bigrams[bigram])
                    else:
                        probsPerTag[bigram] = float(lowestProb)

        otherWord = lastWord
        lastWord = word

