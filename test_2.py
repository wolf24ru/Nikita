import requests
url = 'https://sun9-22.userapi.com/impf/OFDOwbNUOFtRXmoPXbv4A1V1to76Hqxh_QlS8Q/SfpUPJ6lG8g.jpg?size=768x1024&quality=96&sign=4c092d745df76b6dfbbb98e374b33f3c&c_uniq_tag=vZGwrIakwSqCHHHeHAR-naDlX5ned-70TdaVb5X5pMg&type=album'
re = requests.get(url, stream=True)
print(re.raw)
# print(re)