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
