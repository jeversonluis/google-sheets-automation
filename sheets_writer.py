import gspread
from google.oauth2.service_account import Credentials


def connect_sheet():

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scopes
    )

    client = gspread.authorize(creds)

    sheet = client.open("Bitcoin Automation").sheet1

    return sheet


def write_test():
    sheet = connect_sheet()
    sheet.update("A1", [["Automation working!"]])


write_test()
