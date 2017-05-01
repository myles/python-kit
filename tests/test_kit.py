from os.path import dirname, join, realpath

import kit

FIXTURES_PATH = join(dirname(realpath(__file__)), 'fixtures')


def test_main():
    good = "<!DOCTYPE html>\n<h1>One <small>(1)</small></h1>\n<p>Lorem ipsum dolor sit amet, consectetur adipiscing.</p>\n"

    results = kit.convert(join(FIXTURES_PATH, 'one.kit'))

    assert results == good
