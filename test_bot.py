import praw

r = praw.Reddit(user_agent = "test bot, /u/letsLOVE")
r.login("munx1erbot", "thirdverse")
subreddit = r.get_subreddit("test")

already_replied = []

comments_gen = subreddit.get_comments(limit=10)
for comment in comments_gen:
	if ("critical mass" in comment.body.lower()) and (comment.submission not in already_replied):
		comment.reply("Fuck Critical Mass!" + u'\u2122')
		already_replied.append(comment.submission)
		for i in already_replied:
			print i
