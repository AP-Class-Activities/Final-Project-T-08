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
    def __init__(self, fname, lname, gender, ncode, bday, bmonth, byear, username, password, email, phnum, cellnum, address):
        # first name
        if fname.isalpha() == False:
            raise ValueError("your first name should not contain any number")
        self.__fname = fname
        # last name
        if lname.isalpha() == False:
            raise ValueError("your last name should not contain any number")
        self.__lname = lname
        # jensiyat fard
        if gender not in ['male', 'female', 'else', 'prefer not to say']:
            raise ValueError("you have entered an invalid gender")
        self.__gender = gender
        # code melli
        if ncode.isdecimal() == False:
            raise ValueError("national code should only contain numbers")
        self.__ncode = ncode
        # rooze tavalod (ba tarikh tavalod eshtebah nashavad)
        if int(bday) < 1 or int(bday) > 31:
            raise ValueError("invalid day")
        self.__bday = bday
        # mahe tavalod
        if int(bmonth) < 1 or int(bmonth) > 12:
            raise ValueError("invalid month")
        self.__bmonth = bmonth
        # sale tavalod
        if int(byear) > int(today_date.year) or int(byear) < 1900:
            raise ValueError("the age you entered is not valid")
        self.__byear = byear
        #name karbari
        #bayad dar file check shavad ke tadakhol nadashteh bashad
        self.__username = username
        #password
        self.__password = password
        # email
        if '@' in email == False:
            raise ValueError("invalid email")
        self.__email = email
        # shomare telephone sabet
        if num_counter((int(phnum))) != 11 and phnum[0] !='0':
            raise ValueError("invalid number")
        self.__phnum = phnum
        # shomare mobile
        if num_counter(int(cellnum)) != 11 and cellnum[0] != '0' and cellnum[1] != '9':
            raise ValueError("invalid number")
        self.__cellnum = cellnum
        # adrese manzel ya mahale kar
        self.__address = address

    #setters and getters
    # fname
    @property
    def fname(self):
        return self.__fname.title()
    @fname.setter
    def fname(self, value):
        self.__fname = value
    # lname
    @property
    def lname(self):
        return self.__lname.title()
    @lname.setter
    def lname(self, value):
        self.__lname = value
    # gender
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, value):
        self.__gender = value
    # ncode
    @property
    def ncode(self):
        return self.__ncode
    @ncode.setter
    def ncode(self, value):
        self.__ncode = value
    # bday
    @property
    def bday(self):
        return self.__bday
    @bday.setter
    def bday(self, value):
        self.__bday = value
    # bmonth
    @property
    def bmonth(self):
        return self.__bmonth
    @bmonth.setter
    def bmonth(self, value):
        self.__bmonth = value
    # byear
    @property
    def byear(self):
        return self.__byear
    @byear.setter
    def byear(self, value):
        self.__byear = value
    #username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        self.__username = value
    #password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        self.__password = value
    #email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value
    #phnum
    @property
    def phnum(self):
        return self.__phnum
    @phnum.setter
    def phnum(self, value):
        self.__phnum = value
    #cellnum
    @property
    def cellnum(self):
        return self.__cellnum
    @cellnum.setter
    def cellnum(self, value):
        self.__cellnum = value
    #address
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value):
        self.__address = value
        
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
