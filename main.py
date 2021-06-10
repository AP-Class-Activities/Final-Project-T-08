import datetime
# baraye zaman va tarikhe daqiq
today_date = datetime.date.today()
class person:
    # Az in class baraye taerif forooshande va moshtari estefadeh mikonim
    def __init__(self, fname, lname, gender, ncode, bday, bmonth, byear, username, password, email, phnum, cellnum,
                 address):
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
        # name karbari
        # bayad dar file check shavad ke tadakhol nadashteh bashad
        self.__username = username
        # password
        if password.isalpha() == True or password.isdecimal() == True or password.lower() == password or\
                password.upper() == password or len(password) < 8:
            raise ValueError("your password should be a combination of 8 or more capital and small alphabet characters"
                             " and numbers")
        self.__password = password
        # email
        if '@' in email == False:
            raise ValueError("invalid email")
        self.__email = email
        # shomare telephone sabet
        if len(phnum) != 11 or phnum[0] != '0':
            raise ValueError("invalid number")
        self.__phnum = phnum
        # shomare mobile
        if len(cellnum) != 11 or cellnum[0] != '0' or cellnum[1] != '9':
            raise ValueError("invalid number")
        self.__cellnum = cellnum
        # adrese manzel ya mahale kar
        self.__address = address

    # setters and getters
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
    # username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        self.__username = value
    # password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        self.__password = value
    # email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value
    # phnum
    @property
    def phnum(self):
        return self.__phnum
    @phnum.setter
    def phnum(self, value):
        self.__phnum = value
    # cellnum
    @property
    def cellnum(self):
        return self.__cellnum
    @cellnum.setter
    def cellnum(self, value):
        self.__cellnum = value
    # address
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value):
        self.__address = value

class client(person):
    # Az in class baraye moshtari estefadeh mikonim
    def __init__(self, fname, lname, gender, ncode, bday, bmonth, byear, username, password, email, phnum, cellnum,
                 address, id, wallet = 0, fav_list = [], sh_list = [], d_sh_list = []):
        super(client,self).__init__(fname, lname, gender, ncode, bday, bmonth, byear, username, password, email, phnum,\
        cellnum, address)
        # id moshtari
        self.__id = 'CU' + id.zfill(6)
        # kife pool
        self.__wallet = wallet
        # liste kala haye morede alaqe
        self.__fav_list = fav_list
        # list kharid haye dar hale anjam
        self.__sh_list = sh_list
        # list kharid haye anjam shodeh
        self.__d_sh_list = d_sh_list

    # setters and getters
    # id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value
    # wallet
    @property
    def wallet(self):
        return self.__wallet
    @wallet.setter
    def wallet(self, value):
        self.__wallet = value
    # fav_list
    @property
    def fav_list(self):
        return self.__fav_list
    @fav_list.setter
    def fav_list(self, value):
        self.__fav_list = value
    # sh_list
    @property
    def sh_list(self):
        return self.__sh_list
    @sh_list.setter
    def sh_list(self, value):
        self.__sh_list = value
    # d_sh_list
    @property
    def d_sh_list(self):
        return self.__d_sh_list
    @d_sh_list.setter
    def d_sh_list(self, value):
        self.__d_sh_list = value

        
class seller(person):
    # Az in class baraye forooshandeh estefade mikonim
    def __init__(self, fname, lname, gender, ncode, bday, bmonth, byear, email, phnum, cellnum, address, id, wallet = None):
        super(seller, self).__init__(fname, lname, gender, ncode, bday, bmonth, byear, email, phnum, cellnum, address)
        self.id = id
        #id forooshandeh
        self.wallet = wallet
        # kif pool frooshandeh

class kala:
    # in class baraye estefade dar foroshgah va safhe sefareshat ast
    def __init__(self ,kalname ,kalprice ,kalcode , kalline, kalscore, kalstock, comment = []):
        self.__kalname = kalname
        # name kala
        self.__kalprice = kalprice
        # gheymat kala
        self.__kalcode = 'PR' + kalcode.zfill(6)
        # code kala dar foroshgah
        self.__kalline = kalline
        # noe kala (dar dastebandi mahsolat)
        self.__kalscore = kalscore
        # emteaz kala
        self.__kalstock = kalstock
        # mojodi kala
        self.__comment = comment
        # nazarate moshtariyan
    # setter and getter
    # kalname
    "kalname property"
    @property
    def name(self):
        return self.__kalname
    @name.setter
    def name(self , kalname):
        self.__kalname = kalname

    # kalprice
    "kalprice property"
    @property
    def price(self):
        return self.__kalprice
    @price.setter
    def price(self , kalprice):
        self.__kalprice = kalprice

    # kalcode
    "kalcode property"
    @property
    def code(self):
       return self.__kalcode
    @code.setter
    def code(self , kalcode):
       self.__kalcode = kalcode

    # kalline
    "kalline property"
    @property
    def line(self):
        return self.__kalline
    @line.setter
    def line(self , kalline):
        self.__kalline = kalline

    # kalscor
    "kalscor property"
    @property
    def score(self):
        return self.__kalscore
    @score.setter
    def score(self , kalscore):
        self.__kalscore = kalscore

    # kalstock
    "kalstock property"
    @property
    def stock(self):
        return self.__kalstock
    @stock.setter
    def stock(self , kalstock):
        self.__kalstock = kalstock
    # comment
    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, value):
        self.__comment = value


class operatur:
    def __init__(self ,opname , oppass , opcell ):
        self.__opname = 'op'+str(opname).zfill(6)
        # username opratur
        self.__oppass = oppass
        # password operatur
        self.__opcell = opcell
        #shomare operatur

    # setter and getter
    # opname
    "opname property"
    @property
    def pname(self):
        return self.__opname
    @pname.setter
    def pname(self , opname):
        self.opname = opname


    # oppass
    "oppass property"
    @property
    def ppass(self):
        return self.__oppass
    @ppass.setter
    def ppass(self , oppass):
        self.__oppass = oppass


    # opcell
    "opcel property"
    @property
    def pcell(self):
        return self.__opcell
    @pcell.setter
    def pcell(self , opcell):
        self.__opcell = opcell





class karname_mali:
    #in class baraye estefade dar amar foroshande va amar panel operatur ast
    def __init__(self , sood , daramad , tedadsefaresh):
        self.__sood = sood
        self.__daramad = daramad
        self.__tedadsefaresh = tedadsefaresh


    #setter and getter
    "sood property"
    @property
    def sood(self):
        return self.__sood

    @sood.setter
    def sood(self , ksood):
        self.__sood = ksood

    "daramad property"
    @property
    def daramad(self):
        return self.__daramad

    @daramad.setter
    def daramad(self , kdaramad):
        self.__daramad = kdaramad

    "tedadsefaresh property"
    @property
    def tsefaresh(self):
        return self.__tedadsefaresh

    @tsefaresh.setter
    def tsefaresh(self , ktsefaresh ):
        self.__tedadsefaresh = ktsefaresh

