#!/usr/bin/env python

import collections
import os
import sys


STEPS = collections.OrderedDict()
STEPS["%(name)s: Confirm Abstract"] = \
    """Confirm abstract for event.

    Make sure it is what the speaker wants. Ideally has a "what to expect"
    or "what you will walk away with" section"""

STEPS["%(name)s: Set Due Dates in Trello"] = \
    """Set all the due dates for cards related to %(name)s"""

STEPS["%(name)s: Publish Event to Facebook"] = \
    """Publish event to Facebook.

    Get people on facebook to say they are going.

    Due: 1 month out.
    """

STEPS["%(name)s: Publish Event to Pougheepsie Journal"] = ""
STEPS["%(name)s: Push Event to Twitter (pinned)"] = ""
STEPS["%(name)s: Put event on HV Tech Happenings (1w)"] = ""
STEPS["%(name)s: Have someone announce at HV Tech"] = ""


def main():
    name = sys.argv[1]
    for k, v in STEPS.items():
        title = k % {"name": name}
        desc = v % {"name": name}
        cmd = ('trello add-card "%s" "%s" -b "MHVLUG Publicity" '
               '-l "Todo For Meeting"' % (title, desc))
        print(cmd)
        os.system(cmd)

if __name__ == "__main__":
    main()
