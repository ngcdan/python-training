import os

def remove_file(f):
    if os.path.isfile(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f'Error deleting {e.strerror}')
    else:
        print(f'Error deleting file {f}')

remove_file('../files/text.txt')