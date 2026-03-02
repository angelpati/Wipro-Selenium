import openpyxl

def get_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row[:2]
        data.append((username, password))

    return data

