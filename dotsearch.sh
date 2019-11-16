#!/bin/bash
echo -e "1: /etc/passwd\n2: /var/log/messages\n"
read CHOI
if [ $CHOI -eq 1 ]; then
PATHER=/etc/passwd
echo "PATHER=$PATHER"
for x in $(cat $PATHER | cut -d':' -f1 | sort); do for y in "$@"; do if [ "$x" == "$y" ]; then echo -ne "\n$x\n"; else echo -ne "."; fi; done; done; echo -en "\n"
elif [ $CHOI -eq 2 ]; then
PATHER=/var/log/messages
echo "PATHER=$PATHER"
for z in "$@"; do egrep --color=auto $z /var/log/messages; done
else
echo "BAD OPTIONS"
fi
