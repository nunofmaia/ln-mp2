#!/bin/bash


# PALAVRA 1

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' -e 's/\/ \?/\/\?/g' < palavra1/palavra1Anotado.txt > palavra1/palavra1NOR.txt

python prepare.py  palavra1/palavra1NOR.txt palavra1/palavra1Ambiguidade.txt  > palavra1/palavra1Bigramas.txt

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' < palavra1/corpus_input.txt > palavra1/palavra1Frases.txt

python program.py palavra1/palavra1Bigramas.txt palavra1/palavra1Ambiguidade.txt palavra1/palavra1Frases.txt > palavra1/palavra1Resultado.txt


# PALAVRA 2

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' -e 's/\/ \?/\/\?/g' < palavra2/palavra2Anotado.txt > palavra2/palavra2NOR.txt

python prepare.py  palavra2/palavra2NOR.txt palavra2/palavra2Ambiguidade.txt  > palavra2/palavra2Bigramas.txt

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' < palavra2/corpus_input.txt > palavra2/palavra2Frases.txt

python program.py palavra2/palavra2Bigramas.txt palavra2/palavra2Ambiguidade.txt palavra2/palavra2Frases.txt > palavra2/palavra2Resultado.txt


# PALAVRA 3

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' -e 's/\/ \?/\/\?/g' < palavra3/palavra3Anotado.txt > palavra3/palavra3NOR.txt

python prepare.py  palavra3/palavra3NOR.txt palavra3/palavra3Ambiguidade.txt  > palavra3/palavra3Bigramas.txt

sed -Ee 's/[«»“”]/"/g' -e 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔçÇ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' -e 's/- -/--/g' < palavra3/corpus_input.txt > palavra3/palavra3Frases.txt

python program.py palavra3/palavra3Bigramas.txt palavra3/palavra3Ambiguidade.txt palavra3/palavra3Frases.txt > palavra3/palavra3Resultado.txt

