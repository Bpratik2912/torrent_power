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
print("1) RGP : Residential General Purpose (UP to and including 15 KW)\n"
      "2) GLP :For Hospitals,Schools & Religious Purpose\n"
      "3) Non-RGP : Low Tension Service for Commercial and Industrial Purpose\n"
      "4) LTP (AG) : Agriculture Service\n"
      "5) LTMD-1 : Low Tension Maximum Demand for Residential Purpose\n"
      "6) LTMD-2 : Low Tension Maximum Demand for other than residential purpose\n"
      "7) SL : Low Tension Tension Street Light Service\n"
      "8) LEV : LT- Electric Vehicle Charging Stations\n"
      "9) TMP : Low Tension Temporary Supply\n"
      "10) HTMD-1 : High Tension Maximum Demand\n"
      "11) HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC\n"
      "12) HTMD-3 : High Tension Maximum Demand Temporary Supply\n"
      "13) EV: HT Electric Vehicle Charging Station\n"
      "14)HTMD : Metro Traction\n")

method = {1: SelectRgp.last, 2: SelectGlp.glp, 3: SelectNonGlp.non_rgp,
          4: SelectLtp.ltp, 5: SelectLtmdOne.ltmd_one, 6: SelectLtmdTwo.ltmd_two,
          7: SelectSl.sl, 8: SelectLev.lev, 9: SelectTmp.tmp, 10: SelectHtmdOne.htmd_one,
          11: SelectHtmdTwo.htmd_two, 12: SelectHtmdThree.htmd_three,
          13: SelectEv.htmd_ev, 14: SelectHtmd.htmd}


def calculate():
    try:
        i = int(input("enter a method number:"))
        if i in method.keys():
            return method[i]()
        else:
            raise ValueError

    except ValueError:
        print("invalid input!!!!")


calculate()
