.PHONY: help html style push clean

# Self-documenting Makefile
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

html:  ## Generate html
	emacsclient --eval '(org-publish-project "lbolla.info" t)'

style:  ## Download stylesheets
	curl -s https://gongzhitaao.org/orgcss/org.css -o static/css/org.css

run:  ## Run a local server at port 8000
	cd html && python3 -m http.server

push:  ## Publish to AWS
	aws --profile lbolla s3 sync html/ s3://lbolla.info/ --delete

clean:  ## Clean html
	rm -rf html/
