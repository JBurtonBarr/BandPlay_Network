import Band_Play as bp


prediction = bp.run_model().get_output() #should be a list of lists

band_numbers = [] #this will hold a list of letter values added together
                # if a precise number is not reached we use the band with the closest value

#wrap with protection statuses 
def letter_map(letter_sum):
    sum_hold = letter_sum
    while sum_hold > 26:
        sum_hold = sum_hold/26
        
    #input number to letter mapping here 



the_lineUp = ["ACDC", "Pink", "Joji", "Kermy", "Dappy", "ABBA"]


band = ""
band_list = []


for item1 in prediction: #REMEMBER TO AUTO FILL IF A NUMBER IS NOT PRE N2
    letter_sum = int(item1[0]) * int(item1[1])
    letter_hold = letter_map(letter_sum) #turns int into letter
    band += letter_hold # raw string
    band_list.append(letter_hold) #add letter to list 
    
    
