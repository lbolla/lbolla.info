# secure GMail Notifier

- title: secure GMail Notifier
- author: lbolla
- category: programming,tech
- tags: gmail,hack,hex,https,notifier,secure
- summary: 
- post_id: 54
- date: 2007-10-15 13:23:09
- post_date_gmt: 2007-10-15 11:23:09
- comment_status: open
- post_name: secure-gmail-notifier
- status: publish
- post_type: post

----------------

As you might have noticed, [GMail Notifier][1] uses the url <http://mail.google.com/mail> to access your personal mailbox. This is quite annoying for who cares about security. Here is a simple hack to make it use the secure url <https://mail.google.com/mail>. (it works for the Windows version - for the Mac version there is already a [solution][2]). 

  1. create a backup copy of gnotifier.exe (usually in c:Program FilesGoogleGmail Notifier);
  2. open gnotifier.exe with an hex editor (emacs hexl-find-file will do);
  3. find the string <http://mail.google.com/mail> and substitute it with <https://mail.google.com/mail>;
  4. save the file;
  5. close any running GMail Notifier and launch it again.
yes, it is as simple as that.

   [1]: http://toolbar.google.com/gmail-helper/notifier_windows.html (GMail Notifier)
   [2]: http://www.macosxhints.com/article.php?story=200707030100345