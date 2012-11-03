# Errors printing PDFs with CUPS

- title: Errors printing PDFs with CUPS
- author: lbolla
- category: programming
- tags: 
- summary: 
- post_id: 462
- date: 2012-09-13 09:38:57
- post_date_gmt: 2012-09-13 08:38:57
- comment_status: open
- post_name: errors-printing-pdfs-with-cups
- status: publish
- post_type: post

----------------

This is another of those posts _to not forget_. If printing a pdf file with `lp` prints a blank page with error messages like: 

> ERROR: configurationerror OFFENDING COMMAND: setpagedevice STACK: --nostringval-- ...

the problem is probably that your pdf has a certain page size (let's say _letter_) but your printer expects another (let's say _A4_). Check your printer settings and your pdf (with `lpinfo pdffile`) to verify. If this is the case, print with this command instead: [code language="shell"] lp -o fit-to-page pdffile [/code]