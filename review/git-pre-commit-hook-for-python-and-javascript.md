# git pre-commit hook for python and javascript

- title: git pre-commit hook for python and javascript
- author: lbolla
- category: programming
- tags: git,gjslint,hook,javascript,pep8,pyflakes,python
- summary: 
- post_id: 331
- date: 2011-11-17 22:50:21
- post_date_gmt: 2011-11-17 22:50:21
- comment_status: open
- post_name: git-pre-commit-hook-for-python-and-javascript
- status: publish
- post_type: post

----------------

Following a [recent discussion on HN][1], I decided to share my own [git pre-commit hook][2]. [python] #!/usr/bin/python import os import sys import re import subprocess devnull = open(os.devnull, 'w') def call(cmd): p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE) out, err = p.communicate() return out.decode('utf-8'), err.decode('utf-8') def execute(cmd, silent=False): if silent: params = { 'stdout': devnull, 'stderr': devnull, } else: params = {} retcode = subprocess.call(cmd.split(), **params) return retcode def exists(cmd): return execute('which %s' % cmd, silent=True) == 0 def get_modified(ext): modified = re.compile('^(?:M|A).(?P<name>.*\.%s)' % ext) out, _ = call('git status --porcelain') modifieds = [] for line in out.splitlines(): match = modified.match(line.strip()) if (match): modifieds.append(match.group('name')) return modifieds def output(prg, out, err): print(' * %s:\n%s\n%s' % (prg, out, err)) def die(msg): print(msg) sys.exit(1) def check_python(): has_pep8 = exists('pep8') has_pyflakes = exists('pyflakes') if not (has_pep8 or has_pyflakes): die('Install PEP8 and PyFlakes!') modifieds = get_modified('py') rrcode = 0 for file in modifieds: if has_pep8: out, err = call('pep8 %s' % file) if out or err: output('pep8', out, err) rrcode = rrcode | 1 if has_pyflakes: retcode = execute('pyflakes %s' % file) rrcode = retcode | rrcode if rrcode != 0: sys.exit(rrcode) def check_javascript(): has_jsl = exists('gjslint') if not has_jsl: die('Install Closure-Lint!') modifieds = get_modified('js') rrcode = 0 for file in modifieds: out, err = call('gjslint %s' % file) if out or err: output('gjslint', out, err) rrcode = rrcode | 1 if rrcode != 0: sys.exit(rrcode) def main(): check_python() check_javascript() if __name__ == '__main__': main() [/python] It's a work-in-progress, so you can find the [most updated version here][3]. To use it, just drop it in your `.git/hooks` directory. At every `git commit`, it will run `[pep8][4]` and `[pyflakes][5]` on `.py` files, and `[gjslint][6]` on `.js` files.

   [1]: http://news.ycombinator.com/item?id=3244475
   [2]: http://book.git-scm.com/5_git_hooks.html
   [3]: https://github.com/lbolla/dotfiles/blob/master/githooks/pre-commit
   [4]: http://pypi.python.org/pypi/pep8
   [5]: http://pypi.python.org/pypi/pyflakes/0.5.0
   [6]: http://code.google.com/closure/utilities/docs/linter_howto.html