# При слишком частых запросах с одного ip можеть быть долгосрочный таймаут

import requests
from datetime import datetime, timedelta

how_many_days = 2
dtime_now = datetime.now()
dtime_days_ago = dtime_now - timedelta(days=how_many_days)
stack_questions_url = 'https://api.stackexchange.com/2.2/questions'
tag = 'python'
questions_dic = {}

for page in range(100):
    params = {
        'fromdate': f'{int(dtime_now.timestamp())}',
        'todate': f'{int(dtime_days_ago.timestamp())}',
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'tagged': tag,
        'page': page}

    questions_request = requests.get(stack_questions_url,
                                     params=params)
    json_reqest = questions_request.json()
    if questions_request.status_code == 200:
        for x in json_reqest.get('items'):
            questions_dic.update({x['question_id']: x['title']})
        if json_reqest['has_more'] == False:
            break
    else:
        print(questions_request)
        break

for title_name in json_reqest.values():
    print(title_name)
