#
# i6screwdir.py is a python program
# Created By
# Ibrahim Z Sial
# August 17, 2016

#Discription:
# This is a repository of every screw used in the iPhone 6.

#Perpose/Use:
# This should function by asking for the user to input the length of a screw and
# the program will check the drectory to see if there is a matching screw in the
# iPhone and tell the user where in the iPhone it is. 

#Expanson: 
# There should be an option to search by key word:
# There should be tolorance that alows for some of the screws to not match
# perfect. There should be some way to do this simply.


#Below are the values of each screw in the iPhone 6 with my own aplha-numeric
# representation of that screw it's lenth and a discription of it's placment
# within the phone.
# Thay are stored as a three part list within a 56 part list. i6ScrewList[[AN, mm, Discription,]]
i6ScrewLength = [3.75, 1.69, 3.10, 1.20, 2.82, 2.06, 1.58, 1.24, 1.60, 2.61,
                 2.37, 1.50, 1.34, 1.89, 2.35, 1.58, 2.24, 1.88, 2.98, 1.56,
                 2.27, 2.86, 2.31, 3.08, 1.74, 1.68, 1.47, 3.56, 1.51, 1.38,
                 2.11, 2.15, 1.89, 1.50]

i6ScrewList = [ ['Z201', '3.75', 'Two pentalope screws that hold the screen closed.'],
                ['A181', '1.69', 'The top left conner screw of the five Phillips screws holding the EM shield to the logic board.'],
                ['A182', '3.10', 'The top right conner screw of the five Phillips screws holding the EM shield to the logic board.'],
                ['A183', '1.20', 'The bottom three Phillips screws of the five Phillips screws holding the EM shield to the logic board.'],
                ['A191', '2.82', 'The bottom left of the two Phillips screws holding the battery retaining plate in place.'],
                ['A192', '2.60', 'The top right of the two Phillips screws holding the battery retaining plate in place.'],
                ['B061', '2.90', 'The left of the two Pillips screws holding the volume and power flex cable retaining plate in place.'],
                ['B062', '2.24', 'The right of the two Phillips screws holding the volume and power flex cable retaining plate in place.'],
                ['B071', '2.06', 'The bottom right of the two Phillips screws holding the rear facing camera braket in place.'],
                ['B072', '1.58', 'The top left of the two Phillips screws holding the rear facing camera in place.'],
                ['B081', '1.24', 'The Pillips screw holding the flash and rear microphone retaining bracket in place.'],
                ['B091', '1.60', 'Two Pillips screws holding the vibration motor in place.'],
                ['B031', '2.61', 'The top Pillips screw that holds the logic board to the top of the frame'],
                ['B032', '2.37', 'The Standoff screw that holds the top logic board to the frame.'],
                ['B011', '1.50', 'The Phillips screw located just above the rear-facing camera connector.'],
                ['B021', '1.34', 'The Phillips screw holding the L shaped braket to the rim of the frame at the top of the logic board.'],
                ['B211', '1.89', 'Pillips screw in middle of logic board, below sim tray.'],
                ['B212', '2.35', 'Optional screw at bottom of logic board.'],
                ['C151', '1.58', 'Six Phillips screws holding the thermal plate in place to the back of the LCD screen.'],
                ['C152', '2.24', 'The bottom Phillips screw next to the home buttombracket.'],
                ['C161', '1.88', 'The two Phillips screws holding the home button to the back of screen.'],
                ['C172', '2.98', 'Middle screw securing the ear speaker/camera bracket to the back of the screen'],
                ['C173', '1.56', 'Bottom right screw securing the ear speaker/camera bracket to the back of the screen'],
                ['D131', '2.27', 'Top right Phillips screw holding the loud speaker in place.'],
                ['D132', '2.86', 'Two Left Phillips screws holding the loud speaker in place.'],
                ['D133', '2.31', 'Bottom right Phillips screws holding the loud speaker in place.'],
                ['D121', '3.08', 'Two screws holding the white adio jack in place.'],
                ['D102', '1.74', 'Middle left Phillips screw holding the charging port to the frame.'],
                ['D103', '1.68', 'Middle right Phillips screw holding the charging port to the frame.'],
                ['D104', '1.47', 'Bottom two screws holding the charging poart to the frame.'],
                ['D111', '3.56', 'Phillips screw holding plastic bracket and the lower microphone agenst the frame'],        
                ['E051', '1.51', 'Top two Phillips screws holding the WiFi antenna to the frame.'],
                ['E052', '1.38', 'Top one Phillips screws holding the WiFi antenna down.'],
                ['E053', '2.11', 'Bottom one of the two Phillips screws holding the WiFi antenna to the frame.'],
                ['E054', '2.15', 'Lowest screw holding the WiFi anttena to the frame.'],
                ['E041', '1.89', 'Left of the two remaining screws holding the metal coupler in place'],
                ['E042', '1.50', 'Right of the two remaining screws holding the metak coupler in place']]
                
                
                
 


# Z201 = 3.75
# A181 = 1.69
# A182 = 3.10
# A183 = 1.20
# A191 = 2.82
# A192 = 2.60
# B061 = 2.90
# B062 = 2.24
# B071 = 2.06
# B072 = 1.58
# B081 = 1.24
# B091 = 1.60
# B031 = 2.61
# B032 = 2.37
# B011 = 1.50 # "
# B021 = 1.34 # "
# B211 = 1.89 # "Pillips screw in middle of logic board, below sim tray"
# B212 = 2.35 # "Optional screw at bottom of logic board 
# C151 = 1.58 # "Six Phillips screws holding thermal plate in place"
# C152 = 2.24 # "Bottom screw next to home button holding thermal plate in place"
# C161 = 1.88 # "Two Phillips screws holding the home button bracket"
# C171 = 2.20 # "Top left screw securing the ear speaker/camera bracket"
# C172 = 2.98 # "Middle screw securing the ear speaker/camera bracket"
# C173 = 1.56 # "Bottom right screw securing the ear speaker/camera bracket"
# D131 = 2.27 # "Top right Phillips screw holding the loud speaker in place'
#D132 = 2.86 # "Two Left Phillips screws holding the loud speaker in place"
#D133 = 2.31 # "Bottom right Phillips screw holding the loud speaker in place"
#D121 = 3.08 # "Two screws holding white adio jack inplace"
#D101 = 3.05 # "Two top of six Phillips screws holding the charging port to the frame"
#D102 = 1.74 # "Middle left Phillips screw holding the charging port to the frame"
#D103 = 1.68 # "Middle right Phillips screw holding the charging port to the frame"
#D104 = 1.47 # "Botton two Phillips screw holding the charging port to the frame"
#D111 = 3.56 # "Hold platic bracket and the lower microphone agenst the frame"
#E051 = 1.51 # "Top two Phillips screws holding WiFi antenna to frame"
#E052 = 1.38 # "Top one of the two Phillips screws holding the WiFi antenna down" 
#E053 = 2.11 # "Bottom one of the two Phillips screws holding the WiFi anttena down"
#E054 = 2.15 # "Lowest screw holding the WiFi anttena down between power and volumee flex cable clips"
#E041 = 1.89 # "Left of two remaining screws holding metal coupler in place"
#E042 = 1.50 # "Right of two remaining scres holding metal coupler in place"


#The Main Menue



option = 1


def OptionOne(one):
    print ('Hello Welcome to the i6 screw map helper')
    print('[2] - Search for a screw by length')
    print ('[3] - Set tolorance.')
    print ('[4] - List all screw values')
    print ('[5] - See devloper notes')
    print ('[x] - this is option five')
    return(input())

   
def OptionTwo(two):
    print('Option [1] is still under development sorry')
    print('Please input the length of the screw in milimeters')
    screwmm = input()
    screwmm = float(screwmm)

    print(i6ScrewList[i6ScrewLength.index(screwmm)])
    
    print ('To return to the main menue press [1] then ENTER')
    print ('To exit press [x] then ENTER')
    return(input())

def OptionThree(three):
    print('This function is still under development.')
    print ('To return to the main menue press [1] then ENTER')
    print ('To exit press [x] then ENTER')
    return(input())

def OptionFour(four):
           
    print(range(len(i6ScrewList)))
    for i in range(len(i6ScrewList)):
        print(i6ScrewList[i])
    
    print ('To return to the main menue press [1] then ENTER')
    print ('To exit press [x] then ENTER')
    return(input())

def OptionFive(five):
    print('i6 Screw Mapper')
    print('Verson 1.0')
    print('Developed by: Ibrahim Z Sial')
    print('Project Start Date: 8/17/2016')
    print('This project was intended to be developed under the open source community.')
    print('Addition and modification to this code is welcome,')
    print('just please make a note of any changes here in the notes and develoment information section')
    print('For any issues with debugging the code please send to sialrefurbishing@gmail.com')

    
    print ('To return to the main menue press [1] then ENTER')
    print ('To exit press [x] then ENTER')
    return(input())

while option ==1:
    option = int(option)
    while option == 1:
        option = OptionOne(option)
        
    print(option)

    option = int(option)
    while option == 2:
        option = OptionTwo(option)

    option = int(option)
    while option == 3:
        option = OptionThree(option)

    option = int(option)
    while option == 4:
        option = OptionFour(option)

    option = int(option)
    while option == 5:
        option = OptionFive(option)

print(option)



      
#int(menue) = menue #converts the user input to an intager


      
#print('What is the value of the screw that you are maping? please enter a value grater than zero')
#screwSize = input()
    
#float(screwSize) = screwSize #converts any value passed to a floating point number

#if (screwSize):
#       print ('This is a petalope screw and is ether gold silver or gray')
    

