---
title: Goodbye Linode, welcome AWS!
date: 2020-12-11
tags:
- programming
---
After many years of service, I decided to move away from [Linode](https://www.linode.com/). Linode has been hosting this website and my backups flawlessly and gave me my first introduction to Cloud computing back when it wasn\'t so widespread.

Since then, many new players have joined the cloud computing space and few big players have come up on top. Amazon AWS is obviously one of them. I decided to go with them over Linode for a couple of reasons.

First, Amazon AWS should be way cheaper for my use cases. Second, moving to AWS gives me an excuse to familiarize with their many offerings.

As a first project, I moved this website over to AWS, using this setup:

1.  Static html files are stored on [S3](https://aws.amazon.com/s3/).
2.  A [Cloudfront](https://aws.amazon.com/cloudfront/) distribution uses the above S3 bucket as origin to serve the files from.
3.  [Route53](https://aws.amazon.com/route53/) provides DNS records for \"lbolla.info\"
4.  [Lambda@Edge](https://aws.amazon.com/lambda/edge/) provides complex routing and rewrite logic for Cloudfront requests.

On top of all the above, monitoring comes for free. Daunting as it seemed at first, all the above technologies are pretty straightforward to use and I like the idea of not having to manage my own `nginx` or renew SSL certificates, etc.
