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
        self.cellnum = cellnum
        #shomare mobil
        self.address = address

        if gender not in ['male', 'female', 'else', 'prefer not to say']:
            raise ValueError("you have entered an invalid gender")
        self.__gender = gender
        #jensiyat fard
        if bday < 1 or bday > 31:
            raise ValueError("invalid day")
        self.__bday = bday
        #rooze tavalod (ba tarikh tavalod eshtebah nashavad)
        if bmonth < 1 or bmonth > 12:
            raise ValueError("invalid month")
        self.__bmonth = bmonth
        #mahe tavalod
        if byear > today_date.year or byear < 1900:
            raise ValueError("the age you entered is not valid")
        self.__byear = byear
        #sale tavalod
        
