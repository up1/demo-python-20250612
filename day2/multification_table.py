def generate_data():
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table


def display_table_format(table):
    # https://docs.python.org/3/tutorial/inputoutput.html
    for row in table:
        print(" ".join(f"{num:3}" for num in row)) # f-string


def generate():
    table = generate_data()
    display_table_format(table)


if __name__ == "__main__":
    generate()
