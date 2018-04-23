# Owner: Rohit Kashi
# rohitchandratejaswi.kashibatla@sjsu.edu

from random import randint

class GumballMachine:

      def __init__ ( self ):
          # Class Object Attributes To Be Set In Inheriting Classes
          self.single_gumball_cost = 0
          self.number_of_gumballs_available = 0
          self.inserted_single_coin_value = 0
          self.inserted_coins_total_value = 0
          self.is_coin_inserted = False # Indicates whether the coin was inserted or not
          self.is_coin_valid = False # Indicates if the coin is valid for the current machine

      # Empty Class Methods To Be OverRidden In the Child Classes

      # To insert coins in the Gumball Machine
      def insert_coins ( self ):
          pass

      # To Eject the Inserted Coin's From The Gumball Machine
      def eject_coins ( self ):
          # Coin Ejection Use Cases
          # 1. Machine Out Of Gumballs.
          # 2. Inputted an Invalid coin for the Current Machine
          # 3. No Coin Inserted.
          pass

      # To push the Gumball(s) From the machine
      def turn_crank ( self ):
          pass


# Gumball Machine One
class GumballMachineOne ( GumballMachine ):

      def __init__ (self):
          GumballMachine.__init__(self)
          self.single_gumball_cost = 25 # In Cents
          self.number_of_gumballs_available = randint(1, 3) # RANDOM NUMBER BETWEEN 1,3 
          print ("GUMBALL MACHINE ONE:")
          print ("Each Gumball Costs 25 Cents, Accepted Currency: 25 Cents Only.")
          print "Number Of Gumballs Available: " + str( self.number_of_gumballs_available )
          

      def insert_coins (self, inserted_single_coin_value):
          print "Attempting To Insert A Coin In Gumball Machine One"
          self.inserted_single_coin_value = inserted_single_coin_value
          # Decision Making Is Purely Based On is_coin_valid attribute
          if ( self.inserted_single_coin_value <= 0):
               print "No Coin Inserted! Please Insert A 25 Cents Coin."

          # This Means That The User Inserted A Coin
          self.is_coin_inserted = True
          if ( 0 < self.inserted_single_coin_value <= 25):
                 if ( self.inserted_single_coin_value == 25 ):
                      self.is_coin_valid = True
                      print "Successfully Inserted The 25 Cents Coin"
                 else:
                      print "Coin Value is Less Than 25 Cents. Failed To Insert The Coin."
          if ( self.inserted_single_coin_value > 25):
               print "Inserted Coin Value Is Greater Than 25 Cents. Please Insert A 25 Cents Coin."

      def eject_coins (self):
          if ( self.is_coin_valid == False ):
               print ("Invalid Coin Inserted! This Machine Only Accepts A Quarter Dollar, Please Insert A Quarter Dollar.")
          elif ( self.is_coin_valid == True ):
                self.is_coin_valid = False

      def turn_crank (self):
          if ( self.is_coin_valid ):
             if ( self.number_of_gumballs_available == 0 ):
                  print ("No More Gumballs! Ejecting Your Coin.")
                  self.eject_coins()
             else:
                  self.number_of_gumballs_available -= 1
                  print ("Thanks For Your 25 Cents. A Gumball Was Ejected!.")
                  print "Available Gumballs: " + str( self.number_of_gumballs_available )
                  self.eject_coins()
          else: self.eject_coins()



class GumballMachineTwo(GumballMachine):
      def __init__ ( self ):
          GumballMachine.__init__(self)
          self.single_gumball_cost = 50 # 50 Cents
          self.number_of_gumballs_available = randint(1, 4) # RANDOM NUMBER
          print ("GUMBALL MACHINE TWO:")
          print ("Each Gumball Costs 50 Cents, Accepted Currency: 25 Cents only.")
          print "Number Of Gumballs Available: " + str( self.number_of_gumballs_available )
          self.is_first_coin_inserted = False
          self.first_coin_value = 0
          self.is_first_coin_valid = False
          self.is_second_coin_inserted = False
          self.second_coin_value = 0
          self.is_second_coin_valid = False
          self.are_coins_valid = False # Indicates if the inserted coins are valid for the current machine

      def insert_coins ( self, first_coin_value, second_coin_value ):
          self.first_coin_value = first_coin_value
          self.second_coin_value = second_coin_value
          # Decision Making Is Only Based On are_coins_valid attribute
          print "Attempting To Insert The First Coin In Gumball Machine Two" 
          
          if ( self.first_coin_value <= 0):
               print "No Coin Inserted! Please Insert The First 25 Cents Coin."
    
          # This Means That The User Inserted A Coin
          self.is_first_coin_inserted = True
          if ( 0 < self.first_coin_value <= 25):
                 if ( self.first_coin_value == 25 ):
                      self.is_first_coin_valid = True
                      print "Successfully Inserted The First 25 Cents Coin"
                 else:
                      print "Coin Value is Less Than 25 Cents. Failed To Insert The Coin."
          if ( self.inserted_single_coin_value > 25):
               print "Inserted Coin Value Is Greater Than 25 Cents. Please Insert A 25 Cents Coin."
               
          print "Attempting To Insert The Second Coin In Gumball Machine Two" 
          if ( self.second_coin_value <= 0):
               print "No Coin Inserted! Please Insert The Second 25 Cents Coin."
          # This Means That The User Inserted A Positive Coin Value
          self.is_second_coin_inserted = True
          if ( 0 < self.second_coin_value <= 25):
                 if ( self.second_coin_value == 25 ):
                      self.is_coin_valid = True
                      print "Successfully Inserted The Second 25 Cents Coin"
                 else:
                      self.is_second_coin_valid = False
                      print "Coin Value is Less Than 25 Cents. Failed To Insert The Second Coin."
          if ( self.inserted_single_coin_value > 25):
               print "Inserted Coin Value Is Greater Than 25 Cents. Please Insert A 25 Cents Coin."
          
          if ( ( self.is_first_coin_valid is True ) and ( self.is_second_coin_valid is True ) ): self.are_coins_valid = True
          else: self.are_coins_valid = False
                      
      def eject_coins (self):
          if ( self.are_coins_valid == False ):
                if ( self.is_first_coin_inserted is False ):  print ("First Coin Not Inserted! Please Insert 25 Cents.")
                if ( self.is_second_coin_inserted is False ): print ("Second Coin Not Inserted! Please Insert 25 Cents.")
                if ( self.is_first_coin_inserted is False and self.is_second_coin_inserted is False ):
                    print ("No Coins Inserted! Please Insert Two 25 Cent's.")
          if ( self.are_coins_valid == True ): self.are_coins_valid = False
      
      def turn_crank (self):
          if ( self.are_coins_valid ):
             if ( self.number_of_gumballs_available == 0 ):
                  print ("No More Gumballs! Ejecting Your Coins.")
                  self.eject_coins()
             else:
                  self.number_of_gumballs_available -= 1
                  print ("Thanks For Your 50 Cents. A Gumball Was Ejected!.")
                  print "Available Gumballs: " + str( self.number_of_gumballs_available )
                  self.eject_coins()
          else: self.eject_coins()


class GumballMachineThree ( GumballMachine) : 

      def __init__( self ):
          GumballMachine.__init__(self)
          self.single_gumball_cost = 50 # 50 Cents
          self.number_of_gumballs_available = randint(1, 4)  #RANDOM NUMBER
          self.valid_coin_values = [ 5, 15, 25 ]
          self.is_first_coin_inserted = False
          self.first_coin_value = 0
          self.is_first_coin_valid = False
          self.is_second_coin_inserted = False
          self.second_coin_value = 0
          self.is_second_coin_valid = False
          self.is_third_coin_inserted = False
          self.third_coin_value = 0
          self.is_third_coin_valid = False
          self.are_coins_valid = False # Indicates if the inserted coins are valid for the current machine
          self.coin_maybe_valid = False # For Some Use Cases. Ex: 0, 25, 25 
          
          print ("GUMBALL MACHINE THREE:")
          print ("Each Gumball Costs 50 Cents, Accepted Currency: 5, 10, 25 Cents only.")
          print "Number Of Gumballs Available: " + str( self.number_of_gumballs_available )
          
      def insert_coins ( self, first_coin_value, second_coin_value, third_coin_value ):
          self.first_coin_value = first_coin_value
          self.second_coin_value = second_coin_value
          self.third_coin_value = third_coin_value
          
          # Decision Making Is Only Based On are_coins_valid attribute
          
          print "Attempting To Insert The First Coin In Gumball Machine Three"
          if ( self.first_coin_value < 0): print "No Coin Inserted! Please Insert The First Coin."
          if ( self.first_coin_value == 0): 
              print "No Coin Inserted! Please Insert The First Coin."
              self.coin_maybe_valid = True
          
          # This Means That The User Inserted A Coin
          self.is_first_coin_inserted = True
          
          if ( self.first_coin_value in self.valid_coin_values ):
                self.is_first_coin_valid = True
                print "Successfully Inserted The First Coin"
        
          if ( self.first_coin_value not in self.valid_coin_values ): print ("Invalid First Coin! Please Choose From 5, 15 , 25 Cents.")
                  
          print "Attempting To Insert The Second Coin In Gumball Machine Three"       
          if ( self.second_coin_value < 0):
               print "No Coin Inserted! Please Insert The Second Coin."
          if ( self.second_coin_value == 0): 
               print "No Coin Inserted! Please Insert The Second Coin."
               self.coin_maybe_valid = True
          # This Means That The User Inserted A Coin
          self.is_second_coin_inserted = True
          if ( self.second_coin_value > 0):
              if ( self.second_coin_value in self.valid_coin_values ):
                  self.is_second_coin_valid = True
                  print "Successfully Inserted The Second Coin"
              else: 
                  print ("Invalid Second Coin! Please Choose From 5, 15 , 25 Cents.")
               
          print "Attempting To Insert The Third Coin In Gumball Machine Three"     
          if ( self.third_coin_value <= 0):
               print "No Coin Inserted! Please Insert The Third Coin." 
          if ( self.third_coin_value == 0): 
               print "No Coin Inserted! Please Insert The Third Coin."
               self.coin_maybe_valid = True
               
          # This Means That The User Inserted A Coin
          self.is_third_coin_inserted = True
          if ( self.third_coin_value > 0):
              if ( self.third_coin_value in self.valid_coin_values ):
                  self.is_third_coin_valid = True
                  print "Successfully Inserted The Third Coin"
              else: 
                  print ("Invalid Third Coin! Please Choose From 5, 15 , 25 Cents.")
               
          if ( self.is_first_coin_valid and self.is_second_coin_valid and self.is_third_coin_valid ):  
             if ( self.first_coin_value + self.second_coin_value + self.third_coin_value  == 50 and self.coin_maybe_valid ):  
                  self.are_coins_valid = True
             else: self.are_coins_valid = False            
          
          
      def eject_coins(self):
         if ( self.are_coins_valid == False ):
                if ( self.is_first_coin_inserted is False ):  print ("First Coin Not Inserted! Please Choose From 5, 15 , 25 Cents.")
                if ( self.is_second_coin_inserted is False ): print ("Second Coin Not Inserted! Please Choose From 5, 15 , 25 Cents.")
                if ( self.is_third_coin_inserted is False ): print ("Third Coin Not Inserted! Please Choose From 5, 15 , 25 Cents.")
                if ( self.is_first_coin_inserted is False and self.is_second_coin_inserted is False and self.is_third_coin_inserted is False):
                    print ("No Coins Inserted! Please Choose From 5, 15 , 25 Cents.")
         if ( self.are_coins_valid == True ): self.are_coins_valid = False


      def turn_crank(self):
          if ( self.are_coins_valid ):
             if ( self.number_of_gumballs_available == 0 ):
                  print ("No More Gumballs! Ejecting Your Coins.")
                  self.eject_coins()
             else:
                  self.number_of_gumballs_available -= 1
                  print ("Thanks For Your 50 Cents. A Gumball Was Ejected!.")
                  print "Available Gumballs: " + str( self.number_of_gumballs_available )
                  self.eject_coins()
          else: self.eject_coins()


# GUMBALL MACHINE ONE 
GMObj = GumballMachineOne( )
# FAILURE USE CASES
GMObj.insert_coins(-5)
GMObj.insert_coins(0)
GMObj.insert_coins(15)
GMObj.insert_coins(30)
# SUCCESS USE CASE 
GMObj.insert_coins(25)
GMObj.turn_crank()
print ("")
print ("")
print ("")
print ("")


''' 
GUMBALL MACHINE ONE SAMPLE OUTPUT 
GUMBALL MACHINE ONE:
Each Gumball Costs 25 Cents, Accepted Currency: 25 Cents Only.
Number Of Gumballs Available: 3
Attempting To Insert A Coin In Gumball Machine One
No Coin Inserted! Please Insert A 25 Cents Coin.
Attempting To Insert A Coin In Gumball Machine One
No Coin Inserted! Please Insert A 25 Cents Coin.
Attempting To Insert A Coin In Gumball Machine One
Coin Value is Less Than 25 Cents. Failed To Insert The Coin.
Attempting To Insert A Coin In Gumball Machine One
Inserted Coin Value Is Greater Than 25 Cents. Please Insert A 25 Cents Coin.
Attempting To Insert A Coin In Gumball Machine One
Successfully Inserted The 25 Cents Coin
Thanks For Your Quarter. A Gumball Was Ejected!.
Available Gumballs: 2
'''

# GUMBALL MACHINE TWO 
GMObj = GumballMachineTwo( )
# FAILURE USE CASES
GMObj.insert_coins ( -5, -5 )
GMObj.insert_coins ( 0, 0 ) 
GMObj.insert_coins(15,25)
GMObj.insert_coins(25,15)
GMObj.insert_coins(15,30)
GMObj.insert_coins(30,15)
GMObj.insert_coins(30,25)
GMObj.insert_coins(25,30)
GMObj.insert_coins(30,30)

# SUCCESS USE CASE
GMObj.insert_coins(25,25)
GMObj.turn_crank()
print ("")
print ("")
print ("")
print ("")

'''
GUMBALL MACHINE TWO SAMPLE OUTPUT
GUMBALL MACHINE TWO:
Each Gumball Costs 50 Cents, Accepted Currency: 25 Cents only.
Number Of Gumballs Available: 1
Attempting To Insert The First Coin In Gumball Machine Two
No Coin Inserted! Please Insert The First 25 Cents Coin.
Attempting To Insert The Second Coin In Gumball Machine Two
No Coin Inserted! Please Insert The Second 25 Cents Coin.
Attempting To Insert The First Coin In Gumball Machine Two
No Coin Inserted! Please Insert The First 25 Cents Coin.
Attempting To Insert The Second Coin In Gumball Machine Two
No Coin Inserted! Please Insert The Second 25 Cents Coin.
Attempting To Insert The First Coin In Gumball Machine Two
Coin Value is Less Than 25 Cents. Failed To Insert The Coin.
Attempting To Insert The Second Coin In Gumball Machine Two
Successfully Inserted The Second 25 Cents Coin
Attempting To Insert The First Coin In Gumball Machine Two
Successfully Inserted The First 25 Cents Coin
Attempting To Insert The Second Coin In Gumball Machine Two
Coin Value is Less Than 25 Cents. Failed To Insert The Second Coin.
Attempting To Insert The First Coin In Gumball Machine Two
Coin Value is Less Than 25 Cents. Failed To Insert The Coin.
Attempting To Insert The Second Coin In Gumball Machine Two
Attempting To Insert The First Coin In Gumball Machine Two
Attempting To Insert The Second Coin In Gumball Machine Two
Coin Value is Less Than 25 Cents. Failed To Insert The Second Coin.
Attempting To Insert The First Coin In Gumball Machine Two
Attempting To Insert The Second Coin In Gumball Machine Two
Successfully Inserted The Second 25 Cents Coin
Attempting To Insert The First Coin In Gumball Machine Two
Successfully Inserted The First 25 Cents Coin
Attempting To Insert The Second Coin In Gumball Machine Two
Attempting To Insert The First Coin In Gumball Machine Two
Attempting To Insert The Second Coin In Gumball Machine Two
Attempting To Insert The First Coin In Gumball Machine Two
Successfully Inserted The First 25 Cents Coin
Attempting To Insert The Second Coin In Gumball Machine Two
Successfully Inserted The Second 25 Cents Coin
'''

# GUMBALL MACHINE THREE
GMObj = GumballMachineThree( )

# FAILURE USE CASES
GMObj.insert_coins ( -1, -2, -3 )
GMObj.insert_coins ( 0, 0, 0 )
GMObj.insert_coins ( -1, -2, -3 )
GMObj.insert_coins ( 5, 15, 25 )

# SUCCESS USE CASE
GMObj.insert_coins ( 0, 25, 25 ) 
GMObj.turn_crank()
print ("")
print ("")
print ("")
print ("")

''' GUMBALL MACHINE THREE SAMPLE OUTPUT
GUMBALL MACHINE THREE:
Each Gumball Costs 50 Cents, Accepted Currency: 5, 10, 25 Cents only.
Number Of Gumballs Available: 4
Attempting To Insert The First Coin In Gumball Machine Three
No Coin Inserted! Please Insert The First Coin.
Invalid First Coin! Please Choose From 5, 15 , 25 Cents.
Attempting To Insert The Second Coin In Gumball Machine Three
No Coin Inserted! Please Insert The Second Coin.
Attempting To Insert The Third Coin In Gumball Machine Three
No Coin Inserted! Please Insert The Third Coin.
Attempting To Insert The First Coin In Gumball Machine Three
No Coin Inserted! Please Insert The First Coin.
Invalid First Coin! Please Choose From 5, 15 , 25 Cents.
Attempting To Insert The Second Coin In Gumball Machine Three
No Coin Inserted! Please Insert The Second Coin.
Attempting To Insert The Third Coin In Gumball Machine Three
No Coin Inserted! Please Insert The Third Coin.
No Coin Inserted! Please Insert The Third Coin.
Attempting To Insert The First Coin In Gumball Machine Three
No Coin Inserted! Please Insert The First Coin.
Invalid First Coin! Please Choose From 5, 15 , 25 Cents.
Attempting To Insert The Second Coin In Gumball Machine Three
No Coin Inserted! Please Insert The Second Coin.
Attempting To Insert The Third Coin In Gumball Machine Three
No Coin Inserted! Please Insert The Third Coin.
Attempting To Insert The First Coin In Gumball Machine Three
Successfully Inserted The First Coin
Attempting To Insert The Second Coin In Gumball Machine Three
Successfully Inserted The Second Coin
Attempting To Insert The Third Coin In Gumball Machine Three
Successfully Inserted The Third Coin
Attempting To Insert The First Coin In Gumball Machine Three
No Coin Inserted! Please Insert The First Coin.
Invalid First Coin! Please Choose From 5, 15 , 25 Cents.
Attempting To Insert The Second Coin In Gumball Machine Three
Successfully Inserted The Second Coin
Attempting To Insert The Third Coin In Gumball Machine Three
Successfully Inserted The Third Coin
Thanks For Your 50 Cents. A Gumball Was Ejected!.
Available Gumballs: 3
'''
