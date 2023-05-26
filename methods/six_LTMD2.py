class SelectLtmdTwo:
    def ltmd_two():
        try:
            i = float(input("enter number of units in KW for billing demand:"))
            j = int(input("enter contract demand in KW:"))
            k = float(input("enter power factor in percentage(%):"))

            if i < 0:
                raise ValueError
            elif (i > j):
                if i <= 50:
                    energy_charges = (i * 425) + (i * 4.80)
                else:
                    energy_charges = (i * 425) + (i * 5.00)
            elif i <= 50:
                energy_charges = (i * 175) + (i * 4.80)
            elif (i > 50 and i <= 80):
                energy_charges = ((50 * 175) + ((i - 50) * 230)) + (i * 5.00)
            elif (i > 80):
                energy_charges = ((50 * 175) + (30 * 230) + ((i - 80) * 300)) + (i * 5.00)

            if k < 0:
                raise ValueError
            elif (k > 100):
                raise ValueError
            elif k <= 90:
                total_amount = (i * 0.03) + energy_charges
                print(f'you have to pay {total_amount}Rs.')
            elif (k > 90 and k <= 95):
                total_amount = (i * 0.0015) + energy_charges
                print(f'you have to pay {total_amount}Rs.')
            elif (k > 95):
                total_amount = (i * 0.0027) + energy_charges
                print(f'you have to pay {total_amount}Rs.')
        except ValueError:
            print("invalid input!!!!!!!")


SelectLtmdTwo
