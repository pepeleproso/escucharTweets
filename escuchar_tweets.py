# -*- coding: utf-8 -*-

#    This file is part of escucharTweets.
#
#    escucharTweets is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    escucharTweets is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with escucharTweets; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging
logger = logging.getLogger(__name__)
import argparse
import json
import os
import io
import time
import EscucharTweetsMainWindow


parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="count", 
                        help="increase output verbosity (e.g., -vv is more than -v)")
args = parser.parse_args()

debuglevel = logging.WARNING

if args.verbose == 1:
    debuglevel = logging.WARNING
elif args.verbose == 2:
    debuglevel = logging.INFO
elif args.verbose == 3:
    debuglevel = logging.DEBUG

logging.basicConfig(level=debuglevel)

EscucharTweetsMainWindow.EscucharTweetsMainWindow()