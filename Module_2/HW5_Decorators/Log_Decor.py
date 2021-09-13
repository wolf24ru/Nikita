from datetime import datetime
from pathlib import Path


def log_function(old_function):
    def new_function(*arg, **kwarg):
        time_naw = datetime.now()
        result = old_function(*arg, **kwarg)
        name_function = old_function.__name__
        file = ('log_file.txt')
        path_to_file = Path(Path(file).cwd(), file)
        all_information = f'- {time_naw}, {name_function}, {arg}, {kwarg}, {result}, {path_to_file}\n'
        with open(file, 'a') as f:
            f.write(all_information)
        return result

    return new_function


@log_function
def compound_interest(percentage, years, amount):
    total_amount = (1 + percentage / 100)**years * amount
    return f'Итоговая ссума по вкладу {total_amount:.2f}'


if __name__ == '__main__':
    result = compound_interest(8, 10, 50000)
    print(result)
