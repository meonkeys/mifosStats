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

import copy
import math
import os
import time

measures = ['Struts/jsp LOC', 'SpringMVC/ftl LOC']
steepest = {
    'Struts/jsp LOC': {'size': 0, 'date': ''},
    'SpringMVC/ftl LOC': {'size': 0, 'date': ''},
}

f = open('counts.dat')
f.readline() # ignore 1st line (contains column headers)
last = {}
this = {}
for rawline in f:
    (date, this['Struts/jsp LOC'], this['SpringMVC/ftl LOC']) = \
            rawline.rstrip().split('\t')
    for measure in measures:
        thisMeasure = int(this[measure])
        if last.has_key(measure):
            x = math.fabs(last[measure] - thisMeasure)
            last[measure] = thisMeasure
            if x > steepest[measure]['size']:
                steepest[measure]['size'] = x
                steepest[measure]['date'] = date
        last[measure] = thisMeasure
f.close()

print '<p><img src="counts.png"/></p>\n'
print '<hr/>\n'

for measure in measures:
    prettyDate = time.strftime(\
            '%b %Y', time.strptime(steepest[measure]['date'], '%Y-%m-%d'))
    print '<p>Most dramatic change in %s: <strong>%d</strong> (time period ending %s)</p>\n' %\
        (measure, steepest[measure]['size'], prettyDate)

print '''<p>Assumptions:
<ul>
<li>these data are not useful for estimating speed of future refactoring work</li>
<li>all acceptance tests pass in refactored areas</li>
<li>look &amp; feel of refactored areas is acceptable</li>
</ul>
</p>

<p>Also see this <a
href="http://thread.gmane.org/gmane.comp.finance.mifos.devel/10798">this thread
on the dev list</a> about the usefulness of these measurements.</p>
'''

print '<hr/>\n'
print '<p style="font-size: xx-small;"><a href="https://github.com/meonkeys/mifosStats/tree/master/frontEndRefactorSpeed">code used to generate these stats</a></p>\n'
commitHash = os.popen('git rev-parse HEAD').read().rstrip()
print '<!-- built from commit %s at UNIX time %s -->' % (commitHash, time.time())
