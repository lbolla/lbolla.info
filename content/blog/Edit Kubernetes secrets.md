---
title: Edit Kubernetes secrets
date: 2018-01-14
tags:
- programming
- python
---
[Kubernetes](https://kubernetes.io/) secrets are difficult to edit using standard command line tools, like `kubectl`.

When doing `kubectl edit secret my-secret` you are presented with a base64-encoded blob that you have to first decode, in order to edit it and then re-encode before saving the file.

There are various ways to deal with it, but none is user-friendly, in my opinion. Therefore, I wrote [kube-secret-editor](https://github.com/lbolla/kube-secret-editor): a simple Python script to decode and encode secret values on the flight before/after editing.

It\'s used as alternative editor when invoking `kubectl edit`, like this:

``` shell
$> KUBE_EDITOR=/path/to/kube-secret-editor.py kubectl edit secret
```

For simplicity, I have a shell alias, like:

``` shell
alias kedit-secret="KUBE_EDITOR=kube-secret-editor kubectl edit secret"
```
