class SelectSl:
    def sl():
        try:
            i =  float(input("enter number of units:"))

            if i < 0:
                raise ValueError       
            elif i >= 0:
                energy_charges = (i * 4.30)
                return (f'you have to pay {energy_charges}Rs.')
        except ValueError:
            return "invalid input!!!!!!!"
#     print(sl())
# SelectSl