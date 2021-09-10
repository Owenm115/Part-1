week = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0} # Establishes dictionary

total_hours = 0 # initialising variable
bonus = 0 # initialising variable
holiday_days = ['Monday', 'Friday'] # establishing holiday days in a list so they can be recalled


name = input('Employee name: ').lower() # employee name input
position = input('Are you a Manager? (Yes/No) ').lower() # input used in later if statements

for day in week: # loops through elements in the week dictionary
  hours = float(input(f'{day} Hours worked: ')) # float input for hours worked
  if day in holiday_days: # bonus pay depends on holiday days
    holiday = input(f'Is it a holiday? (Yes/No) ').lower()
    if holiday == 'yes':
      bonus = bonus + 4 * week.get('Monday') # retrieves the value of the key monday and adds bonus, not necessary to add to friday because the order of the values don't matter
    else:
      bonus = bonus + 0 * week.get('Monday') # retrieves the value of the key monday and adds no bonus
  total_hours = total_hours + hours # adds hours in loop to total hours variable
  week[day] = hours # changes key value in dictionary according to hours worked

if position == 'yes': # converts hours to payment
  normal_rate = 30 * total_hours # manager payment
else:
  normal_rate = 23 * total_hours # regular payment
  
bonus = bonus + 3 * week.get('Saturday') # bonus for saturday
bonus = bonus + 4 * week.get('Sunday') # bonus for sunday
pay = bonus + normal_rate # gets total pay through the bonus and normal rates

print(f'{name.capitalize()} made ${pay} this week!!!!?') # uses the name variable and prints the amount of pay earned in total.
    

