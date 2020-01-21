import string

# converts file into a list of strings
def create_data_list(data_file : string) -> list:
    o_file = open(data_file, 'r')
    data_list = []
    for line_str in o_file:
        data_list.append(line_str.strip().split(','))
    return data_list


def monthly_averages(data_list : list) -> list:
    monthly_average = {}

    for i in range(len(data_list)):
        try:
            y, m, d = data_list[i][0].split("-")
            y = int(y)
            m = int(m)
            d = int(d)
        except:
            print("Data format wrong!")

        if (y, m) in monthly_average.keys():
            monthly_average[(y, m)][0] += float(data_list[i][5]) * float(data_list[i][6])
            monthly_average[(y, m)][1] += float(data_list[i][5])
        else:
            monthly_average[(y, m)] = []
            monthly_average[(y, m)].append(float(data_list[i][5]) * float(data_list[i][6]))
            monthly_average[(y, m)].append(float(data_list[i][5]))

    # Append tuple of results in a list
    # Tuples are like (average, year, month).
    # Final average needs to be calculated since it only contains the numerator and denominator
    monthly_average_list = []
    for (y, m), value in monthly_average.items():
        average = value[0] / value[1]
        monthly_average_list.append((average, y, m))

    # Sorting first by descending average. In case of ties sort by year and then month
    monthly_average_list.sort(reverse=True)


def print_info(monthly_averages_list : list) -> None:
    """ Prints sorted list of 6 best and 6 worst average (2 decimals) by months in the format:
                 Six best months
            Average    Year       Month
            ----       ----       -----
                    Six worst months
            Average    Year       Month
            ----       ----       -----
    """
    print('{:^33s}'.format('Six best months'))
    print('{:11s}{:11s}{:11s}'.format('Average', 'Year', 'Month'))
    # Print six best months assuming list is ordered in descending order
    for i in range(6):
        average, year, month = monthly_averages_list[i]
        print('{:<11.2f}{:<11d}{:<2d}'.format(average, year, month))

    print()
    print('{:^33s}'.format('Six worst months'))
    print('{:11s}{:11s}{:11s}'.format('Average', 'Year', 'Month'))
    # Print six worst months assuming list is ordered in descending order
    for i in range(1, 7):
        average, year, month = monthly_averages_list[-i]
        print('{:<11.2f}{:<11d}{:<2d}'.format(average, year, month))


def main():
    data_list = create_data_list("GOOG.csv")
    monthly_averages_list = monthly_averages(data_list)
    print_info(monthly_averages_list)


main()
