month_conversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


# print(month_conversions[1])
# print(month_conversions.get(2))
# print(month_conversions.get("Luv", "This is an invalid key"))

# print(2 ** 4)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


# print(raise_to_power(2, 5))


number_grid_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [float(input("Enter your number: "))]
]

# print(number_grid_2d[3][0])
for row in number_grid_2d:
    for column in row:
        print(column)
