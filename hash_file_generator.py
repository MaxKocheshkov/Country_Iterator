import hashlib
import glob


def hash_line(path):
    for file_open in path:
        with open(file_open, 'r') as file:
            for output_line in file:
                yield hashlib.md5(output_line.encode()).hexdigest()
            return output_line


if __name__ == '__main__':
    print(hash_line(glob.glob('*.txt')))
    for item in hash_line(glob.glob('*.txt')):
        print(item)
