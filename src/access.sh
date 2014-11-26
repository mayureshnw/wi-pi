#!/bin/bash
curl "https://api.att.com/oauth/token" \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --header "Accept: application/json" \
    --data "client_id=<add client id>" \
    --request POST
