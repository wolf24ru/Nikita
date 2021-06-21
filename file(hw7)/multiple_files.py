from pathlib import Path

files = [Path('1.txt'), Path('2.txt'), Path('3.txt')]
file_for_write = Path('final_file.txt')

for file in sorted(files, key=lambda text_file: len(text_file.open().readlines())):
    file_for_write.open('a').write(f'\n{str(file)}\n')
    file_for_write.open('a').write(f'{str(len(file.open().readlines()))}\n')
    file_for_write.open('a').write(f'{file.open().read()}\n')


print(file_for_write.open().read())
