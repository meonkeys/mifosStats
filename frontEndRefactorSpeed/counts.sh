#!/bin/bash

mifosHead=$HOME/git/mifos-head

dates="2010-05-01 2010-05-15 2010-06-01 2010-06-15 2010-07-01 2010-07-15 2010-08-01 2010-08-15 2010-09-01 2010-09-15 2010-10-01 2010-10-15 2010-11-01 2010-11-15 2010-12-01 2010-12-15 2011-01-01 2011-01-15"
# column headers
echo -e "Date\t\"Struts/jsp LOC\"\t\"SpringMVC/ftl LOC\""
pushd $mifosHead > /dev/null
for date in $dates
do
    commitAtDate=`git rev-list -n 1 --before=$date origin/master`
    git checkout --quiet $commitAtDate
    git clean -fdx
    strutsJsplines=`find $mifosHead -type f \( -iname '*.jsp' -o -iname '*action.java' \) \! -path "$mifosHead/.git/*" \! -path "*/target/*" -print0 | wc --files0-from=- --lines | grep --color=never total$ | sed -e 's/^\([0-9]\+\) .*/\1/'`
    springMvcFtllines=`find $mifosHead -type f \( -iname '*.ftl' -o -iname '*controller.java' \) \! -path "$mifosHead/.git/*" \! -path "*/target/*" -print0 | wc --files0-from=- --lines | grep --color=never total$ | sed -e 's/^\([0-9]\+\) .*/\1/'`
    echo -e "$date\t$strutsJsplines\t$springMvcFtllines"
done
popd > /dev/null
