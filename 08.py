
''' ПРИМЕР '''
from datetime import datetime
import locale

data_string = "october 28 2021"
date = datetime.strptime (data_string, "%B %d %Y" )
print(date)

locale.setlocale(locale.LC_ALL, "ru_RU")
print(date.strftime("%c"))
print(date.strftime("%A - %d %B %Y"))
dn1 = date.strftime("%A")
if dn1 in ('суббота', 'воскресенье' ):
    pass
