# -*- coding: utf-8 -*-
# Не работали русские буквы
import sys
sys.path.append("/Users/a18826700/Library/Python/3.9/lib/python/site-packages")
import requests
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import math
import random
import telebot
from selenium.webdriver.support.ui import WebDriverWait
import requests
import data
bot_api = ''
chat = ''

def send(message):
    bot = telebot.TeleBot(bot_api)
    bot.config['api_key'] = bot_api
    bot.send_message(chat, message)


x = 10

swipe_dislike = '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]'

close_total_tinder = '//*[@id="c1564682258"]/div/div/button[2]'
cl2 = '//*[@id="c1564682258"]/div/div/div[2]/button[2]'

swipe_mobile = '//*[@id="c-690079234"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]'

# driver.get('https://tinder.com')



def timeout_after_action():
    time.sleep(2)

def messaging():
    driver.find_element_by_xpath(xpath_messages).click()
    timeout_after_action()
    items = driver.find_elements_by_class_name('messageListItem')
    lim = 0
    while lim < len(items):
        items[lim].click()
        timeout_after_action()
        text_blocks = driver.find_elements_by_class_name('text')
        i = 0
        already_wrote = False
        while i < len(text_blocks):
            if text_blocks[i].text == mtx_real:
                already_wrote = True
            i += 1
        lim += 1
        if (already_wrote == False):
            driver.find_element_by_tag_name('textarea').send_keys(mtx)

OPTIONS = {
    'error_signals_limit': 30,
    'likes_limit': 10,
    'speed': 2,
    'text_message': 'Привет, приятные фото. :) Напиши телеграм, тут просто очень редко бываю.',
    '_implicitly_wait': 3,
    '_url': 'https://tinder.com',
    '_start_time': datetime.datetime.today()
}

XPATH = {
    '_like_first': '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]',
    '_like_other': '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]',
    '_dislike': '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]',
    '_link_to_messages': '//*[@id="c-690079234"]/div/div[1]/div/aside/nav/div/div/div/div[2]/div/div[2]',
    '_link_to_matches': '//*[@id="c-690079234"]/div/div[1]/div/aside/nav/div/div/div/div[2]/div/div[1]'
}

CLASSNAME = {
    '_message_item': 'messageListItem',
    '_match_item': 'matchListItem',
    '_match_item_text': 'text'
}


class TinderAI(object):
    def __init__(self):
        self.options = OPTIONS
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(self.options['_implicitly_wait'])

        self.likes = 0
        self.dislikes = 0
        self.error_signals = 0
        self.error_logs = []
        self.driver.get(self.options['_url'])

    def init(self):
        # self.start_swiping()
        self.search_key_message()
        self.send_results()

    def search_key_message(self):
        try:
            self.driver.get(self.options['_url'])
            open_matches = self.driver.find_elements_by_class_name(CLASSNAME['_match_item'])
            lim = len(open_matches) - 1
            while lim != 1:
                open_matches[lim].click()
                time.sleep(2)
                text_items = self.driver.find_elements_by_class_name(CLASSNAME['_match_item_text'])
                i = 0
                already_wrote = False
                while i < len(text_items):
                    if text_items[i].text == self.options['text_message']:
                        already_wrote = True
                    i += 1
                lim -= 1
                if (already_wrote == False):
                    self.driver.find_element_by_tag_name('textarea').send_keys(self.options['text_message'] + '\n')
                    time.sleep(2)
                    self.driver.find_element_by_xpath(XPATH['_link_to_matches']).click()
                    time.sleep(2)
        except:
            self.error_logs.append('search_key_message')

    def send_results(self):
        l = 'Likes: ' + str(self.likes) + '\n'
        d = 'Dislikes: ' + str(self.dislikes) + '\n'
        st = 'Session time: ' + str(datetime.datetime.today() - self.options['_start_time']) + '\n'
        logs = 'Error logs: ' + str(self.error_logs) + '\n'
        print(l + d + logs + st)
        send(l + d + logs + st)

    def start_swiping(self):
        self.driver.get(self.options['_url'])
        option_likes_limit = self.options['likes_limit']

        while self.likes < option_likes_limit and option_likes_limit > 0:
            try:
                chance = random.random() < 0.90 + random.random()/10

                if self.likes == 0:
                    el_first_like = self.driver.find_element_by_xpath(XPATH['_like_first'])
                    el_first_like.click()
                    self.likes += 1
                    print('like', self.likes)

                if self.likes > 0:
                    if chance:
                        el_other_like = self.driver.find_element_by_xpath(XPATH['_like_other'])
                        el_other_like.click()
                        self.likes += 1
                        print('like', self.likes)
                    else:
                        el_dislike = self.driver.find_element_by_xpath(XPATH['_dislike'])
                        el_dislike.click()
                        self.dislikes += 1
                        print('dislike', self.dislikes)

                self.error_signals = 0
                time.sleep(self.options['speed'] + random.random())
            except:
                if self.error_signals == self.options['error_signals_limit']:
                    self.error_logs.append('start_swiping')
                    break
                self.error_signals += 1
                self.error_handler()

    def error_handler(self):
        print('error', self.likes)
        self.driver.get(self.options['_url'])
        time.sleep(10)
        try:
            el_first_like = self.driver.find_element_by_xpath(XPATH['_like_first'])
            el_first_like.click()
            self.likes += 1
        except:
            pass

bot = TinderAI()
