
FormatReadme:
	python src/functions/FormatReadme/main.py

org: FormatReadme

commit-reasons:
	git add . && git commit -m 'commit reasons' && git push
