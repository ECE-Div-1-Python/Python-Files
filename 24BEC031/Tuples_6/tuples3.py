from datetime import datetime,date


def dbd(start_date, end_date):
  #converting to d-m-y format as required by the question
  start_date = datetime.strptime(start_date, '%d-%m-%Y')
  end_date = datetime.strptime(end_date, '%d-%m-%Y')
  diff = end_date - start_date
  return diff.days

#drawback is user has to follow a strict format (I was short on time to tailor it in detail) :(
d1 = input("Enter starting date in format \"d-m-y\"")
d2 = input("Enter ending date in format \"d-m-y\"")


print(f"The distance between {d1} and {d2} is: {dbd(d1,d2)} days")
