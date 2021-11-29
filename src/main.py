import os.path
from src.credit_instance import CreditInstance
from typing import List

months = {
    1: {
        "sex": {
            "male": [],
            "female": []
        },
        "education": {
            "graduate_school": [],
            "university": [],
            "high_school": [],
            "other": []
        },
        "marriage": {
            "married": [],
            "single": [],
            "other": []
        },
        "balance_limit": {
            "1000_9999": [],
            "10000_49999": [],
            "50000_249999": [],
            "250000_1000000": []
        },
        "age": {
            "18_25": [],
            "26_39": [],
            "40_64": [],
            "65_plus": []
        }
    },
    2: {
        "sex": {
            "male": [],
            "female": []
        },
        "education": {
            "graduate_school": [],
            "university": [],
            "high_school": [],
            "other": []
        },
        "marriage": {
            "married": [],
            "single": [],
            "other": []
        },
        "balance_limit": {
            "1000_9999": [],
            "10000_49999": [],
            "50000_249999": [],
            "250000_1000000": []
        },
        "age": {
            "18_25": [],
            "26_39": [],
            "40_64": [],
            "65_plus": []
        }
    },
    3: {
        "sex": {
            "male": [],
            "female": []
        },
        "education": {
            "graduate_school": [],
            "university": [],
            "high_school": [],
            "other": []
        },
        "marriage": {
            "married": [],
            "single": [],
            "other": []
        },
        "balance_limit": {
            "1000_9999": [],
            "10000_49999": [],
            "50000_249999": [],
            "250000_1000000": []
        },
        "age": {
            "18_25": [],
            "26_39": [],
            "40_64": [],
            "65_plus": []
        }
    },
    4: {
        "sex": {
            "male": [],
            "female": []
        },
        "education": {
            "graduate_school": [],
            "university": [],
            "high_school": [],
            "other": []
        },
        "marriage": {
            "married": [],
            "single": [],
            "other": []
        },
        "balance_limit": {
            "1000_9999": [],
            "10000_49999": [],
            "50000_249999": [],
            "250000_1000000": []
        },
        "age": {
            "18_25": [],
            "26_39": [],
            "40_64": [],
            "65_plus": []
        }
    },
    5: {
        "sex": {
            "male": [],
            "female": []
        },
        "education": {
            "graduate_school": [],
            "university": [],
            "high_school": [],
            "other": []
        },
        "marriage": {
            "married": [],
            "single": [],
            "other": []
        },
        "balance_limit": {
            "1000_9999": [],
            "10000_49999": [],
            "50000_249999": [],
            "250000_1000000": []
        },
        "age": {
            "18_25": [],
            "26_39": [],
            "40_64": [],
            "65_plus": []
        }
    },
    6: {
        "sex": {
            "male": [],
            "female": []
        },
        "education": {
            "graduate_school": [],
            "university": [],
            "high_school": [],
            "other": []
        },
        "marriage": {
            "married": [],
            "single": [],
            "other": []
        },
        "balance_limit": {
            "1000_9999": [],
            "10000_49999": [],
            "50000_249999": [],
            "250000_1000000": []
        },
        "age": {
            "18_25": [],
            "26_39": [],
            "40_64": [],
            "65_plus": []
        }
    }
}


def calculate_bal_limit_key(limit: int):  # Calculates which key the balance limit belongs in
    if 1000 <= limit <= 9999:
        return '1000_9999'
    elif 10000 <= limit <= 49999:
        return '10000_49999'
    elif 50000 <= limit <= 249999:
        return '50000_249999'
    elif 250000 <= limit <= 1000000:
        return '250000_1000000'


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


def apply_category(bal_limit: str, sex: str, education: str, marriage: str, age: str, instance: CreditInstance):
    months[instance.get_month()]["balance_limit"][bal_limit].append(instance)
    months[instance.get_month()]["sex"][sex].append(instance)
    months[instance.get_month()]["education"][education].append(instance)
    months[instance.get_month()]["marriage"][marriage].append(instance)
    months[instance.get_month()]["age"][age].append(instance)


def categorize(data: List[str]):  # Separate data into each category
    bal_limit = calculate_bal_limit_key(int(data[1]))
    sex = data[2]
    education = data[3]
    marriage = data[4]
    age = data[5]
    default = data[len(data) - 1]

    instances = [CreditInstance(1, data[6], int(data[12]), int(data[18]), default),
                 CreditInstance(2, data[7], int(data[13]), int(data[19]), default),
                 CreditInstance(3, data[8], int(data[14]), int(data[20]), default),
                 CreditInstance(4, data[9], int(data[15]), int(data[21]), default),
                 CreditInstance(5, data[10], int(data[16]), int(data[22]), default),
                 CreditInstance(6, data[11], int(data[17]), int(data[23]), default)
                 ]

    for instance in instances:
        apply_category(bal_limit, sex, education, marriage, age, instance)


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
    file.close()

    # Test output
    for i in range(1, 7):
        for instance in months[i]["sex"]["male"]:
            print(instance)


if __name__ == '__main__':
    read_file()
