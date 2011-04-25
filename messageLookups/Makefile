DATA:=e-release-start.txt e-release-pages.txt f-release-start.txt f-release-pages.txt master-start.txt master-pages.txt

showreport: report.txt
	@cat $<

report.txt: report.sh $(DATA)
	./$< $@

README.html: README.mkd
	markdown $< > $@

clean:
	$(RM) report.txt README.html
