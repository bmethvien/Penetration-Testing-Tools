base = 'http://10.10.10.10/downloads/'
#example is 2024-12-34-upload.pdf

def months():
    for month in range(1,13):
        if month < 10:
            month = f"0{month}"
            days(month)
        else:
            days(month)

def days(month):
    for day in range(1,32):
        if day < 10:
            day = f"0{day}"
            output = f"2024-{month}-{day}-upload.php"
            print(base + output)
        else:
            file = f"2024-{month}-{day}-upload.php"
            print(base + output)

def main():
    months()

if __name__== "__main__":
    main()
