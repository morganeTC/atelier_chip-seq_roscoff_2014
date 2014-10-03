MAKEFILE=makefile
help:
	@grep -P "^\w+:" $(MAKEFILE) | sed 's/://' | sed 's/^/\t/'

pushAll:
	pull
	git add --all
	git commit -m "Updated"
	git push
