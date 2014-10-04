MAKEFILE=makefile

help:
	@grep -P "^\w+:" $(MAKEFILE) | sed 's/://' | sed 's/^/\t/'


ifdef MAKECMDGOALS
 ifeq ($(MAKECMDGOALS), pushFiles)
  ifeq ($(FILES),)
   $(error FILES variable is undefined. Use: "make pushFiles FILES= /path/f1,/path/f2")
  endif
 endif
endif

comma := ,
FILELIST=$(subst $(comma), , $(FILES))

pushFiles:
	git checkout gh-pages
	git pull
	git add $(FILELIST)
	git commit -m "Updated"
	git push
	#git checkout gh-pages
	#git pull
	#git rebase master
	#git push origin gh-pages
	#git checkout master

