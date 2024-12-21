'''logical oprators = evaluate multiple conditions (or, and, not)
                      or = at  least one condition must be true 
                      and = both cinditions must be true 
                      not = inverse the condition (not false, not true)''' 



'''temp = 25 
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")'''
    
temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT otside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")    
    print("It is CLOUDY")    
elif temp <= 0 and not is_sunny:
    print("It is Cold outside")    
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")        
    print("It is CLOUDY")        