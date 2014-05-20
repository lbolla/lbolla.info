import os
import StringIO
import sys
import yaml


def convert(fn):
    if not fn.endswith('.md'):
        return False
    with open(fn, 'r') as fd:
        lines = fd.readlines()
        if not lines[0].startswith('#'):
            return False
        title = lines[0].strip('# \n')
        config_lines = []
        while lines:
            line, lines = lines[0], lines[1:]
            if line.startswith('------'):
                break
            config_lines.append(line.strip())
        body = ''.join(lines)

    buff = StringIO.StringIO('\n'.join(config_lines))
    config_yaml = yaml.load(buff)
    config_yaml.append({'title': title})

    new_config = {}
    for item in config_yaml:
        for k, v in item.iteritems():
            if k == 'category':
                new_config['categories'] = [v]
            elif k == 'tags':
                new_config['tags'] = ([t.strip() for t in v.split(',')]
                                      if v else [])
            elif k == 'date':
                new_config['date'] = v.strftime('%Y-%m-%d')
            elif k in ['author']:
                continue
            elif k == 'summary':
                new_config['description'] = v
            else:
                new_config[k] = v

    buff = StringIO.StringIO('\n'.join(config_lines))
    buff.write('---\n')
    for k in sorted(new_config):
        v = new_config[k]
        if isinstance(v, list):
            buff.write('%s:\n' % k)
            for item in v:
                buff.write('  - "%s"\n' % item)
        else:
            buff.write('%s: "%s"\n' % (k, v))
    buff.write('---\n')
    buff.write(body)

    with open(fn, 'w') as fd:
        fd.write(buff.getvalue())

    return True


for root, dir, files in os.walk(sys.argv[1]):
    for file in files:
        fn = os.path.join(root, file)
        try:
            if convert(fn):
                print fn, 'converted.'
            # else:
            #     print fn, 'skipped.'
        except Exception as exc:
                print fn, 'failed:', exc
