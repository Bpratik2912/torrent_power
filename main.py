from methods.one_RGP import SelectRgp
from methods.two_GLP import SelectGlp
from methods.three_Non_RGP import SelectNonGlp
from methods.four_LTP import SelectLtp
from methods.five_LTMD1 import SelectLtmdOne
from methods.six_LTMD2 import SelectLtmdTwo
from methods.seven_SL import SelectSl
from methods.eight_LEV import SelectLev
from methods.nine_TMP import SelectTmp
from methods.ten_HTMD1 import SelectHtmdOne
from methods.eleven_HTMD2 import SelectHtmdTwo
from methods.twelve_HTMD3 import SelectHtmdThree
from methods.thirteen_EV import SelectEv
from methods.fourteen_HTMD import SelectHtmd



method = {'1' : SelectRgp ,'2' : SelectGlp,'3' : SelectNonGlp,'4' : SelectLtp,'5' : SelectLtmdOne,'6' : SelectLtmdTwo,'7' : SelectSl,'8' : SelectLev,'9' : SelectLev,'10' : SelectHtmdOne,
'11': SelectHtmdTwo,'12' : SelectHtmdThree,'13' : SelectEv,'14' : SelectHtmd}

i = int(input("enter a method number"))
for i in method:
    print(method.values(i))

