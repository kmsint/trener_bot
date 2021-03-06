from config import CLIENT_SECRET, GS_DOCUMENT
import pygsheets
from datetime import datetime, timedelta

LIGHT_GREEN_COLOR = (0.7137255, 0.84313726, 0.65882355, 0)


def connect_to_gs(gs_document):
    gc = pygsheets.authorize(service_file = CLIENT_SECRET)
    sh = gc.open(gs_document)
    return sh.sheet1


def get_current_date():
    return datetime.now().strftime('%-d-%m-%Y')

def get_current_time():
    return datetime.now().strftime('%H:%M:%S')


def get_training_by_date(date):
    wks = connect_to_gs(GS_DOCUMENT)
    current_date_cell = wks.find(date)
    if current_date_cell:
        current_training = wks.get_row(current_date_cell[0].row, include_tailing_empty=False)
        return current_training[0], current_training[1:]
    return 'Сегодня тренировки нету'


def get_next_training():
    wks = connect_to_gs(GS_DOCUMENT)
    next_date = datetime.now()
    while True:
        next_date += timedelta(days=1)
        next_date_format = next_date.strftime('%-d-%m-%Y')
        current_date_cell = wks.find(next_date_format)
        if current_date_cell:
            next_training = wks.get_row(current_date_cell[0].row, include_tailing_empty=False)
            return next_training[0], next_training[1:]
    

def get_workouts_left():

    wks = connect_to_gs(GS_DOCUMENT)
    next_training_date = get_next_training()[0]
    training_dict = {}
    all_dates = wks.get_col(1, include_tailing_empty=False)[1:]
    all_dates_left = all_dates[all_dates.index(next_training_date):]
    training_table = wks.get_all_values(returnas='matrix', majdim='ROWS', include_tailing_empty=False, include_tailing_empty_rows=False)[1:]

    for row in training_table:
        if row[0] in all_dates_left:
            for elem in row[1:]:
                quantity, exercise = elem.split()
                if exercise[:3] in training_dict:
                    training_dict[exercise[:3]] += int(quantity)
                else:
                    training_dict[exercise[:3]] = int(quantity)
    
    return training_dict


def get_workouts_done():
    
    wks = connect_to_gs(GS_DOCUMENT)
    next_training_date = get_next_training()[0]
    training_dict = {}
    all_dates = wks.get_col(1, include_tailing_empty=False)[1:]
    all_dates_done = all_dates[:all_dates.index(next_training_date)]
    training_table = wks.get_all_values(returnas='matrix', majdim='ROWS', include_tailing_empty=False, include_tailing_empty_rows=False)[1:]
    
    for row in training_table:
        if row[0] in all_dates_done:
            for elem in row[1:]:
                quantity, exercise = elem.split()
                if exercise[:3] in training_dict:
                    training_dict[exercise[:3]] += int(quantity)
                else:
                    training_dict[exercise[:3]] = int(quantity)

    return training_dict


def format_output(training_dict):
    format_string = ''
    replace_dict = {'отж': 'Отжимания', 
                    'при': 'Приседания',
                    'под': 'Подтягивания'}
    
    for key in training_dict:
        format_string += replace_dict[key] + ': ' + str(training_dict[key]) + '\n'

    return format_string


def format_training_output(training_tuple):
    if training_tuple == 'Сегодня тренировки нету':
        return 'Сегодня тренировки нету'
    training = '\n'.join(training_tuple[1])
    return f'Тренировка {training_tuple[0]}:\n{training}'


def colorize_row_by_date(date):
    wks = connect_to_gs(GS_DOCUMENT)
    current_date_cell = wks.find(date)

    if current_date_cell:
        current_training = wks.get_row(current_date_cell[0].row, returnas='range', include_tailing_empty=False)
        model_cell = pygsheets.Cell(current_date_cell[0].label)
        model_cell.color = LIGHT_GREEN_COLOR
        current_training.apply_format(model_cell, fields="userEnteredFormat.backgroundColor")

#print(format_output(get_workouts_left()))
#colorize_row_by_date('4-02-2022')