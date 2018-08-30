# telegram + jupyter

Sending message on cell complete.
Sending messages from python code.

For start:
* Create new bot via @BotFather. Get API key like `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw `
* Start conversation with our bot via `\start`
* Get chat_id from `curl https://api.telegram.org/bot{API_key}/getUpdates`

That's all!

Send message from python like:
```
def send_tg(mess):
    bot, chat = 'bot_token', int_chat_id
    url = 'https://api.telegram.org/bot{bot}/sendMessage?chat_id={chat}&text={message}'.format(bot=bot, chat=chat,
                                                                                               message=mess)
    requests.get(url)
```

Or subscribe on jupyter-cell events like in example.py