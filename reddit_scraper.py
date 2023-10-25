import praw

reddit = praw.Reddit(
    client_id='OC26EFyzowDzJUyGJh12YA',
    client_secret='-IMM47ObzZAtHg719nfQo9AaxSjGfQ',
    user_agent='python-web-2023'
)
subreddit = reddit.subreddit("Python")

for submission in subreddit.hot(limit=10):
    print(submission.title)
