import re
from os.path import dirname, join

key_regex = re.compile(r'<!-- \$(?P<key>\w+) -->', re.M)
key_value_regex = re.compile(r'<!-- \$(?P<key>\w+) = (?P<value>.*) -->',
                             re.M)
import_regex = re.compile(r'^<!-- @import (?P<value>.*) -->$', re.M)


def convert(filename):
    with open(filename) as fobj:
        content = fobj.read()

    import_find = import_regex.findall(content)
    layout_filename = join(dirname(filename), import_find[0])

    with open(layout_filename) as fobj:
        layout = fobj.read()

    context = dict(key_value_regex.findall(content))

    results = key_regex.sub(lambda match: context[match.groups()[0]], layout)

    return results
