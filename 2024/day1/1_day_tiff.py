def answer():
    f = open("1.1_daytxt.txt", "r")
    data = f.read()
    result = 0
    [col1, col2] = clean_data(data)
    col1.sort()
    col2.sort()
    for i in range(len(col1)):
        result = result + abs(col1[i] - col2[i])
    print(result)
    f.close()


def clean_data(data):
    rows = data.strip().split("\n")

    column1 = []
    column2 = []

    for row in rows:
        col1, col2 = map(int, row.strip().split())
        column1.append(col1)
        column2.append(col2)

    return column1, column2


answer()
