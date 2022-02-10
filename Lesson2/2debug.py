seconds = int(input("enter seconds"))

curSec = seconds % 60  #12
totalMin = seconds // 60 #301
curMin = totalMin % 60
totalHour = totalMin // 60
curHour = totalHour % 24
totalDay = totalHour // 24

