import datetime
#baraye zaman va tarikhe daqiq
today_date = datetime.date.today()
def num_counter(num):
    i = 0
    while num > 0:
        num = num // 10
        i = i + 1
    return i
class person:
    #az in class baraye taerif forooshande va moshtari estefadeh mikonim
    def __init__(self, fname, lname, gender, ncode, bday, bmonth, byear, email, phnum, cellnum, address):
        self.fname = fname
        #first name
        self.lname = lname
        #last name
        self.ncode = ncode
        #code melli
        self.email = email
        self.phnum = phnum
        #telephon sabet
        self.address = address

        if gender not in ['male', 'female', 'else', 'prefer not to say']:
            raise ValueError("you have entered an invalid gender")
        self.__gender = gender
        #jensiyat fard
        if int(bday) < 1 or int(bday) > 31:
            raise ValueError("invalid day")
        self.__bday = bday
        #rooze tavalod (ba tarikh tavalod eshtebah nashavad)
        if int(bmonth) < 1 or int(bmonth) > 12:
            raise ValueError("invalid month")
        self.__bmonth = bmonth
        #mahe tavalod
        if int(byear) > int(today_date.year) or int(byear) < 1900:
            raise ValueError("the age you entered is not valid")
        self.__byear = byear
        #sale tavalod
        if num_counter(int(cellnum)) != 11:
            raise ValueError
        self.__cellnum = cellnum
        #shomare mobile

        class kala:
            # in class baraye estefade dar foroshgah va safhe sefareshat ast
            def __init__(self, kalname, kalprice, kalcode, kalline, kalscore, kalstock):
                self.kalname = kalname
                # name kala
                self.kalprice = kalprice
                # gheymat kala
                self.kalcode = kalcode
                # code kala dar foroshgah
                self.kalline = kalline
                # noe kala (dar dastebandi mahsolat)
                self.kalscore = kalscore
                # emteaz kala
                self.kalstock = kalstock
                # mojodi kala
