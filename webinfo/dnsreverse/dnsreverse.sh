#!/bin/bash
figlet 29Security
printf "Criado por Joas Antonio e Alex Piccon"
echo
printf "Aguarde...."
echo
for ip in $(seq 1 254);
do
host $1.$ip
done
