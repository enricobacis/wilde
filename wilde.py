#!/usr/bin/python -u

from tor import Tor
import scholar
import time
import sys


# fix encoding issues
reload(sys)
sys.setdefaultencoding("utf8")


def getmembers(members_files):
    with open(members_files) as f:
        return [line.strip() for line in f]


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('USAGE: THE FIRST ARGUMENT MUST BE A FILE CONTAINING PROGRAM COMMITTEE MEMBERS, ONE PER LINE')
        return scholar.main()

    conference = sys.argv.pop(1)
    print '#', conference.upper()
    print '----------'
    print 'Options: %s\n' % ' '.join(sys.argv[1:])

    with Tor() as tor:

        for member in getmembers(conference):
            print "##", member

            tor.renew()
            time.sleep(5)
            print '----------'
            print '<sub>IP address: %s</sub>\n' % tor.ip()

            sys.argv.extend(('-a', member, '--gfm'))
            scholar.main()
            del sys.argv[-3:]

if __name__ == '__main__':
    main()
