student_marks = {'Krishna': [67.0, 68.0, 69.0],
                 'Arjun': [70.0, 98.0, 63.0],
                 'Malika': [52.0, 56.0, 60.0]}

query_name = 'Malika'
sum_all_mark = sum(student_marks.get(query_name))
sum_len = len(student_marks.get(query_name))

print(f'{(sum_all_mark / sum_len):.2f}')
