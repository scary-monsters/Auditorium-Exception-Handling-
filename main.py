import numpy as np
import pandas as pd
# Array with Full Seats
A = np.array([[0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]])
# Array with only 2 open seats
B = np.array([[1, 0, 0,1, 1], 
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1]])
# Custom made Exception error for when the Auditorium is Full
class AuditoriumFull(Exception):
  def __init__(self, msg):
    super().__init__(msg)
    
class Auditorium:
    def __init__(self, meeting_date, times, num_seats):
        # constructor initializing my variables
        self.meeting_date = input("Meeting Date:  ")
        self.times = input("Time:  ")
        self.num_seats = 15
    # Method that checks if the auditorium is full
    # Will raise an Error if it's full
    def auditorium_full(self):
      try:
        one_zero = 0 in B
        if one_zero == False:
          raise AuditoriumFull('No Seats')
      except AuditoriumFull:
        print("No Seats Available "+" Date: "+ self.meeting_date + " Time: "+ self.times)
    # Method that reserves a seat if the auditorium is full
    def reserve_seat(self):
      audit.auditorium_full()
      x = np.argwhere(B == 0)
      try:
        idx = pd.Index(x[0])
        one = idx[0]
        two = idx[1]
        B[one,two] = 1
        print(B)
        print("Your seat has been reserved!")
        print(str(x[0]) + " Is your seat number!")
        print("Your Date! "+ self.meeting_date)
        print("Your Time! "+ self.times)
      except (IndexError,UnboundLocalError):
        pass
    # Method that cancels a seat   
    def cancel_seat(self):
      r = int(input("What is your row number? 0-2? "))
      c = int(input("What is your column number ? 0-4? "))
      B[r,c] = 0
      print(B)
      print("Your Reservation has been canceled!")

# Driver Code
prompt = True
audit = Auditorium(0,0,15)
# Repeated prompts until user choses to stop
# With array B if you Reserve three times it will cause the Exception Handling
# After that you can still Cancel a seat
while(prompt == True):
  p = input("Would you like to Reserve, Cancel a Seat or End? R, C, or E? ")
  if(p == "R"):
    audit.reserve_seat()
  elif(p == "C"):
    audit.cancel_seat()
  else:
    prompt = False
# Driver Code

  

