import os.path

attributes = []
month_averages = {}


def average():  # TODO: Average out data
    print("TODO")


def categorize():  # TODO: Separate data into each category
    print("TODO")


def process_line(line: str):  # TODO: process Each line
    data = line.split(',')
    print(data)


def read_file():
    data = False
    with open(os.getcwd() + os.path.sep + '..' + os.path.sep + 'lib' + os.path.sep + 'out.arff') as file:
        for line in file:
            if '@data' in line:
                data = True
            elif '@attribute' in line:
                attributes.append(line.split(' ')[1].strip("'"))
            elif data:
                process_line(line.strip())
        print(attributes)


if __name__ == '__main__':
    read_file()
