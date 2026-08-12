---
title: gio in cronjob
date: 2020-12-14
tags:
- programming
---
[gio](https://developer.gnome.org/gio/stable/gio.html) provides a nice API to deal with VFS. I am using it to mount a NAS harddrive to use for backups.

The problem is that using it from cronjobs is not straightfoward. I got the following errors when trying to run `gio info` and `gio mount` from a cronjob:

```
gio: smb://internetbox-nas.local/philips%20ufd/: Operation not supported
gio: smb://internetbox-nas.local/philips%20ufd/: volume doesn’t implement mount
```

I didn\'t find the right answer in Google, so I am sharing it here in case someone else is affected.

The culprit is that cronjobs run in a very limited environment, and `gio` requires some environmental variables to be set. So, just add these to your cronjob:

```
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
```

Adapt the `user_id` to fit your needs, `id -u` may be helpful, too.
