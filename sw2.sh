#!/bin/bash

VAR1=9

while [ $VAR1 -ne 3 ]; do
    echo -e "0: tail -f /var/log/messages\n1: tcpdump -npi enp0s31f4\n2: QUIT\n3: QUIT"
    read VAR1
    if [ $VAR1 -eq 0 ]; then
        tail -f /var/log/messages | egrep -n --color=auto '^[A-Z][a-z]*\ \ [0-9]*\ [0-9]*\:[0-9]*\:[0-9]*|sudo|audit|uid|auid|systemd'
    elif [ $VAR1 -eq 1 ]; then
        tcpdump -npi enp0s31f6 | egrep -n --color=auto 'ARP|ICMP|ICMP6|IP|IP6'
    elif [ $VAR1 -eq 2 ]; then
        echo "QUIT2"; break
    else
        echo "QUITelse"; break
    fi
done
