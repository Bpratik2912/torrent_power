class SelectLev:
    def lev():
        try:
            i =  float(input("enter number of units:"))

            if i < 0:
                raise ValueError       
            elif i >= 0:
                energy_charges = (i * 4.20)
                FIXED_CHARGES = 25
                total_amount = energy_charges + FIXED_CHARGES
                print(f'you have to pay {total_amount}Rs.')
        except ValueError:
            print("invalid input!!!!!!!")
    # print(lev())
SelectLev