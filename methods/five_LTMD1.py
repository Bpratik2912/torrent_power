class SelectLtmdOne:
    def ltmd_one():
        try:
            i =  float(input("enter number of units in KW for billing demand:"))
            j = int(input("enter contract demand in KW:"))
            k = float(input("enter power factor in percentage(%):"))

            if i < 0:
                raise ValueError 
            elif (i > j):
                if i <=  50:
                    energy_charges = (i * 425)+(i * 4.65)
                else:
                    energy_charges = (i * 425)+(i * 4.80)      
            elif i <= 50:
                energy_charges = (i * 150)+(i * 4.65)
                
            elif (i > 50 and i <= 80):
                energy_charges = ((50 * 150)+((i-50) * 185))+(i * 4.80)
                
            elif (i > 80):
                energy_charges = ((50 * 150)+(30 * 185)+((i - 80)*245))+(i * 4.80)
            
            
            

            if k < 0:
                raise ValueError
            elif (k > 100):
                raise ValueError
            elif k <= 90:
                total_amount = (i * 0.03) + energy_charges
                return (f'you have to pay {total_amount}Rs.')
            elif (k > 90 and k <= 95):
                total_amount =  (i * 0.0015) + energy_charges
                return (f'you have to pay {total_amount}Rs.')
            elif (k > 95):
                total_amount =  (i * 0.0027) + energy_charges
                return (f'you have to pay {total_amount}Rs.')

        except ValueError:
            return "invalid input!!!!!!!"
#     print(ltmd_one())
# SelectLtmdOne