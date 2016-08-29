# encoding: utf-8
"""
Reddit-Mealtime Video bot
"""
from __future__ import division

from pytz import timezone

import datetime
import json
import os
import praw
import pytumblr
import random
import time
import traceback
import logging
import sys
import tumblr

logger = logging.getLogger(__name__)

class Bot(object):
    def __init__(self, **kwargs):
        self.config = kwargs
        logger.info('Initializing')

        # Create reddit agent
        self.reddit = praw.Reddit(user_agent= os.environ['user_agent'])

        self.reddit.login(os.environ['REDDIT_USERNAME'], os.environ['REDDIT_PASSWORD'], disable_warning=True)


if __name__ == '__main__':
    Bot()
