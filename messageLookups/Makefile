showreport: report.txt
	@cat $<

report.txt: report.sh
	./$< $@

clean:
	$(RM) report.txt
