import praw
import time

r = praw.Reddit(user_agent = "test bot, /u/letsLOVE")
r.login("munx1erbot", "thirdverse")
subreddit = r.get_subreddit("test")

# Would be nice if already_replied was a text file that persisted even if bot crashed.
already_replied = []

comments_gen = subreddit.get_comments(limit=10)
while True:
	for comment in comments_gen:
		if ("critical mass" in comment.body.lower()) and (comment.submission not in already_replied):
			comment.reply("Fuck Critical Mass!" + u'\u2122')
			already_replied.append(comment.submission)
	time.sleep(60)
