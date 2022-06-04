from datetime import datetime
today = datetime.now()
print("Current date and Time =",today)
dt = today.strftime("%B%D%Y%H%M%S")
print("Current Date & Time=",dt)