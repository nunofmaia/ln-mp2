# -*- coding: utf-8 -*- 

import re

unigrams = {}
bigrams = {}
probs = {}

wordsFile = 'palavra2Anotado.txt'
ambiguityFile = 'palavra2Ambiguidade.txt'
lineBeginning = '<s>'

regexp = re.compile('([a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ]+)(-[a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ]+)*/(.+)')

ambiguities = [line.strip() for line in open(ambiguityFile)]
lines = [line.strip() for line in open(wordsFile)]

verb = ambiguities[0]
verbs = []
tags = ambiguities[1].split(' ')
verbalForms = ambiguities[2].split(' ')

unigrams[lineBeginning] = len(lines)

for tag in tags:
    unigram = verb + '/' + tag
    verbs.append(unigram)
    unigrams[unigram] = 0

for line in lines:
    words = line.split(' ')
    lastWord = lineBeginning
    for word in words:
        word = word.lower()
        match = regexp.match(word)
        if match and ((match.group(1) in verbalForms) or (match.group(1) == verb)) and (match.group(3) in tags):
            word = verb + '/' + match.group(3)
            unigrams[word] += 1
        else:
            if word in unigrams:
                unigrams[word] += 1
            else:
                unigrams[word] = 1

        if regexp.match(word) or regexp.match(lastWord):
            bigram = (lastWord, word)
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1

        lastWord = word

for unigram in unigrams:
    for verb in verbs:
        bigramLeft = (verb, unigram)
        bigramRight = (unigram, verb)

        if not bigrams.get(bigramLeft):
            bigrams[bigramLeft] = 0 
        if not bigrams.get(bigramRight):
            bigrams[bigramRight] = 0

for bigram, count in bigrams.iteritems():
    probs[bigram] = (float(count) + 1) / (unigrams[bigram[0]] + len(unigrams.keys()))

for bigram, prob in probs.iteritems():
    print bigram[0], bigram[1] + '\t', prob
