# Secure GMail Notifier

- author: lbolla
- category: programming
- tags: google
- summary: 
- date: 2007-10-15 13:23:09

----------------

As you might have noticed, [GMail Notifier][1] uses the url
<http://mail.google.com/mail> to access your personal mailbox. This is quite
annoying for who cares about security. Here is a simple hack to make it use the
secure url <https://mail.google.com/mail>. (It works for the Windows version -
for the Mac version there is already a [solution][2]). 

  1. Create a backup copy of gnotifier.exe (usually in c:Program FilesGoogleGmail Notifier);
  2. Open gnotifier.exe with an hex editor (emacs hexl-find-file will do);
  3. Find the string <http://mail.google.com/mail> and substitute it with <https://mail.google.com/mail>;
  4. Save the file;
  5. Close any running GMail Notifier and launch it again.

Yes, it is as simple as that.

   [1]: http://toolbar.google.com/gmail-helper/notifier_windows.html (GMail Notifier)
   [2]: http://www.macosxhints.com/article.php?story=200707030100345
