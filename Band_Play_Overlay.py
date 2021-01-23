import Band_Play as bp
import webbrowser

#MAKE THIS CASE INSENSITIVE

prediction = bp.run_model().get_output() #should be a list of lists

band_numbers = [] #this will hold a list of letter values added together
                # if a precise number is not reached we use the band with the closest value

#wrap with protection statuses 
def letter_map(letter_sum):
    sum_hold = letter_sum
    while sum_hold > 26:
        sum_hold = sum_hold/26
        
    #input number to letter mapping here 



the_lineUp = {"ACDC":"https://youtu.be/v2AC41dglnM", "Pink":"https://youtu.be/FJfFZqTlWrQ",
              "Joji":"https://youtu.be/K3Qzzggn--s", "Kermy":"https://youtu.be/WS3Lkc6Gzlk",
              "Dappy":"https://youtu.be/WoImizvsj5w", "ABBA":"https://youtu.be/xFrGuyw1V8s"}

lineUp_num = {"ACDC":, "Pink":, "Joji":, "Kermy":, "Dappy":, "ABBA":}
       #ADD letter numerical equivilents


band = ""
band_list = []
code_hold = 0


for item1 in prediction: #REMEMBER TO AUTO FILL IF A NUMBER IS NOT PRE N2
    letter_sum = int(item1[0]) * int(item1[1])
    letter_hold = letter_map(letter_sum) #turns int into letter
    band += letter_hold # raw string
    band_list.append(letter_hold) #add letter to list 
    

if band in the_lineUp:
    song_link = the_lineUp.get(band, default = "https://youtu.be/FxYw0XPEoKE") # default is just a fun error solution
    webbrowser.open(song_link) #try... needs network checks etc
else if band not in the_lineUp:
    for item in band_list:
        letnum = ord(num)
        code_hold += letnum

    #Add code here that goes to nearest band value if value not matched 



    
