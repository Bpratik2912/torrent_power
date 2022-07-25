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

print("Torrent Power electricity billing")
print("1) RGP : Residential General Purpose (UP to and including 15 KW)\n2) GLP :For Hospitals,Schools & Religious Purpose\n"
      "3) Non-RGP : Low Tension Service for Commercial and Industrial Purpose\n4) LTP (AG) : Agriculture Service\n"
      "5) LTMD-1 : Low Tension Maximum Demand for Residential Purpose\n6) LTMD-2 : Low Tension Maximum Demand for other than residential purpose\n"
      "7) SL : Low Tension Tension Street Light Service\n8) LEV : LT- Electric Vehicle Charging Stations\n"
      "9) TMP : Low Tension Temporary Supply\n10) HTMD-1 : High Tension Maximum Demand\n"
      "11) HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC\n12) HTMD-3 : High Tension Maximum Demand Temporary Supply\n"
      "13) EV: HT Electric Vehicle Charging Station\n14)HTMD : Metro Traction\n")

# method = {1 : SelectRgp.last(), 2 : SelectGlp.glp(), 3 : SelectNonGlp.non_rgp(), 4 : SelectLtp.ltp(), 5 : SelectLtmdOne.ltmd_one(), 6 : SelectLtmdTwo.ltmd_two(), 7 : SelectSl.sl(), 8 : SelectLev.lev(), 9 : SelectLev.lev(), 10 : SelectHtmdOne.htmd_one(),
# 11 : SelectHtmdTwo.htmd_two(), 12 : SelectHtmdThree.htmd_three(), 13 : SelectEv.htmd_ev(),14 : SelectHtmd.htmd()}
# method = {1:'pratik',2:'vatsal',3:'paras' }

# print(method[1])

# for i in method.keys():
#     print(method[i])

i = int(input("enter a method number:"))

try:
    if i == 1:
        SelectRgp.last()
    elif i == 2:
        SelectGlp.glp()
    elif i == 3:
        SelectNonGlp.non_rgp()
    elif i == 4:
        SelectLtp.ltp()
    elif i == 5:
        SelectLtmdOne.ltmd_one()
    elif i == 6:
        SelectLtmdTwo.ltmd_two()
    elif i == 7:
        SelectSl.sl()
    elif i == 8:
        SelectLev.lev()
    elif i == 9:
        SelectTmp.tmp()
    elif i == 10:
        SelectHtmdOne.htmd_one()
    elif i == 11:
        SelectHtmdTwo.htmd_two()
    elif i == 12:
        SelectHtmdThree.htmd_three()
    elif i == 13:
        SelectEv.htmd_ev()
    elif i == 14:
        SelectHtmd.htmd()
    else:
        raise ValueError
        
except ValueError:
    print("invalid input!!!!!!")
