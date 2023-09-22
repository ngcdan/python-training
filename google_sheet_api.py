import gspread
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])

try:
    gc = gspread.authorize(credentials)
    sheet = gc.open('Accounting_T8')
    worksheets = sheet.worksheets()
    for worksheet in worksheets:
        worksheet_name = worksheet.title
        print(f'Trang bảng tính: {worksheet_name}')

        data = worksheet.get_all_values()
        for row in data:
            print(row)

except Exception as e:
    print(f'Error: {str(e)}')

