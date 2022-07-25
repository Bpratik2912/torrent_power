class SelectEv:
    def htmd_ev():
        try:
            i =  float(input("enter number of units in KW for billing demand:"))
            j = int(input("enter contract demand in KW:"))
            # k = float(input("enter power factor in percentage(%):"))

            if i < 0:
                raise ValueError       

            elif (i < j):
                energy_charges = (i * 25) + (i * 4.10) 
                print(f'you have to pay {energy_charges}Rs.')  
                
            elif (i > j):
                energy_charges = (i * 50) + (i * 4.10)
                print(f'you have to pay {energy_charges}Rs.')
    
                
        except ValueError:
            print("invalid input!!!!!!!")
    # htmd_ev()
SelectEv