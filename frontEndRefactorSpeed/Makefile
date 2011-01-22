report.html: report.py counts.dat
	python $< > $@

counts.png: counts.gpi counts.dat
	gnuplot $<

counts.dat: counts.sh
	bash $< > $@

clean:
	$(RM) counts.png report.html

reallyclean: clean
	$(RM) counts.dat
