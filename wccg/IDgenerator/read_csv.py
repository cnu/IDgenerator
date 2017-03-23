from openpyxl import load_workbook
import json


def run():
    wb = load_workbook(filename='rider_details.xlsx', read_only=True)
    ws = wb['Form Responses 1']  # ws is now an IterableWorksheet
    rider_details = []
    rejected = []
    truncated = []
    forbidden = ['(', ')', '.', '_']
    for row in ws.rows:
        rider_uid = row[0].value
        try:
            name = row[2].value + ' ' + row[15].value
        except:
            name = row[2].value
        if name:
            if len(name) > 22:
                first_name = row[2].value
                last_name = row[15].value
                name = first_name
        blood_group = row[3].value
        emergency_name = row[4].value
        emergency_no = row[6].value
        rider_no = row[7].value
        email = row[8].value
        rider = (rider_uid, name, blood_group, emergency_name, str(emergency_no), str(rider_no), email)
        if name is None or blood_group is None or emergency_name is None or emergency_no is None or email is None:
            rejected.append(rider)
        else:
            rider_details.append(rider)

    with open('rider_details.json', 'w') as f:
        json.dump(rider_details, f, indent=1)
    with open('rejected_riders.json', 'w') as f:
        json.dump(rejected, f, indent=1)

if '__name__' == '__main__':
    run()