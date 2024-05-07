import datetime

from aplication.salary import calculate_salary
from aplication.db.people import get_employees
import datetime
import zipfile

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.date.today())


