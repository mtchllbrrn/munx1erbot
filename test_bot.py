# -*- coding: utf-8 -*-
import praw

r = praw.Reddit(user_agent = "test bot, /u/letsLOVE")
already_replied = []
r.login("munx1erbot", "cRypto6pIe1eNgage5sKy")

subreddit = r.get_subreddit("test")

comments_gen = subreddit.get_comments(limit=10)
for comment in comments_gen:
	if "thanks" in comment.body.lower():
		print comment.body
		comment.reply(u'\2122')
