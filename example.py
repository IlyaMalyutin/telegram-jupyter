import time
from IPython import get_ipython
import requests


def send_tg(mess):
    try:
        bot, chat = 'bot_token', 'int_chat_id'
        url = 'https://api.telegram.org/bot{bot}/sendMessage?chat_id={chat}&text={message}'.format(bot=bot, chat=chat,
                                                                                                   message=mess)
        requests.get(url)
    except requests.exceptions.RequestException as e
        print(e)


class CellEvents:
    def __init__(self, threshold=5, name='jupyter'):
        """
        :param threshold: int, seconds
        :param name: str, name of jupyter notebook
        """
        self.threshold = threshold;
        self.start_time = None;
        self.name = name

    def pre_execute(self):
        if not self.start_time:
            self.start_time = time.time()

    def post_run_cell(self, result):
        if self.start_time and time.time() - self.start_time > self.threshold:
            result = ('Err: ' + str(result.error_in_exec) + '; ' if result.error_in_exec else '') + str(result.result)
            message = result[:2000] + '\n...\n' + result[-2000:] if len(result) > 4000 else result
            send_tg('{} ready!\n'.format(self.name) + message)
        self.start_time = None


sendme = CellEvents(5, 'jupyter_name')
ipython = get_ipython()
ipython.events.register('pre_execute', sendme.pre_execute)
ipython.events.register('post_run_cell', sendme.post_run_cell)
