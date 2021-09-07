import hashlib
from pathlib import Path


def md5_hash_gen(path_file):
    md5_hash = hashlib.md5()
    with path_file.open() as f:
        line = f.readline()
        while line:
            md5_hash.update(bytes(line, 'utf-8'))
            yield md5_hash.digest()
            line = f.readline()


if __name__ == '__main__':
    path_file = Path('country_links.csv')
    for hash_str in md5_hash_gen(path_file):
        print(hash_str)
