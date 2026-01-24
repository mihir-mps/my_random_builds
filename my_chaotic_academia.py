import webbrowser as wb

def main():
    voldemort()
    rickroll()
    caution()
    hidden_artist()

def voldemort():
    url = "https://www.youtube.com/shorts/JSbuBRIGnL4"
    wb.open(url)
 
def rickroll():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    wb.open(url)

def caution():
    x = 0
    while True:
        print(x)
        x += 1

def hidden_artist():
    n = int(input("number: "))
    for i in range(n):
        print("|#|" * i)

if __name__ == "__main__":
    main()