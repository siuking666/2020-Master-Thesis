from datetime import datetime as dt
import time

list2 = []
list3 = []

#===========================================

#x = dt.strftime(2020, 1, 1)
#x = dt.date(2020, 1, 1)
#x = date.today()

#convert date code from internet

def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction

#===========================================

#open file

date_file = open("FITS_dates.txt", 'r')

# ".readlines()" reads each line as one string, and stores each string (date) in a list

for each_line in date_file.readlines():
    
# .split("/") will treat / as the separater and further split each date string into 3 strings, stores into date_list

    date_list = each_line.split("/")
    
# day,month,year needs to be integers for decimal conversion code
# this is a "for loop", next entry will overwrite prior entry
    
    day = int(date_list[0])
    month = int(date_list[1])
    year = int(date_list[2].replace("\n", ""))
        
    print (year, ",", month, ",", day)
    
    list2.append(toYearFraction(dt(year, month ,day)))
    
print (list2)

#===========================================

#"open" a file for export
output_date = open("Converted_dates.txt", 'w+')

for item in list2:
    string = str(item)
    list3.append(string)

output_date.write('\n'.join(list3))


#close the file for no reason
date_file.close()   
output_date.close()

