#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

from requests import *

app = Flask(__name__)


# Получение ID соперника
@app.route('/get_id')
def get_id(your_id):
    return opponent_id()


# Обработка времени
@app.route('/time_change')
def timer(lost_time1, lost_time2):
    return time_trak(lost_time1, lost_time2)


# Настройка длительности игры
@app.route('/set_time')
def set_time(stand_time):
    return reset_time(stand_time)


# Просмотр профиля соперника
@app.route('/get_profile/<enemy_id>')
def profile(enemy_id):
    return get_profile(enemy_id)


# Установка и подсчёт рейтинга
@app.route('/get_profile/<enemy_id>/stat')
def stat(enemy_id):
    return get_stat(enemy_id)


client = pymongo.MongoClient(
    "mongodb+srv://Kaedone:<password>@chess.wscna.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)
