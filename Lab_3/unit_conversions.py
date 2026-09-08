# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ruby Johnson
#               Iris Hernandez
#               Oliver Brumley
#               John Leach
# Section:      559
# Assignment:   Lab 3 (Team)
# Date:         09/07/2026
#-----------------------------------------------------------#

#asking for quantity through input
quantity_asked = float(input("Please enter the quantity to be converted: ")) 

#conversion from pounds(force) to newtons
lbf_to_n = 4.44822 #conversion value
newton_final = quantity_asked*lbf_to_n #multiplying by original input
print(f"{quantity_asked:.2f} pounds force is equivalent to {newton_final:.2f} newtons") #limiting values to 2 decimal places

#conversion from meters to feet
m_to_ft = 3.28084
feet_final = quantity_asked*m_to_ft
print(f"{quantity_asked:.2f} meters is equivalent to {feet_final:.2f} feet")

#conversion from atmospheres to kilopascals
atm_to_kpa = 101.325
kpa_final = quantity_asked*atm_to_kpa
print(f"{quantity_asked:.2f} atmospheres is equivalent to {kpa_final:.2f} kilopascals")

#conversion from watts to BTU per hour
w_to_btu = 3.41214163
btu_final = quantity_asked*w_to_btu
print(f"{quantity_asked:.2f} watts is equivalent to {btu_final:.2f} BTU per hour")

#conversion from liters per second to US gallons per minute
lps_to_gpm = 0.264172052 * 60  #liter to gallons conversion multiplied by second to minute time conversion
gpm_final = quantity_asked*lps_to_gpm
print(f"{quantity_asked:.2f} liters per second is equivalent to {gpm_final:.2f} US gallons per minute")

#conversion from degrees celcius to degrees farenheit
c_to_f = 33.8
fahrenheit_final = quantity_asked*c_to_f
print(f"{quantity_asked:.2f} degrees Celsius is equivalent to {fahrenheit_final:.2f} degrees Fahrenheit")