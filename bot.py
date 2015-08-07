import praw
import datetime
from time import sleep
from collections import deque

# Read credentials from file
line = open('creds.txt').read().splitlines()
words = line[0].split(':')
my_username = words[0]
bot_password = words[1]
bot_message = words[2]

r = praw.Reddit(user_agent = "munx1erbot, /u/%s" % my_username)
r.login("munx1erbot", bot_password)
subreddit = r.get_subreddit("test")

# Set up our cache and completed work set
comment_cache = deque(maxlen=200)
submission_cache = deque(maxlen=200)

running = True
while running:
    try:
        comments = subreddit.get_comments(limit=10)

        # Check comments 
        for c in comments:

            # Check if we've already scanned this comment or if the comment is from munx1erbot
            if c.id in comment_cache or c.submission.id in submission_cache:
            	continue

            # Add this to our cache
            comment_cache.append(c.id)

            # Check if we need to reply
            if ("critical mass" in c.body.lower()):
                print "found: " + c.body
                c.reply(bot_message)
                submission_cache.append(c.submission.id)

	sleep(15)

    except KeyboardInterrupt:
        running = False
    except Exception as e:
        now = datetime.datetime.now()
        print now.strftime("%m-%d-%Y %H:%M")
        print 'ERROR:', e
        print 'Going to sleep for 30 seconds...\n'
        sleep(30)
        continue
