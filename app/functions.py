import os

def parse_csv(file):
    file_list = []
    with open(file, 'r') as f:
        for line in f:
            key, value = line.strip().split(',')
            file_list.append((key, value))
    os.remove(file)
    return file_list

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'csv'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS