# Owner: Rohit Kashi 
# rohitchandratejaswi.kashibatla@sjsu.edu

import sys

# Global Variables 
machine_type = 0 # Permitted Values: 1, 2, 3
inserted_single_coin_value = 0 
inserted_coin_one_value = 0 
inserted_coin_two_value = 0
value_inserted = False 

'''
# Method For Consumption And Validation Of User Input
# A ) User inputs the Gumball Machine Number
# B ) User inputs the Coin(s)

def getGumballMachineNumber( ): 
    permitted_gumball_machine_values = [ 1, 2, 3 ]
    permitted_gumball_machine_one_and_two_coin_values = [ 25 ]
    permitted_gumball_machine_three_coin_values = [ 5, 10, 25 ]
    print ("Available Gumball Machines are: ")
    print ("Gumball Machine 1: Each Gumball Costs 25 Cents, Accepted Currency: 25 Cents only.")
    print ("Gumball Machine 2: Each Gumball Costs 50 Cents, Accepted Currency: 25 Cents only.")
    print ("Gumball Machine 3: Each Gumball Costs 50 Cents, Accepted Currency: 5, 10, 25 Cents only.")
    machine_type = int ( raw_input("Pick A Gumball Machine Number From 1 2 3:  ") )
    if not permitted_gumball_machine_values.__contains__(machine_type): 
       print ("Invalid Gumball Machine Value! Pick A Number From 1 2 3")
       is_valid = False
       sys.exit(1)   
    
    elif machine_type == 2: 
         print ("Insert Two 25 Cent Coins.")
         inserted_coin_one_value = int ( raw_input("Insert the first 25 Cent Coin: ") )
         if not permitted_gumball_machine_one_and_two_coin_values.__contains__(inserted_coin_one_value):
            print ("Invalid Coin Value! Please Insert a 25 Cent Coin.")
            is_valid = False
            sys.exit(1)
         inserted_coin_two_value = int ( raw_input("Insert the second 25 Cent Coin: ") ) 
         if not permitted_gumball_machine_one_and_two_coin_values.__contains__(inserted_coin_two_value):
            print ("Invalid Coin Value! Please Insert a 25 Cent Coin.")
            is_valid = False
            sys.exit(1)
         GMObj = GumballMachineTypeTwo( )
    
    else:
         
         # 25 = 10 + 10 + 5 ( A ), 10 + 5 + 5 +5 ( B ) , 5 + 5 + 5 + 5 +5 ( C )
         # Possible Combinations : 13
         # Two 25 Cent Coins  
         # One 25 + Two 10  + One 5 Cent Coins : D
         # One 25 + One 10  + Three 5 Cent Coins 
         # One 25 + Five 5 Cent Coins : D 
         # Four 10  + Two 5 Cent Coins : D
         # Three 10 + Four 5 Cent Coins : D
         # Two 10 + Five 5 Cent Coins : D
         # Three 10 + Four 5 Cent Coins : D
         # Two 10 + 6 5 Cent Coins : D
         # Eight 5 Cent Coins + 1 10 Cent Coin : D
         # Two 10 + Six 5 Cent Coins : D
         # One 10 + Eight 5 Cent Coins : D
         # Ten 5 Cent Coins
         print ("Insert Two 25 Cent Coins.") 
         GMObj = GumballMachineTypeThree( ) 

    value_inserted = True
    return 0
'''
class GumballMachine:

      def __init__ ( self ):
          # CLASS ATTRIBUTES TO BE SET IN CHILD CLASS(ES)
          # self.machine_type = 0
          self.single_gumball_cost = 0
          self.number_of_gumballs_available = 0
          self.inserted_single_coin_value = 0
          self.inserted_coins_total_value = 0 
          self.coin_inserted = False # Indicates whether the coin was inserted or not
          self.coin_valid = False # Indicates if the coin is valid for the current machine

      # Empty Class Methods To Be OverRidden In the Child Class(es)
      
      # To insert coin(s) in the gumball machine
      def insert_coins ( self ):
          pass

      # To eject the inserted coin(s)
      def eject_coins ( self ):
          # Coin Ejection Use Cases
          # 1. Machine Out Of Gumballs.
          # 2. Inputted an Invalid coin for the Current Machine
          # 3. No Coin Inserted.
          pass
     
      # To push the gumball(s) out of the machine
      def turn_crank ( self ):
          pass


# Gumball Machine Type 1
class GumballMachineTypeOne ( GumballMachine ):

      def __init__ (self):
          GumballMachine.__init__(self)
          self.machine_type = machine_type
          self.single_gumball_cost = 25 # 25 Cents
          self.number_of_gumballs_available = 2 # RANDOM NUMBER
          # self.has_quarter = False

      def insert_coins (self, inserted_single_coin_value):
        
          print "Attempting to insert the coin in Gumball Machine One" 
          self.inserted_single_coin_value = inserted_single_coin_value
          # Decision Making should be purely based on is_coin_valid attribute
          if ( self.inserted_single_coin_value <= 0): 
               self.coin_inserted = False
               # self.has_quarter = False
               self.is_coin_valid = False
               print "No Coin Inserted! Please Insert a Quarter Dollar."
          # This means the user inserted a positive coin value
          self.coin_inserted = True
          if ( 0 < self.inserted_single_coin_value <= 25):
                 if ( self.inserted_single_coin_value == 25 ):
                      # self.has_quarter = True
                      self.is_coin_valid = True
                      print "Successfully inserted the coin"
                 else: 
                      self.is_coin_valid = False
                      print "Failed to insert the coin"
          if ( self.inserted_single_coin_value > 25):
               self.is_coin_valid = False
               print "Please insert a 25 cents coin."

      def eject_coins (self):
          if ( self.is_coin_valid == False ): 
               print ("Invalid Coin Inserted! This Machine Only Accepts A Quarter Dollar, Please insert a Quarter Dollar.")
          elif ( self.is_coin_valid == True ): 
                self.is_coin_valid = False
      
      def turn_crank (self):
          if ( self.is_coin_valid ):
             if ( self.number_of_gumballs_available == 0 ):
                  print ("No More Gumballs! Ejecting Your Coin.")
                  self.eject_coins()
             else:
                  self.number_of_gumballs_available -= 1
                  print ("Thanks for your quarter.  Gumball Ejected!.")
                  self.eject_coins()
          else: self.eject_coins()

'''
class GumballMachineTypeTwo(GumballMachine):
      def __init__ ( self, machine_type, inserted_single_coin_value ):
          GumballMachine.__init__(self)
          self.machine_type = machine_type
          self.single_gumball_cost = 50 # 50 Cents
          self.number_of_gumballs_available = 1 # RANDOM NUMBER
          self.has_two_quarters = False
          self.inserted_single_coin_value = inserted_single_coin_value
          if ( self.inserted_single_coin_value != 0): self.coin_inserted = True

      def insert_coins ( self ):
          if ( self.inserted_single_coin_value >= 0):
             if ( self.inserted_single_coin_value == 0): self.coin_inserted = False
             elif ( self.inserted_single_coin_value == 25): print ("Only 25 Cents Inserted ! 25 More Cents are needed for a gumball on this machine.")
             elif ( self.inserted_single_coin_value == 50):
                   self.has_two_quarters = True
                   self.coin_inserted = True
          else: #self.has_quarter = False
     
     def eject_coins ( self ):
         if ( self.has_two_quarters): self.has_two_quarters = False
         elif ( self.coin_inserted == False ): print ("No Coin Inserted! Please Insert a Quarter Dollar.")
         else: print ("Invalid Coin Inserted! This Machine Only Accepts Two Quarter Dollar, Please insert Two Quarter Dollar.")
      
      def turn_crank ( self ):
          if ( self.has_two_quarters ):
             if ( self.number_of_gumballs_available > 0 ):
                  self.number_of_gumballs_available -= 1
                  self.has_two_quarters = False
                  print ("Thanks for your quarter.Gumball Ejected!.")
             else:
                  print ("No More Gumballs! Ejecting Your Coin.")
                  self.eject_coins()
          else: self.eject_coins()
'''
'''
class GumballMachineTypeThree ( GumballMachine) : #Accepts 5, 10 , 25 Cents #Costs 50 Cents

      def __init__(self, inserted_single_coin_value):
          GumballMachine.__init__(self)
          self.machine_type = machine_type
          self.single_gumball_cost = 50 # 50 Cents
          self.number_of_gumballs_available = 1  #RANDOM NUMBER
          self.inserted_single_coin_value = inserted_single_coin_value
          self.has_dime = False
          self.has_penny = False
          self.has_quarter = False

      def insert_coins(self):
          if ( self.inserted_single_coin_value <= 0): self.coin_inserted = False
          # This means the user inserted a positive coin value
          else:
             self.coin_inserted = True
             if ( self.inserted_single_coin_value == 25): 
                  self.has_quarter = True
                  self.inserted_single_coin_value += 25
             if ( self.inserted_single_coin_value == 10): 
                  self.has_penny = True
                  self.inserted_single_coin_value += 10
             if ( self.inserted_single_coin_value == 5): 
                  self.has_dime = True
                  self.inserted_single_coin_value += 5
  
       # Coin Ejection Use Cases
          # 1. Out Of Gumballs.
          # 2. Inputted an Invalid coin for the Current Machine
          # 3. No Coin Inserted.    

      def eject_coins(self):
         if ( self.coin_inserted == False ): print ("No Coin Inserted! Please Insert a Quarter ,Penny ,Dime.")
         if ( self.has_quarter ): self.has_quarter = False
         if ( self.has_penny ): self.has_penny = False
         if ( self.has_dime ): self.has_dime = False
         else: print ("Invalid Coin Inserted! This Machine Only Accepts Quarters, Pennies, Dimes Please insert one of these.")


      def turn_crank(self):
          if ( self.has_quarter ):
             if ( self.number_of_gumballs_available > 0 ):
                  self.number_of_gumballs_available -= 1
                  self.has_quarter = False
                  print ("Thanks for your quarter.  Gumball Ejected!")
             else:
                  print ("No More Gumballs! Ejecting Your Coin.")
                  self.eject_coins()
          else: self.eject_coins() 
'''

# is_valid = True
# while is_valid:
# getGumballMachineNumber()
# Based on the machine type the respective Gumball Machine Class Object is created
'''
   if machine_type == 1:
      inserted_single_coin_value = int ( raw_input("Insert A 25 Cent Coin: ") )
      if not permitted_gumball_machine_one_and_two_coin_values.__contains__(inserted_single_coin_value):
          print ("Invalid Coin Value! Please Insert a 25 Cent Coin.")
          is_valid = False
          sys.exit(1)
      GMObj = GumballMachineTypeOne( )
'''
GMObj = GumballMachineTypeOne( )
GMObj.insert_coins(25)
GMObj.turn_crank()
GMObj.turn_crank()

