#!/usr/bin/env python3

import sys

from rqt_gui.main import Main

main = Main()
sys.exit(main.main(sys.argv, standalone='esterel_plan_viewer'))
