class SelectHtmdThree:
    def htmd_three():
        try:
            i = float(input("enter number of units in KW for billing demand:"))
            j = int(input("enter contract demand in KW:"))
            k = float(input("enter power factor in percentage(%):"))

            if i < 0:
                raise ValueError
            elif (i < j):
                energy_charges = (i * 25 * 30) + (i * 0.60) + (i * 7.05)
            elif (i > j):
                energy_charges = (i * 30 * 30) + (i * 0.60) + (i * 7.05)

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


SelectHtmdThree
