---
title: Speeding up Oh-my-zsh
date: 2018-05-20
tags:
- programming
---
Today I read a [very interesting article](https://blog.jonlu.ca/posts/speeding-up-zsh) about speeding up [Oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh). So, I tried to profile my own startup times and I discovered that:

-   Zsh start time was about 500ms
-   Bash start time is less than 10ms
-   Zsh (without config) start time is less than 10ms

Most of startup time was spent loading 3 plugins that I regularly use:

-   `emacs`, which provides handy aliases to interact with Emacs daemon. I was surprised this plugin was slow because it just defines a bunch of aliases. It turns out that it was spending 50+ ms checking Emacs\' version (by starting up Emacs every time). I sped it up considerably by instead checking `emacsclient` version. [PR submitted](https://github.com/robbyrussell/oh-my-zsh/issues/6840).
-   `kubectl`, which provides aliases and completion for `kubectl`. It turns out that it was spending 200+ ms to generate the completion script using `kubectl completion zsh` every single time. I sped it up by caching the completion script, that is not subject to change very often. [PR submitted](https://github.com/robbyrussell/oh-my-zsh/pull/6844).
-   `virtualenvwrapper`, which sources `virtualenvwrapper.sh` and little more. Virtualenvwrapper also supports a \"lazy\" version of its script, so I sped up startup times by preferring the \"lazy\" script to the \"eager\" one. [PR submitted](https://github.com/robbyrussell/oh-my-zsh/pull/6842).

I hope the above 3 PRs will be approved and merged!
