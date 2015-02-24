from datetime import datetime

def add_fuzzy_time():
    '''Display the current time as fuzzy time, e.g. "quarter past six".'''
    hour_str = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
    minute_str = {
            5: 'five past',
            10: 'ten past',
            15: 'quarter past',
            20: 'twenty past',
            25: 'twenty-five past',
            30: 'half past',
            35: 'twenty-five to',
            40: 'twenty to',
            45: 'quarter to',
            50: 'ten to',
            55: 'five to',
    }
    special_case_str = {
            (23, 58): 'round about midnight',
            (23, 59): 'round about midnight',
            (0, 0): 'midnight',
            (0, 1): 'round about midnight',
            (0, 2): 'round about midnight',
            (12, 0): 'noon',
    }

    now = datetime.now()

    try:
        powerline.append(special_case_str[(now.hour, now.minute)], Color.TIME_FG, Color.TIME_BG)
        return
    except KeyError:
        pass

    hour = now.hour
    if now.minute > 32:
        if hour == 23:
            hour = 0
        else:
            hour += 1
    if hour > 11:
        hour = hour - 12
    hour = hour_str[hour]

    minute = int(round(now.minute / 5.0) * 5)
    if minute == 60 or minute == 0:
        powerline.append(' '.join([hour, 'o\'clock']),Color.TIME_FG, Color.TIME_BG )
        return
    else:
        minute = minute_str[minute]
        powerline.append( ' '.join([minute, hour]),Color.TIME_FG, Color.TIME_BG)
        return

add_fuzzy_time()
