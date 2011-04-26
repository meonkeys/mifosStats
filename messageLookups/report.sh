#!/bin/bash
log=$1

echo "Stats run from `date`" > $log

printstats() {
    log=$1
    release=$2
    echo "*** $release ***" >> $log
    echo "lines of SQL logged" >> $log
    wc -l ${release}-start.txt ${release}-pages.txt >> $log
    echo -n "count of ' lookup_value ' (note spaces): " >> $log
    grep -c ' lookup_value ' ${release}-pages.txt >> $log
    echo -n "count of ' lookup_value_locale ': " >> $log
    grep -c ' lookup_value_locale ' ${release}-pages.txt >> $log
    echo -n "number of Connect calls: " >> $log
    grep -c ' Connect	' ${release}-start.txt >> $log
    echo >> $log
}

printstats "$log" "e-release"
printstats "$log" "f-release"
printstats "$log" "master"
