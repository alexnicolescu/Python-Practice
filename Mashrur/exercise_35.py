import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


def get_birthdays():
    with open("birth.json", "r") as f:
        return json.load(f)


def get_month(num):
    months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
              "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
    return months[num]


def extract_month(birthday):
    month = birthday.split('/')[0]
    return get_month(month)


def get_months():
    birthdays = get_birthdays()
    months = [extract_month(birthday) for birthday in birthdays.values()]
    counter = Counter(months)
    return dict(counter.most_common())


months = get_months()
output_file("plot.html")
all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
p = figure(x_range=all_months)
p.vbar(x=list(months.keys()), top=list(months.values()), width=0.5)
show(p)
