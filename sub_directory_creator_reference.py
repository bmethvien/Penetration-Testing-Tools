base = 'http://10.10.10.10/downloads/'
#example is 2024-12-34-upload.pdf

def months():
    for i in range(1,13):
        if i < 10:
            i = f"0{i}"
            days(i)
        else:
            days(i)

def days(month):
    for i in range(1,32):
        if i < 10:
            i = f"0{i}"
            file = f"2024-{month}-{i}-upload.php"
            print(base + file)
        else:
            file = f"2024-{month}-{i}-upload.php"
            print(base + file)

def main():
    months()

if __name__== "__main__":
    main()
