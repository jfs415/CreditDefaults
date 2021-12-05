"""
Jon Healy
ISTE470
Summary Statistics
"""

import csv
import json
import os.path

from typing import List

attribute_data = {
    "sex": {
        "male": {
            "default_count": 0,
            "default_percentage": 0
        },
        "female": {
            "default_count": 0,
            "default_percentage": 0
        }
    },
    "education": {
        "graduate_school": {
            "default_count": 0,
            "default_percentage": 0
        },
        "university": {
            "default_count": 0,
            "default_percentage": 0
        },
        "high_school": {
            "default_count": 0,
            "default_percentage": 0
        },
        "other": {
            "default_count": 0,
            "default_percentage": 0
        }
    },
    "marriage": {
        "married": {
            "default_count": 0,
            "default_percentage": 0
        },
        "single": {
            "default_count": 0,
            "default_percentage": 0
        },
        "other": {
            "default_count": 0,
            "default_percentage": 0
        }
    },
    "balance_limit": {
        "10000_24999": {
            "default_count": 0,
            "default_percentage": 0
        },
        "25000_49999": {
            "default_count": 0,
            "default_percentage": 0
        },
        "50000_249999": {
            "default_count": 0,
            "default_percentage": 0
        },
        "250000_1000000": {
            "default_count": 0,
            "default_percentage": 0
        }
    },
    "age": {
        "18_25": {
            "default_count": 0,
            "default_percentage": 0
        },
        "26_39": {
            "default_count": 0,
            "default_percentage": 0
        },
        "40_64": {
            "default_count": 0,
            "default_percentage": 0
        },
        "65_plus": {
            "default_count": 0,
            "default_percentage": 0
        }
    }
}

outlier_count = 0
parsed = []
header = []
def_count = 0


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


def apply_averages():
    for attribute in attribute_data.keys():
        for sub in attribute_data[attribute]:
            attribute_data[attribute][sub]["default_percentage"] = average_default(attribute_data[attribute][sub]["default_count"])


def average_default(count: int):
    return ((count / def_count) * 100) / 5  # Divide by 5 since that the number of attributes we're looking at


def categorize(data: List[str]):  # Separate data into each category
    bal_limit = calculate_bal_limit_key(int(data[1]))
    sex = data[2]
    education = data[3]
    marriage = data[4]
    age = data[5]

    if data[len(data) - 1] in 'yes':
        attribute_data["balance_limit"][bal_limit]["default_count"] += 1
        attribute_data["sex"][sex]["default_count"] += 1
        attribute_data["education"][education]["default_count"] += 1
        attribute_data["marriage"][marriage]["default_count"] += 1
        attribute_data["age"][age]["default_count"] += 1


def write_csv():
    with open(os.getcwd() + os.path.sep + '..' + os.path.sep + 'lib' + os.path.sep + 'NonOutliers.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(parsed)

    csvfile.close()


def process_line(line: str):  # Process each line
    global outlier_count
    global def_count

    data = line.split(',')

    if not is_outlier(data):
        categorize(data)
        parsed.append(data)
        if data[len(data) - 1] in 'yes':
            def_count += 1
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

    # Output
    print(json.dumps(attribute_data, indent=4))

    # Test verification
    # percent = 0
    # for k, v in attribute_data.items():
    #     print(k)
    #     for subK, subV in attribute_data[k].items():
    #         print(subK)
    #         print(json.dumps(subV, indent=4))
    #         percent += subV["default_percentage"]
    #
    # print(round(percent, 2))


if __name__ == '__main__':
    read_file()
