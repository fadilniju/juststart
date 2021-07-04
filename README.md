### Deploy

###### Simple Way
https://heroku.com/deploy?template=https://github.com/shamilhabeebnelli/juststart

#### Mandatory VARS
`
    BOT_TOKEN = BOT_TOKEN from @botfather
    APP_ID = from telegram ORG scrapper
    API_HASH = from telegram ORG scrapper
    BUTTON1 = first button name
    BUTTONURL1 = first button url
    BUTTON2 = second button name
    BUTTONURL2 = second button url
    BUTTON3 = third button name
    BUTTONURL3 = third button url
    START_MSG = start message
    START_IMG = start image as telegraph
    OWNERID = Owner ID integer
`

#### Host on VPS
`
git clone https://github.com/shamilhabeebnelli/juststart
cd juststart
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m start
