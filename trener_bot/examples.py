from config import CLIENT_SECRET
import pygsheets

def get_row_by_date(date):
    pass

gc = pygsheets.authorize(service_file = CLIENT_SECRET)
# print(gc)

print(gc.spreadsheet_titles())
# print(gc.spreadsheet_ids()) 

# gc.create('Fucking sheet', template=None, folder=None, folder_name=None)


# # Open spreadsheet and then worksheet
sh = gc.open('Training schedule for 2022')
# sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1DbcKn32KsMthzL311lU_4IP9T5PXvvi6yZMreLnSZng/edit?usp=sharing')
wks = sh.sheet1

header = wks.find('21-01-2022')
print(header)
print(header[0])
print(header[0].col)
print(header[0].row)
print(header[0].color)

cell_color = header[0].color

#header = 

wks.find('31-12-2022')[0].set_value(cell_color).update()
# header[0].set_value(cell_color)

# Update a cell with value (just to let him know values is updated ;) )
# wks.update_value('A1', "Hey yank this numpy array")
# my_nparray = np.random.randint(10, size=(3, 4))

# update the sheet with array
# wks.update_values('A2', my_nparray.tolist())
# for num in range(1, 10):
#     for char in 'ABCDEFGH':
#         wks.update_value(f'{char}{num}', 'Пизда')
# print(wks.get_value('A5'))

# print(wks.get_col(1, include_tailing_empty=False))
print(wks.get_row(161, include_tailing_empty=False))
gray_cell = pygsheets.Cell("A2")
gray_cell.color = (0.9529412, 0.9529412, 0.9529412, 0)
gray_cell.set_text_format("foregroundColor", {"red": 1.0, "green": 0, "blue": 0})
gray_cell.update()
print(gray_cell)

header = wks.cell('A1')
header.value = 'Дата'
header.text_format['bold'] = True # make the header bold
# header.text_format['color'] = (0.7137255, 0.84313726, 0.65882355, 0)
header.color = (0.7137255, 0.84313726, 0.65882355, 0)
header.update()

# print(dir(header))

# gray_cell.apply_format({'backgroundColor':{'red':1}})
# wks.update_value("A1", {"foregroundColor": {"red": 1.0, "green": 0, "blue": 0}})


from datetime import datetime

current_datetime = datetime.now()

print(current_datetime)

dt_string = current_datetime.strftime("%d-%m-%Y")
time_string =  current_datetime.strftime('%H:%M:%S')
print(dt_string)
print(time_string)