# Create variable to store the total number of sums
total_number_of_sums = 0
# For at most 200 coins of 1 pence
for pence_1 in range(201):
    # For max number of 2 pence coins
    min_val_1 = pence_1
    max_pence_2 = (200-min_val_1)//2
    for pence_2 in range(max_pence_2+1):
        # For max number of 5 pence coins
        min_val_2 = min_val_1 + pence_2*2
        if(min_val_2>200):
            break
        max_pence_5 = (200-min_val_2)//5
        for pence_5 in range(max_pence_5+1):
            # For max number of 10 pence coins
            min_val_5 = min_val_2 + pence_5*5
            if(min_val_5>200):
                break
            max_pence_10 = (200-min_val_5)//10
            for pence_10 in range(max_pence_10+1):
                # For max number of 20 pence
                min_val_10 = min_val_5 + pence_10*10
                if(min_val_10>200):
                    break
                max_pence_20 = (200-min_val_10)//10
                for pence_20 in range(max_pence_20+1):
                    # For max number of 50 pence
                    min_val_20 = min_val_10 + pence_20*20
                    if(min_val_20>200):
                        break
                    max_pence_50 = (200-min_val_20)//50
                    for pence_50 in range(max_pence_50+1):
                        # For max number of 1 pound
                        min_val_50 = min_val_20 + pence_50*50
                        if(min_val_50>200):
                            break
                        max_pound_1 = (200-min_val_50)//100
                        for pound_1 in range(max_pound_1+1):
                            # For max number of 2 pounds
                            min_val_100 = min_val_50 + pound_1*100
                            if(min_val_100>200):
                                break
                            max_pound_2 = (200-min_val_100)//200
                            for pound_2 in range(max_pound_2 + 1):
                                val = min_val_100+pound_2*200
                                if(val==200):
                                    total_number_of_sums=total_number_of_sums+1
                                    print(total_number_of_sums)

print(total_number_of_sums)