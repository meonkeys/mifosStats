import copy
import math
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

print '<p><img src="counts.png"/></p>'

for measure in measures:
    prettyDate = time.strftime(\
            '%b %Y', time.strptime(steepest[measure]['date'], '%Y-%m-%d'))
    print '<p>Most dramatic change in %s: <strong>%d</strong> (time period ending %s)</p>' %\
        (measure, steepest[measure]['size'], prettyDate)
