#!/bin/bash
log=$1

echo "Stats run from `date`" > $log

printstats() {
    log=$1
    release=$2
    echo "*** $release ***" >> $log
    echo "lines of SQL logged" >> $log
    wc -l ${release}-start.txt ${release}-pages.txt >> $log
    echo -n "count of 'from lookup_value ' (note the space): " >> $log
    grep -c 'from lookup_value ' ${release}-pages.txt >> $log
    echo -n "count of 'from lookup_value_locale': " >> $log
    grep -c 'from lookup_value_locale' ${release}-pages.txt >> $log
    echo -n "number of Connect calls: " >> $log
    grep -c ' Connect	' ${release}-start.txt >> $log
    echo >> $log
}

printstats "$log" "e-release"
printstats "$log" "f-release"
printstats "$log" "master"
