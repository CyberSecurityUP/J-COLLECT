#!/bin/bash
figlet 29Security
printf "Criado por Joas Antonio e Alex Piccon"
echo
for palavra in $(cat $2)
do
resposta=$(curl -s -o /dev/null -w "%{http_code}" $1/$palavra/)
if [ $resposta == "200" ]
then echo "Diretorio foi encontrado: $palavra"
else echo "Diretorio não encontrado: $palavra"
fi
done
