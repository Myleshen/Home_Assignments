for ten_thousand_place in range(1, 10):
    for thousand_place in range(0, 10):
        for hundreds_place in range(0, 10):
            for tens_place in range(0, 10):
                for ones_place in range(1, 10):
                    if (ten_thousand_place * 10000 + thousand_place * 1000 + hundreds_place * 100 + tens_place * 10 + ones_place * 1) * 4 ==  (ones_place * 10000 + tens_place * 1000 + hundreds_place * 100 + thousand_place * 10 + ten_thousand_place * 1):
                        print((ten_thousand_place * 10000 + thousand_place * 1000 + hundreds_place * 100 + tens_place * 10 + ones_place * 1))
