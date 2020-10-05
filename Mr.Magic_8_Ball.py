# All Imports
import random

#Giving The User Information
print('Hello, I am Mr.Magic 8 Ball, I Can Tell You If Something\nWill Happen Or Not.\n')

# Taking The Quesion From The User
qU = input('What Would You Like To Know:\n\n')

# Specifying The List Of Possible Predictions
pP = ['As I see it, yes',
'Ask again later',
 'Better not tell you now',
 'Cannot predict now',
 'Concentrate and ask again',
 'Don’t count on it',
 'It is certain',
 'It is decidedly so',
 'Most likely',
 'My reply is no',
 'My sources say no',
 'Outlook not so good',
 'Outlook good',
 'Reply hazy, try again',
 'Signs point to yes',
 'Very doubtful',
 'Without a doubt',
 'Yes',
 'Yes – definitely',
 'You may rely on it']
 
# Randomising The And Printing One Of The Prediction
aP = random.choice(pP)
 
# Giving The User The Prediction
print('')
print(aP, end = '\n')

# End Note
print('\nDo Come Again')
