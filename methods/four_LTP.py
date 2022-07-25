class SelectLtp:
    def ltp():
        try:
            i =  float(input("enter number of units:"))
            j = int(input("enter BHP:"))

            if i < 0:
                raise ValueError       
            elif i >= 0:
                energy_charges = (i * 3.40)
            
            
            if j < 0:
                raise ValueError
            elif j >= 0:
                total_amount = (energy_charges + (j*10))
                return (f'you have to pay {total_amount}Rs.')
        except ValueError:
            return "invalid input!!!!!!!"
#     print(ltp())
# SelectLtp