"""
Jon Healy
ISTE470
Summary Statistics
"""

import csv
import json
import os.path

from src.credit_instance import CreditInstance
from typing import List

attribute_data = {
    "sex": {
        "male": {
            "data": [],
            "averages": None
        },
        "female": {
            "data": [],
            "averages": None
        }
    },
    "education": {
        "graduate_school": {
            "data": [],
            "averages": None
        },
        "university": {
            "data": [],
            "averages": None
        },
        "high_school": {
            "data": [],
            "averages": None
        },
        "other": {
            "data": [],
            "averages": None
        }
    },
    "marriage": {
        "married": {
            "data": [],
            "averages": None
        },
        "single": {
            "data": [],
            "averages": None
        },
        "other": {
            "data": [],
            "averages": None
        }
    },
    "balance_limit": {
        "10000_24999": {
            "data": [],
            "averages": None
        },
        "25000_49999": {
            "data": [],
            "averages": None
        },
        "50000_249999": {
            "data": [],
            "averages": None
        },
        "250000_1000000": {
            "data": [],
            "averages": None
        }
    },
    "age": {
        "18_25": {
            "data": [],
            "averages": None
        },
        "26_39": {
            "data": [],
            "averages": None
        },
        "40_64": {
            "data": [],
            "averages": None
        },
        "65_plus": {
            "data": [],
            "averages": None
        }
    }
}

outlier_count = 0
parsed = []
header = []


def get_month_averages():
    print("Null")


def average_bill_amount(data: List[CreditInstance]):
    total = 0
    for instance in data:
        total += instance.get_bill_amount()

    return total / (len(data) / 6)


def average_pay_amount(data: List[CreditInstance]):
    total = 0
    for instance in data:
        total += instance.get_pay_amount()

    return total / (len(data) / 6)


def average_pay_type(data: List[CreditInstance]):
    no_consumption = 0
    pay_duly = 0
    revolving_credit = 0
    one_month = 0
    two_months = 0
    three_months = 0
    four_months = 0
    five_months = 0
    six_months = 0
    seven_months = 0
    eight_months = 0
    nine_months = 0
    ten_months_plus = 0

    for instance in data:
        if instance.pay_type in "no_consumption":
            no_consumption += 1
        elif instance.pay_type in "pay_duly":
            pay_duly += 1
        elif instance.pay_type in "revolving_credit":
            revolving_credit += 1
        elif instance.pay_type in "one_month":
            one_month += 1
        elif instance.pay_type in "two_months":
            two_months += 1
        elif instance.pay_type in "three_months":
            three_months += 1
        elif instance.pay_type in "four_months":
            four_months += 1
        elif instance.pay_type in "five_months":
            five_months += 1
        elif instance.pay_type in "six_months":
            six_months += 1
        elif instance.pay_type in "seven_months":
            seven_months += 1
        elif instance.pay_type in "eight_months":
            eight_months += 1
        elif instance.pay_type in "nine_months":
            nine_months += 1
        elif instance.pay_type in "ten_months_plus":
            ten_months_plus += 1

    pay_types = {
        "no_consumption": (no_consumption / (len(data) / 6)),
        "pay_duly": (pay_duly / (len(data) / 6)),
        "revolving_credit": (revolving_credit / (len(data) / 6)),
        "one_month": (one_month / (len(data) / 6)),
        "two_months": (two_months / (len(data) / 6)),
        "three_months": (three_months / (len(data) / 6)),
        "four_months": (four_months / (len(data) / 6)),
        "five_months": (five_months / (len(data) / 6)),
        "six_months": (six_months / (len(data) / 6)),
        "seven_months": (seven_months / (len(data) / 6)),
        "eight_months": (eight_months / (len(data) / 6)),
        "nine_months": (nine_months / (len(data) / 6)),
        "ten_months_plus": (ten_months_plus / (len(data) / 6))
    }

    return pay_types


def average_default(data: List[CreditInstance]):
    default_count = 0
    for instance in data:
        if instance.will_default == 'yes':
            default_count += 1

    defaults = {
        "default_count": (default_count / 6),
        "percentage:": default_count / (len(data) / 6)
    }

    return defaults


def calculate_bal_limit_key(limit: int):  # Calculates which key the balance limit belongs in
    if 10000 <= limit <= 24999:
        return '10000_24999'
    elif 25000 <= limit <= 49999:
        return '25000_49999'
    elif 50000 <= limit <= 249999:
        return '50000_249999'
    elif 250000 <= limit <= 1000000:
        return '250000_1000000'


def is_outlier(data: List[str]):
    pay_type_count = 0
    for pay_type in (data[6:11]):  # Check if there was no consumption more than 3 times
        if 'no_consumption' in pay_type:
            pay_type_count += 1

    if pay_type_count > 3:
        return True

    bill_count = 0
    for bill in data[12:17]:  # Check if bill was 0 more than 3 times
        if int(bill) == 0:
            bill_count += 1
        elif int(bill) > int(data[1]):  # Bill should never exceed limit
            return True
        elif int(bill) < ((int(data[1]) * .4) * -1):  # Check using less than because credit to the customer is shown as a negative balance
            return True  # Amount to be refunded to customer should not be very high ~40%

    pay_count = 0
    for pay in data[18:23]:  # Check if more than 3 payments were $0
        if int(pay) == 0:
            pay_count += 1

    if bill_count > 3 or pay_count > 3:  # If bill amount or pay amount were $0 more than 3 times it's an outlier
        return True

    return False


def calculate_averages(data: List[CreditInstance]):
    bill_amount = average_bill_amount(data)
    pay_amount = average_pay_amount(data)
    default = average_default(data)
    pay_types = average_pay_type(data)

    averages = {
        "pay_type": pay_types,
        "bill_amount": bill_amount,
        "pay_amount": pay_amount,
        "default": default
    }

    return averages


def apply_averages():
    for attribute in attribute_data.keys():
        for sub in attribute_data[attribute]:
            attribute_data[attribute][sub]["averages"] = calculate_averages(attribute_data[attribute][sub]["data"])


def apply_category(bal_limit: str, sex: str, education: str, marriage: str, age: str, instance: CreditInstance):
    attribute_data["balance_limit"][bal_limit]["data"].append(instance)
    attribute_data["sex"][sex]["data"].append(instance)
    attribute_data["education"][education]["data"].append(instance)
    attribute_data["marriage"][marriage]["data"].append(instance)
    attribute_data["age"][age]["data"].append(instance)


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


def write_csv():
    with open(os.getcwd() + os.path.sep + '..' + os.path.sep + 'lib' + os.path.sep + 'NonOutliers.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(parsed)

    csvfile.close()


def process_line(line: str):  # Process each line
    global outlier_count
    data = line.split(',')

    if not is_outlier(data):
        categorize(data)
        parsed.append(data)
    else:
        outlier_count += 1


def read_file():
    data = False
    with open(os.getcwd() + os.path.sep + '..' + os.path.sep + 'lib' + os.path.sep + 'out.arff') as file:
        for line in file:
            if '@data' in line:
                data = True
            elif '@attribute' in line:
                header.append(line.split(" ")[1].strip("'"))
            elif data:
                process_line(line.strip())
    file.close()

    # Uncomment to write csv file with outlier data filtered out
    # write_csv()

    print("There were " + str(outlier_count) + " outliers")
    apply_averages()

    # print(len(attribute_data["age"]["26_39"]["data"]) / 6)
    # for k, v in attribute_data["age"].items():
    #     print(k)
    #     print(json.dumps(v["averages"], indent=4) + "\n")
    # print(json.dumps(attribute_data["age"]["18_25"]["averages"], indent=4))


if __name__ == '__main__':
    read_file()
