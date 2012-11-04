# Auto add reviewers in Gerrit

- author: lbolla
- category: programming
- tags: gerrit, javascript, git
- summary: Trick to add reviewers to Gerrit automatically
- date: 2012-08-01 11:04:21

----------------

If you are using [Gerrit][1] for code review and project management of
git-based projects, you might find yourself manually adding the same bunch of
reviewers to your patches every single time.

In the past, I alleviated the
problem with a simple Javascript bookmarklet: add it to your browser and
click it while watching the patch in Gerrit.

<script src="https://gist.github.com/1303423.js?file=add_reviewer_bookmarklet.js"></script>

But there's a better method: do it
from command line, when pushing your local commits to Gerrit. Just add these
lines to your `.git/config`:

    pushurl = ssh://user@gerrit:29418/project
    push = HEAD:refs/for/master
    receivepack = git receive-pack --reviewer reviewer1 --reviewer reviewer2

Now, when you want to push a review, just do: `git push review` and "reviewer1"
and "reviewer2" will be added to your patchset.

   [1]: http://code.google.com/p/gerrit/ (Gerrit)
