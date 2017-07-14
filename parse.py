from bs4 import BeautifulSoup

# Class definition
class ITESMClass:
    def __init__(self, name, code, time_begin,
                 time_end, days, teacher):
        self.name = name
        self.code = code
        self.time_begin = time_begin
        self.time_end = time_end
        self.days = days
        self.teacher = teacher


# Parsing
file1 = open("tablas.htm", 'r', encoding='utf-8')
file2 = file1.read()
soup = BeautifulSoup(file2, 'lxml')
table = soup.find_all('tbody')[2]
rows = table.find_all('tr')
text = ['MA2009','MA1006','F1005','H2001','TC1020','TC2017','TC2018','TC2019']
classes = []
for row in rows:
    cols = row.find_all('td')
    if (cols[3].text.strip() in text):
        name = cols[2].text.strip()
        code = cols[3].text.strip()
        time_begin = cols[9].text.strip()
        time_end = cols[10].text.strip()
        days = cols[11].text.strip()
        teacher = cols[14].text.strip()
        classes.append(ITESMClass(name, code, time_begin, time_end, days,
                                  teacher))

classes = sorted(classes, key=lambda course: course.time_end)
for course in classes:
    print(course.name)
