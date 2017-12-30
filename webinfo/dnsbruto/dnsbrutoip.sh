#!/bin/bash
figlet 29Security
printf "Criado por Joas Antonio e Alex Piccon"
echo
printf "Aguarde....."
echo
for url in $(cat dns.txt);
do
host $url.$1 | grep "has address" | cut -d " " -f4
done
