class SelectHtmdOne:
    def htmd_one():
        try:
            i =  float(input("enter number of units in KW for billing demand:"))
            j = int(input("enter contract demand in KW:"))
            k = float(input("enter power factor in percentage(%):"))
            h = float(input("enter night time used unit:"))

            if i < 0:
                raise ValueError  
            elif (i > j):
                if i <=  300:
                    energy_charges = (i * 385)+(i * 0.80)+(i * 4.55)

                elif (i > 300 and i <= 400):
                    energy_charges = (i * 385)+((i * 0.80)+((i-300) * 1.00))+(i * 4.55)

                elif (i > 400 and i <= 1000):
                    energy_charges = (i * 385)+((i * 0.80)+((i-300) * 1.00))+((i * 4.55)+((i-400) * 4.45))     
            elif i <= 1000:
                if i <=  300:
                    energy_charges = (i * 260)+(i * 0.80)+(i * 4.55)

                elif (i > 300 and i <= 400):
                    energy_charges = (i * 260)+((i * 0.80)+((i-300) * 1.00))+(i * 4.55)

                elif (i > 400 and i <= 1000):
                    energy_charges = (i * 260)+((i * 0.80)+((i-300) * 1.00))+((i * 4.55)+((i-400) * 4.45))
                
            elif (i > 1000):
                energy_charges = ((1000 * 260)+((i-1000) * 335)) + ((i * 0.80)+((i-300) * 1.00))+((i * 4.55)+((i-400) * 4.45))
                        
            

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
    # print(htmd_one())
# SelectHtmdOne