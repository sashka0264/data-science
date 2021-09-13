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
import requests
import data
bot_api = ''
chat = ''

def send(message):
    bot = telebot.TeleBot(bot_api)
    bot.config['api_key'] = bot_api
    bot.send_message(chat, message)


x = 10

swipe_first = '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]'
swipe = '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]'
swipe_dislike = '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]'

close_total_tinder = '//*[@id="c1564682258"]/div/div/button[2]'
cl2 = '//*[@id="c1564682258"]/div/div/div[2]/button[2]'

swipe_mobile = '//*[@id="c-690079234"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://tinder.com')



def tryCloseAll(i):
    print(i, 'error')
    try:
        driver.find_element_by_xpath(close_total_tinder).click()
        return
    except:
        pass
    try:
        driver.find_element_by_xpath(cl2).click()
        return
    except:
        pass
    try:
        driver.find_element_by_xpath(swipe_first).click()
        return
    except:
        pass
    return


options = {
    'error_max': 30,
    'swipes': 3000,
    'timer_second': 2,
}

def autoLikes(options):
    error_signals_max = options['error_max']
    error_signals = error_signals_max
    i = options['swipes']
    dislikes = 0
    start_time = datetime.datetime.today()
    matches = 0
    swipe_sum = 0
    while i > 0:
        try:
            matches = len(driver.find_elements_by_class_name('matchListItem')) - 2
            if i == options['swipes']:
                print(i)
                driver.find_element_by_xpath(swipe_first).click()
                i -= 1
                swipe_sum += 1
            if i < options['swipes']:
                if (random.random() < 0.90 + random.random()/10):
                    print(i)
                    driver.find_element_by_xpath(swipe).click()
                    i -= 1
                    swipe_sum += 1
                else:
                    print('dislike')
                    driver.find_element_by_xpath(swipe_dislike).click()
                    dislikes = dislikes + 1
            error_signals = error_signals_max
        except:
            error_signals -= 1
            if error_signals == 1:
                driver.get('https://tinder.com/app/recs')
                time.sleep(60)
            if error_signals == 0:
                send('Error...')
                i = 0
            tryCloseAll(i)
        time.sleep(options['timer_second'] + random.random())
    send('Свайпов: ' + str(swipe_sum) + '\nДизлайков: ' + str(dislikes) + '\nИтого открытых матчей: ' + str(matches) + '\nВремя сеанса: ' + str(datetime.datetime.today() - start_time))


