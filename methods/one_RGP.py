# power = float(input("enter number to select type of power:"))
# from errno import ENETRESET

class SelectRgp:
    
    def rgp():
        try:

            i =  float(input("enter number of units:"))
            j = int(input("enter type of phase:"))
            if i < 0:
                raise ValueError        
            elif i <= 50:
                energy_charges = (i * 3.20)
            elif (50 < i  and i<= 200):
                energy_charges = ((50*3.20)+((i-50)*3.95))
            elif (i > 200):
                energy_charges = ((50*3.20)+(150*3.95)+((i-200)*5.00))
            
            if j == 1:
                total_amount = (energy_charges + 25)
                return (f'you have to pay {total_amount}Rs.')
            elif j == 3:
                total_amount = (energy_charges + 65)
                return (f'you have to pay {total_amount}Rs.')
            else :
                return ("invalid input!")
        except ValueError:
            return "invalid input!!!!!"

    def bpl():
        
        try:
            i =  float(input("enter number of units:"))
            if i < 0:
                raise ValueError
            elif i <= 50:
                energy_charges = (i * 1.50)
            elif (50 < i  and i<= 200):
                energy_charges = ((50*1.50)+((i-50)*3.95))
            elif (i > 200):
                energy_charges = ((50*1.50)+(150*3.95)+((i-200)*5.00))
            
            total_amount = energy_charges + 5
            return (f'you have to pay {total_amount}Rs.')
        except ValueError:
            return "invalid input!!!!!"
    def last():
        t = int(input("enter type of power:"))
        if t == 1:
            print(SelectRgp.rgp())
        elif t == 2:
            print(SelectRgp.bpl())
        else:
            print("invalid input!")

            

SelectRgp
        




            
        
    
