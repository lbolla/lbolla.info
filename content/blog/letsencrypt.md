---
categories:
  - "programming"
date: "2015-12-04"
description: "Enabled HTTPS using Let's Encrypt"
tags:
  - "tls"
title: "lbolla.info is using HTTPS"
---

Today I have enabled `https` on this website. I am using certificates issued by [Let's Encrypt][1], which is a new free, automated and open certificate authority.

To manage the certificates, I am using [simp_le][2], a simple command line client to issue and renew certificates using [Let's Encrypt][1] API.

All working fine, so far!

  [1]: https://letsencrypt.org/
  [2]: https://github.com/kuba/simp_le/
