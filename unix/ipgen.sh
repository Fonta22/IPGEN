#!/bin/sh

if [ "$1" = "-s" ]; then
    py saveip.py $1
else
    py createbot.py $1
fi