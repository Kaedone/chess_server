import json


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
