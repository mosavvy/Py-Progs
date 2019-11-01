


Cel_Fah = input("Celsius or Fahrenheit? 1 = Celsius, 2 = Fahrenheit")

if Cel_Fah == 1:
	Celsius = input("What is the temperature in Celsius? ") 
	print("Converting to Fahrenheit.. ")
	pause 
	
	Con_Temp = Celsius * 33.8
	print(" The Temperature " + Celsius + " C is " + Con_Temp + " F. ")
else:
	Fahrenheit = input("What is the temperature in Fahrenheit? ")
	print("Converting to Celsius.. ")
	pause
	
	Con_Temp2 = Fahrenheit / 33.8 
	print(" The temperature " + Fahrenheit + " F is " + Con_Temp2 + " C. ")
	
Print("All DONE! Thank you for using our program! -Team 5 ")
