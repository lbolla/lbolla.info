.PHONY: help post book article serve clean

# Self-documenting Makefile
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

post:  ## Create a new blog post
	@read -p "Enter post title (slug format, e.g., my-first-post): " SLUG; \
	hugo new "blog/$$SLUG.md"

book:  ## Create a new book
	@read -p "Enter book title (slug format, e.g., dune): " SLUG; \
	hugo new --kind book "reading/$$SLUG.md"

article:  ## Create a new article
	@read -p "Enter article title (slug format, e.g., dune): " SLUG; \
	hugo new --kind article "reading/$$SLUG.md"

serve:  ## Serve
	hugo server -D

clean:  ## Clean
	rm -rf public/
