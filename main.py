import datetime
#baraye zaman va tarikhe daqiq
today_date = datetime.date.today()
class person:
    #az in class baraye taerif forooshande va moshtari estefadeh mikonim
    def __init__(self, fname, lname, ncode, bday, bmonth, byear, email, password, phnum, cellnum, address):
        self.fname = fname
        #first name
        self.lname = lname
        #last name
        self.ncode = ncode
        #code melli
        self.bday = bday
        #rooze tavalod (tvajoh konid ke ba tarikh tavalod farq dare)
        self.bmonth = bmonth
        #mahe tavalod
        self.byear = byear
        #sale tavalod
        self.email = email
        self.password = password
        self.phnum = phnum
        #telephon sabet
        self.cellnum = cellnum
        #shomare mobil
        self.address = address
    @property
    def byear(self):
        return self.__byear
    @byear.setter
    def byear(self, value):
        if int(1900)<int(value)<int(today_date.year):
            self.byear = value
        else:
            print("Invalid age")
