# from distutils.log import error


class SelectGlp:
    def glp():
        try:
            i =  float(input("enter number of units:"))
            j = int(input("enter type of phase:"))

            if i < 0:
                raise ValueError       
            elif i <= 200:
                energy_charges = (i * 4.10)
            elif (i > 200):
                energy_charges = ((200 * 4.10)+((i-200)*4.80))
            
            if j == 1:
                total_amount = (energy_charges + 30)
                return (f'you have to pay {total_amount}Rs.')
            elif j == 3:
                total_amount = (energy_charges + 70)
                return (f'you have to pay {total_amount}Rs.')
            else :
                return ("invalid input!")
        except ValueError:
            return "invalid input!!!!!!"

    print(glp())
# SelectGlp