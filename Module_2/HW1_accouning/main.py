from application import salary
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    salary.calculate_salary()
    get_employees()
    print(datetime.now().date())
