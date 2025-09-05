import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)


def log_to_sheet(sheet_name, data):
    sheet = client.open("AlgoTradingLogs").worksheet(sheet_name)
    sheet.append_row(data)