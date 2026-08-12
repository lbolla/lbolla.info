---
title: Netlify
date: 2026-03-28
---
I recently moved [lbolla.info](https://lbolla.info) to [Digital Garden]({{< relref "blog/Digital Garden.md" >}}). The notes are now published and deployed on [Netlify](https;//app.netlify.com). Here are some notes about the whole setup.
## Project
`lbolla.info` is a project in Netlify. The project has a [GitHub repo](https://en.wikipedia.org/wiki/Knowledge_graph) from which it deploys. Staging deploys are possible from the repo branches.
## Plan
The "Personal" plan includes generous traffic and deployments for 9 USD/month. I think this is enough for me. 9 USD/month may seem like a lot, but:
* [Obsidian Publish](https://obsidian.md/publish) goes for 8 USD/month and it's less flexible
- Doesn't require me to maintain my own blogging solution, even if as simple as [Hugo](https://gohugo.io/).
- It's the price of 2 coffees, where I live.
## DNS
Netlify manages DNS records for the `lbolla.info` project. I had to copy over DNS records from AWS Route53 (my previous DNS provider) and amend the nameservers in my domain's registrar.

I forgot to copy over CNAMEs, so I broke email in the process... For posterity, always remember to check DNS records (`MX`, `TXT` and `CNAME`) with `dig`. E.g.:
```
dig @dns1.p05.nsone.net lbolla.info MX
dig @dns1.p05.nsone.net lbolla.info TXT
dig @dns1.p05.nsone.net protonmail2._domainkey.lbolla.info CNAME
...
```

Luckily [ProtonMail](https://mail.proton.me/) warned me of the misconfiguration and I could fix it without downtime.
## Next steps
- Netlify can also act as registrar. I may move `lbolla.info` away from AWS, which is way more complicated for my taste.