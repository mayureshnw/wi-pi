#!/bin/bash

arecord -D plughw:0,0 -f cd -t wav -r 8000 -c 1 -q > /home/mayuresh/Desktop/wipivoice/rec.wav

./speech2text.sh | cut -d\" -f30 > stt.txt

QUESTION=$(cat stt.txt)
echo "Me: " $QUESTION

ANSWER=$(python wolframsearch.py $QUESTION)
echo "Wi-Pi: " $ANSWER

./text2speech.sh $ANSWER
