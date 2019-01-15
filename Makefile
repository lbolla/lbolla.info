.PHONY: help html style push clean

# Self-documenting Makefile
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

html:  ## Generate html
	emacsclient --eval '(org-publish-project "lbolla.info" t)'

style:  ## Download stylesheets
	curl -s https://gongzhitaao.org/orgcss/org.css -o static/css/org.css

run:  ## Copy html to tmp, where local nginx expects them
	cp -R html/ /tmp/
	xdg-open http://localhost:81/

push:  ## Publish
	rsync -acvz html/ lbolla.info:public2/

clean:  ## Clean html
	rm -rf html/
