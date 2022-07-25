class SelectTmp:
    def tmp():
        try:
            i =  float(input("enter number of units:"))
            j = int(input("enter KW:"))

            if i < 0:
                raise ValueError       
            elif i >= 0:
                energy_charges = (i * 5.10)
            
            
            if j < 0:
                raise ValueError
            elif j >= 0:
                total_amount = (energy_charges + ((j*25*30)))
                print(f'you have to pay {total_amount}Rs.')
        except ValueError:
            print("invalid input!!!!!!!")
#     print(tmp())
SelectTmp