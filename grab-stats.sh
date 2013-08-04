#!/bin/bash
#
# grab-stats.sh - eat status codes from apache files
tail -f /var/log/challenge/example.log | while read line; do
    code=$(echo "$line" | awk '{print $9}' | tr -d '\n') 
    case "$code" in
        1*) echo "http.status.codes.1xx $code" | nc 127.0.0.1 2003
            ;;
        2*) echo "http.status.codes.2xx $code" | nc 127.0.0.1 2003
            ;;
        3*) echo "http.status.codes.3xx $code" | nc 127.0.0.1 2003
            ;;
        4*) echo "http.status.codes.4xx $code" | nc 127.0.0.1 2003 
            ;;
        5*) echo "http.status.codes.5xx $code" | nc 127.0.0.1 2003
            ;;
    esac
done
