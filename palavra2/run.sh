#!/bin/bash

#sed -Ee 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])/\1 - \2/g' -e 's/[a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ]+(-[a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ]+)?(\/[0-9]{2})/aprender\2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' < corpus.txt > palavra2Anotado.txt

sed -Ee 's/([\.,?!:;"()])/ \1 /g' -e 's/([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])-([^a-zA-ZáàãéóíõâôêÁÀÃÉÓÍÕÂÊÔ])/\1 - \2/g' -e 's/ +/ /g' -e 's/\. \. \./\.\.\./g' < corpus.txt > palavra2Anotado.txt

python cenas.py > palavra2Bigramas.txt
