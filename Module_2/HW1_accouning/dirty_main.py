from package.salary import *
from package.db.people import *
from datetime import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now().date())
