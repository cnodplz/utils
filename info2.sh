#!/bin/bash
RED="\033[0;31m"
BRED="\033[1;31m"
DGREY="\033[1;30m"
GRN="\033[0;32m"
BGRN="\033[1;32m"
BLK="\033[0;30m"
WHT="\033[0;29m"
SUB="${BGRN}\t%s${WHT}"
USER=$(whoami)
DATE=$(date "+%T %F")
OS=$(uname -snr)
LAST=$(last -n1 | grep -v wtmp | tr -s ' ' | cut -d' ' -f"1 2 3 4 5 6 7 8 9 10")
printf "${BRED}[ INFO ]: \t${BRED}$0 @ $(date)\n${BRED}[ USER ]:  $SUB\n${BRED}[ OS   ]:  $SUB\n${BRED}[ DATE ]:  $SUB\n" "$USER" "$OS" "$DATE"
echo -e "${BRED}[ PROC ]:       ${BGRN}daemons enabled ($(systemctl list-unit-files | grep -c enabled))${WHT}"
echo -e "${BRED}[ CPU  ]:      ${BGRN}$(cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d':' -f2)${WHT}"
echo -e "${BRED}[ STAT ]: \t${BRED}DONE${WHT}"
