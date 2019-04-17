def bmi_app():
    height = input('How Tall are You? ')
    weight = input ('What is your Weight? ')
    bmi = int(weight)/(int(height)/100)**2
    print('Your BMI is {}'.format(round(bmi,2)))
    if bmi < 18.5:
        print ('You\'d better eat more')
    elif bmi >= 18.5 and bmi <= 24:
        print ('Good Job')
    else:
        print ('You\'d better do some exercises')
    
bmi_app()