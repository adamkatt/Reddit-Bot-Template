# bigwordbot

import praw#you need praw for this reddit bot
# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(
    client_id='', client_secret='', username='', password='',
    user_agent='')  #this last part can be anything
print('Logged in')
subreddit_name = 'scp'  #change the name to the name of the subreddit you want
subreddit = reddit.subreddit(subreddit_name)

keyphrase = '!activate '  # phrase to activate the bot

for comment in subreddit.stream.comments(
):  #this will search for comments in the subreddit, if you would like to search submissions then use 'submissions' instead of 'comments'
    if keyphrase in comment.body:  #this checks if the bot keyphrase is in the comment
        word = comment.body.replace(keyphrase, '').replace(
            ' ', ''
        )  #this will remove the keyphrase, it will also remove any spaces from the leftover comment
        ##
        if word == 'bot':
            comment.reply(
                'the bot has been activated'
            )  #comment.reply is the command to reply to the comment
            print('EURIKA')
        else:
            print('the bot is still inactive')
        ##
        #anything between '##' is where the bulk of your program should go(what i wrote is an example, if you want your bot to be across multiple subs you may use a loop to do so