# Auto add reviewers in Gerrit

- title: Auto add reviewers in Gerrit
- author: lbolla
- category: programming
- tags: 
- summary: 
- post_id: 433
- date: 2012-08-01 11:04:21
- post_date_gmt: 2012-08-01 10:04:21
- comment_status: open
- post_name: auto-add-reviewers-in-gerrit
- status: publish
- post_type: post

----------------

If you are using [Gerrit][1] for code review and project management of git-based projects, you might find yourself manually adding the same bunch of reviewers to your patches every single time. In the past, I alleviated the problem with a simple javascript [bookmarklet][2]: add it to your browser and click it while watching the patch in Gerrit. But there's a better method: do it from command line, when pushing your local commits to Gerrit. Just add these lines to your `.git/config`: [code lang="shell"] [remote "review"] pushurl = ssh://user@gerrit:29418/project push = HEAD:refs/for/master receivepack = git receive-pack --reviewer reviewer1 --reviewer reviewer2 [/code] Now, when you want to push a review, just do: [code lang="shell"]git push review[/code] ` and "reviewer1" and "reviewer2" will be added to your patchset.

   [1]: http://code.google.com/p/gerrit/ (Gerrit)
   [2]: https://gist.github.com/1303423