#!/bin/bash
curl "https://api.att.com/speech/v3/speechToText" \
    --header "Authorization: Bearer <Add authorization code>" \
    --header "Accept: application/json" \
    --header "Content-Type: audio/x-wav" \
    --data-binary @'/home/mayuresh/Desktop/wipivoice/rec.wav' \
    --request POST
