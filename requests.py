import json
import requests


def reset_time(standart_time):
    global player1_timer

    player1_timer = standart_time

    global player2_timer

    player2_timer

    player2_timer = standart_time


def opponent_id(id):
    idshnik = json.dumps(id, sort_keys=True, indent=4)
    return idshnik


def time_trak(lost_time1, lost_time2):
    player1_timer -= lost_time1
    player2_timer -= lost_time2
    times = [player1_timer, player2_timer]
    return times


def get_profile(enemy_id):
    name = requests.get('я хз как это реализовать')  # Вот тут должен быть запрос на клиент с сервака, хз можно ли так
    win_counter = int(requests.get('аналогично'))
    lose_counter = int(requests.get(''))
    prof = {
        "id": enemy_id,
        "player_name": name,
        "player_win": win_counter,
        "player_lose": lose_counter
    }

    y = json.dumps(prof)

    return y
