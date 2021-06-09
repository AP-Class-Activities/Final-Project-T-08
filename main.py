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
        if fname.isalph() == False:
            raise ValueError("your first name should not contain any number")
        self.__fname = fname
        #first name
        if lname.isalpha() == False:
            raise ValueError("your last name should not contain any number")
        self.__lname = lname
        #last name
        if gender not in ['male', 'female', 'else', 'prefer not to say']:
            raise ValueError("you have entered an invalid gender")
        self.__gender = gender
        #jensiyat fard
        if ncode.isdecimal() == False:
            raise ValueError("national code should only contain numbers")
        self.__ncode = ncode
        #code melli
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
        if '@' in email == False:
            raise ValueError("invalid email")
        self.__email = email
        #email
        if num_counter((int(phnum))) != 11 and phnum[0] !='0':
            raise ValueError("invalid number")
        self.__phnum = phnum
        #shomare telephone sabet
        if num_counter(int(cellnum)) != 11 and cellnum[0] != '0' and cellnum[1] != '9':
            raise ValueError("invalid number")
        self.__cellnum = cellnum
        #shomare mobile
        self.address = address
        #adrese manzel ya mahale kar

        
class seller(person):
    #Az in class baraye forooshandeh estefade mikonim
    def __init__(self, fname, lname, gender, ncode, bday, bmonth, byear, email, phnum, cellnum, address, id, wallet = None):
        super(seller, self).__init__(fname, lname, gender, ncode, bday, bmonth, byear, email, phnum, cellnum, address)
        self.id = id
        #id forooshandeh
        self.wallet = wallet
        #kif pool frooshandeh

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
