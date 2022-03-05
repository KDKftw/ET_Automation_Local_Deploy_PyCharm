
def returnLocatorForMealHotelKarty(poziceHotelu):
    string1 = "/ html / body / div[ @ id = 'app'] / div[ @ id = 'c_page-mainSearch'] / div[ @class ='hotel-results-section'] / div[@ class ='hotel-results-content'][1] / div[@ class ='tile-hotel-section'] / div[@ class ='items'] / div[@ class ='flex']["
    stringVariable = poziceHotelu
    stringVariable = str(stringVariable)
    string2 = "] / a[@ class ='c_tile-hotel'] / div[@ class ='inner'] / div[@ class ='section-border'] / div[@ class ='c_row'][2] / span[1]"
    finalString = string1 + stringVariable + string2
    finalString = finalString.replace(" ", "")
    print(finalString)
    return str(finalString)


returnLocatorForMealHotelKarty(1)