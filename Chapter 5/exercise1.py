# dateconvert2.py
#     Converts day month and year numbers into two date formats
#     Modified using format strings

def main():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
              
    monthStr = months[month-1]

    print("The date is {0}/{1}/{2} or {3} {1}, {2}".format(month, day, year, monthStr))

main()
