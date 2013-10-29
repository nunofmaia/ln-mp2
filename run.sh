#!/bin/bash

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' -e 's/\/ \?/\/\?/g' < palavra1/corpus.txt > palavra1/palavra1Anotado.txt

python cenas.py  palavra1/palavra1Anotado.txt palavra1/palavra1Ambiguidade.txt  > palavra1/palavra1Bigramas.txt

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' < palavra1/corpus_input.txt > palavra1/palavra1InputAnotado.txt

python program.py palavra1/palavra1Bigramas.txt palavra1/palavra1Ambiguidade.txt palavra1/palavra1InputAnotado.txt


sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' -e 's/\/ \?/\/\?/g' < palavra2/corpus.txt > palavra2/palavra2Anotado.txt

python cenas.py  palavra2/palavra2Anotado.txt palavra2/palavra2Ambiguidade.txt  > palavra2/palavra2Bigramas.txt

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' < palavra2/corpus_input.txt > palavra2/palavra2InputAnotado.txt

python program.py palavra2/palavra2Bigramas.txt palavra2/palavra2Ambiguidade.txt palavra2/palavra2InputAnotado.txt

