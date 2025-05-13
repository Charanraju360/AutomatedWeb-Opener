import webbrowser as wb
number = int(input(print("Enter The Number Of Websites That You Want To Open:")))

for i in range(number):
    url = input("Enter The Website **URL(s)**:\n")

def workAuto():
    path = 'C:/YOUR/BROWSER/PATH/BROWSER_NAME.exe %s'
    wb.get(path).open(url)

workAuto()