showreport: report.txt
	@cat $<

report.txt: report.sh
	./$< $@

README.html: README.mkd
	markdown $< > $@

clean:
	$(RM) report.txt README.html
