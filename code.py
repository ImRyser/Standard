#entering name
first_name = input("What is your name: ")   
current_age = int(input("What is your age: "))
#age of person
if current_age >= 18: print("You're too old")    
elif current_age <= 5: print("You are too young")  
else:   
 print("You are able to go")   
#printing camp choices
 activities = { "1": ("Cultural immersion", 5, "easy", 800), "2": ("Kayaking and pancakes", 3, "moderate", 400), "3": ("Mountain biking", 4, "difficult", 900), }   
 print("\nAvailable Activities:")   
 for key, value in activities.items():
  print(f"{key}. {value[0]}. This is for {value[1]} days, considered '{value[2]}', and costs ${value[3]}.")   
#users choice of activity
 place = input("Choose the number of your activity: ")   
 if place in activities:   
  activity_name = activities[place][0]  
 print(f"\nYou have chosen {activity_name}.")   
 if place == " ":  
  print("\nInvalid selection. Changing to 'Cultural immersion'.")   
 activity_name = activities["1"][0]   
 activity_cost = activities["1"][3]   
 personal = [current_age, first_name]   
 activity_cost = activities[place][3]   

   
 transport_cost = 0  
 transport_response = input("Would you like transport? (yes/no): ").strip().lower()    
 if transport_response == "yes": transport_cost = 80  



 food_options = ["Standard", "Vegan", "Vegetarian", "None"]   
 print("\nMeal options:")   
 for i, option in enumerate(food_options, 1): print(f"{i}. {option}")   
 food_choice = input("Choose the number of your food option: ")   

 

 if food_choice.isdigit() and 1 <= int(food_choice) <= len(food_options): food_option = food_options[int(food_choice) - 1]   

 

 print(f"\nYou have chosen the {food_option} meal option.")   

 

 if food_choice == 2: food_option = "Vegan"  

 

 if food_choice == 3: food_option = "Vegetarian"  

 

 if food_choice == 4: food_option = "none"  

 

 if food_choice == " ": print("\nInvalid selection. Changing to 'Standard'.")   

 

 total_cost = activity_cost + transport_cost   

 

 print(f"\nTotal cost for {first_name} (Age {current_age}):"f" Activity: {activity_name}"f" Transport:{' Included' if transport_cost > 0 else ' Not included '}"f" Food: {food_option}"f" Total: ${total_cost}") 