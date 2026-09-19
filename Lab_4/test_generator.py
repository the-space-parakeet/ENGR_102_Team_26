
sex_vals = ["M", "F"]
age_vals = list(range(20, 80))
cho_vals = list(range(1, 300))
smo_vals = ["Y", "N"]
hdl_vals = list(range(1, 300))
sbp_vals = list(range(1, 300))
med_vals = ["Y", "N"]



'''
EXAMPLE TEST CASE:
sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
'''

def out_case(outfile, sex, age, cho, smo, hdl, sbp, med, out) -> str:
    outfile.write(f"sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{out}")


def calc_out(sex, age, cho, smo, hdl, sbp, med) -> int:
    points = 0
    # sex
    if (sex == "F"):
        # age
        if   (20 <= age <= 34):
            points -= 7
            # cho
            if  (0 <= cho < 160):
                pass
            elif (160 <= cho <= 199):
                points += 4
            elif (200 <= cho <= 239):
                points += 8
            elif (240 <= cho <= 279):
                points += 11
            else:
                points += 13
            # smo
            if (smo): points += 9

        elif (35 <= age <= 39):
            points -= 3
            # cho
            if  (0 <= cho < 160):
                pass
            elif (160 <= cho <= 199):
                points += 3
            elif (200 <= cho <= 239):
                points += 6
            elif (240 <= cho <= 279):
                points += 8
            else:
                points += 10
            # smo
            if (smo): points += 9

        elif (40 <= age <= 44):
            pass
        elif (45 <= age <= 49):
            points += 3
        elif (50 <= age <= 54):
            points += 6    
        elif (55 <= age <= 59):
            points += 8
        elif (60 <= age <= 64):
            points += 10
        elif (65 <= age <= 69):
            points += 12
        elif (70 <= age <= 74):
            points += 14
        elif (75 <= age <= 79):
            points += 16

            # cho
            if  (0 <= cho < 160):
                pass
            elif (160 <= cho <= 199):
                points +=
            elif (200 <= cho <= 239):
                points += 
            elif (240 <= cho <= 279):
                points +=
            else:
                points +=


    


        
with open("test_cases.txt", "w") as out:
