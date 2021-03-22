#!/bin/sh

function ipgen() {
    if [ "$2" = "-s" ]; then
        python saveip.py $1
    elif [ "$1" = "clear" ]; then
        python saveip.py 0
    else
        python createbot.py $1
    fi
}
