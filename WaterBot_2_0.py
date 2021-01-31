# Twitter bot 2.0
# jams286

# import credentials and tweepy
from Api import Api_Key, Api_Key_Secret, Access_Token, Access_Token_Secret
import tweepy
import json
import datetime

# tweet msg
msg = 'Tweet de prueba '

# twitter authentication
auth = tweepy.OAuthHandler(Api_Key, Api_Key_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)

# api
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def randtext():
    ''' enumerate tweets'''
    # open conf.json
    with open('WaterBot2.0/conf.json', 'r') as f:
        conf = json.load(f)
    # reset numeration
    if len(conf['serie2']) > 4:
        conf['serie2'] = '0000'
    # create numeration string
    num = str(int(conf['serie2'])+1).zfill(len(conf['serie2']))
    text = conf['serie1'] + num

    # save file
    with open('WaterBot2.0/conf.json', 'w') as f:
        conf['serie2'] = num
        json.dump(conf, f)

    return " "+text


if __name__ == '__main__':
    try:
        # send tweet
        api.update_status(msg + randtext())
        # save success on log
        with open('WaterBot2.0/logs.txt', 'a') as l:
            current_time = datetime.datetime.now()
            now = current_time.strftime("%d-%m-%y %I:%M:%S")
            l.write("\n"+now+" Success!")
    except Exception as e:
        # save error on log
        with open('WaterBot2.0/logs.txt', 'a') as l:
            current_time = datetime.datetime.now()
            now = current_time.strftime("%d-%m-%y %I:%M:%S")
            l.write("\n"+now+" "+str(e))
