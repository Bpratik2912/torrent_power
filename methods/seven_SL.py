class SelectSl:
    def sl():
        try:
            i =  float(input("enter number of units:"))

            if i < 0:
                raise ValueError       
            elif i >= 0:
                energy_charges = (i * 4.30)
                print(f'you have to pay {energy_charges}Rs.')
        except ValueError:
            print("invalid input!!!!!!!")
#     print(sl())
SelectSl