import os.path
from typing import List

months = {
    '1': {
        'sex': {
            'male': [],
            'female': []
        },
        'education': {
            'graduate_school': [],
            'university': [],
            'high_school': [],
            'other': []
        },
        'marriage': {
            'married': [],
            'single': [],
            'other': []
        },
        'balance_limit': {
            '1000_9999': [],
            '10000_49999': [],
            '50000_249999': [],
            '250000_1000000': []
        },
        'age': {
            '18_25': [],
            '26_39': [],
            '40_64': [],
            '65+': []
        }
    },
    '2': {
        'sex': {
            'male': [],
            'female': []
        },
        'education': {
            'graduate_school': [],
            'university': [],
            'high_school': [],
            'other': []
        },
        'marriage': {
            'married': [],
            'single': [],
            'other': []
        },
        'balance_limit': {
            '1000_9999': [],
            '10000_49999': [],
            '50000_249999': [],
            '250000_1000000': []
        },
        'age': {
            '18_25': [],
            '26_39': [],
            '40_64': [],
            '65+': []
        }
    },
    '3': {
        'sex': {
            'male': [],
            'female': []
        },
        'education': {
            'graduate_school': [],
            'university': [],
            'high_school': [],
            'other': []
        },
        'marriage': {
            'married': [],
            'single': [],
            'other': []
        },
        'balance_limit': {
            '1000_9999': [],
            '10000_49999': [],
            '50000_249999': [],
            '250000_1000000': []
        },
        'age': {
            '18_25': [],
            '26_39': [],
            '40_64': [],
            '65+': []
        }
    },
    '4': {
        'sex': {
            'male': [],
            'female': []
        },
        'education': {
            'graduate_school': [],
            'university': [],
            'high_school': [],
            'other': []
        },
        'marriage': {
            'married': [],
            'single': [],
            'other': []
        },
        'balance_limit': {
            '1000_9999': [],
            '10000_49999': [],
            '50000_249999': [],
            '250000_1000000': []
        },
        'age': {
            '18_25': [],
            '26_39': [],
            '40_64': [],
            '65+': []
        }
    },
    '5': {
        'sex': {
            'male': [],
            'female': []
        },
        'education': {
            'graduate_school': [],
            'university': [],
            'high_school': [],
            'other': []
        },
        'marriage': {
            'married': [],
            'single': [],
            'other': []
        },
        'balance_limit': [],
        'age': {
            '18_25': [],
            '26_39': [],
            '40_64': [],
            '65+': []
        }
    },
    '6': {
        'sex': {
            'male': [],
            'female': []
        },
        'education': {
            'graduate_school': [],
            'university': [],
            'high_school': [],
            'other': []
        },
        'marriage': {
            'married': [],
            'single': [],
            'other': []
        },
        'balance_limit': {
            '1000_9999': [],
            '10000_49999': [],
            '50000_249999': [],
            '250000_1000000': []
        },
        'age': {
            '18_25': [],
            '26_39': [],
            '40_64': [],
            '65+': []
        }
    }
}


def is_outlier(data: List[str]):
    pay_type_count = 0
    for pay_type in (data[6:11]):  # Check if there was no consumption more than 4 times
        if 'no_consumption' in pay_type:
            pay_type_count += 1

    if pay_type_count > 4:
        return True

    bill_count = 0
    for bill in data[12:17]:  # Check if bill was 0 more than 4 times
        if int(bill) == 0:
            bill_count += 1

    pay_count = 0
    for pay in data[18:23]:  # Check if more than 4 payments were also $0
        if int(pay) == 0:
            pay_count += 1

    if bill_count > 4 and pay_count > 4:  # If bill amount and pay amount were $0 more than 4 times it's an outlier
        return True

    return False


def average():  # TODO: Average out data
    print("TODO")


def categorize(data: List[str]):  # TODO: Separate data into each category
    print(data)


def process_line(line: str):  # Process each line
    data = line.split(',')
    if not is_outlier(data):
        categorize(data)


def read_file():
    data = False
    with open(os.getcwd() + os.path.sep + '..' + os.path.sep + 'lib' + os.path.sep + 'out.arff') as file:
        for line in file:
            if '@data' in line:
                data = True
            elif data:
                process_line(line.strip())


if __name__ == '__main__':
    read_file()
