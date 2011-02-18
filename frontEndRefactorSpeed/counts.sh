#!/bin/bash

# This file is part of Mifos Stats - Front End Refactor Speed Report
# (hereafter "counts").
#
# Counts is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Counts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Counts.  If not, see <http://www.gnu.org/licenses/>.

mifosHead=$HOME/git/mifos-head

dates="2010-05-01 2010-05-15 2010-06-01 2010-06-15 2010-07-01 2010-07-15 2010-08-01 2010-08-15 2010-09-01 2010-09-15 2010-10-01 2010-10-15 2010-11-01 2010-11-15 2010-12-01 2010-12-15 2011-01-01 2011-01-15 2011-02-01 2011-02-15"
# column headers
echo -e "Date\t\"Struts/jsp LOC\"\t\"SpringMVC/ftl LOC\""
pushd $mifosHead > /dev/null
for date in $dates
do
    commitAtDate=`git rev-list -n 1 --before=$date origin/master`
    git checkout --quiet $commitAtDate
    git clean -fdx
    strutsJsplines=`find $mifosHead -type f \( -iname '*.jsp' -o -iname '*action.java' \) \! -path "$mifosHead/.git/*" \! -path "*/target*" -print0 | wc --files0-from=- --lines | grep --color=never total$ | sed -e 's/^\([0-9]\+\) .*/\1/'`
    springMvcFtllines=`find $mifosHead -type f \( -iname '*.ftl' -o -iname '*controller.java' \) \! -path "$mifosHead/.git/*" \! -path "*/target*" -print0 | wc --files0-from=- --lines | grep --color=never total$ | sed -e 's/^\([0-9]\+\) .*/\1/'`
    echo -e "$date\t$strutsJsplines\t$springMvcFtllines"
done
popd > /dev/null
