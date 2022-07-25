class SelectHtmdTwo:
    def htmd_two():
        try:
            i =  float(input("enter number of units in KW for billing demand:"))
            j = int(input("enter contract demand in KW:"))
            k = float(input("enter power factor in percentage(%):"))
            h = float(input("enter night time used unit:"))

            if i < 0:
                raise ValueError       
            
            elif (i > j):
                energy_charges = (i * 285)+ + (i * 0.60) + (i * 4.10)   

            elif (i > 0):
                energy_charges = (i * 225)+ + (i * 0.60) + (i * 4.10)
            
            
            
            

            if k < 0:
                raise ValueError
            elif (k > 100):
                raise ValueError
            elif k <= 90:
                total_amount = (i * 0.03) + energy_charges 
                
            elif (k > 90 and k <= 95):
                total_amount =  (i * 0.0015) + energy_charges
                
            elif (k > 95):
                total_amount =  (i * 0.0027) + energy_charges
                
            
            if h < 0:
                raise ValueError
            elif (h >= 0):
                total = total_amount + (h * 0.30)
                return (f'you have to pay {total}Rs.')

            
        except ValueError:
            return "invalid input!!!!!!!"
#     print(htmd_two())
# SelectHtmdTwo