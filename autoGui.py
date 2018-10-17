#imports modules
import pyautogui as auto
import datetime
import time
import pickle



#allows for a failsafe to break the program
auto.PAUSE = .5
auto.FAILSAFE = True

print('\n\n\n')
print('  Welcome to autoGUI.  '.center(240,'#'))

while True:
    #sets all the parameters for the program loop
    

    #creates a class to be used for each step of the program (each step will be an instants of the class)
    class automate:
        
                location = 0 #stores location for movement function
                duration = .3 #the duration in seconds for the mouse to move locations
                message = 'print' #the default message for the type function
                move = 0     #uses the move function when value is changed to 1
                click = 0    #uses the click function when value is changed to 1
                doubleclick = 0    #uses the click function when value is changed to 1
                dateTime = 0
                pri = 0      #uses the print function when value is changed to 1
                enter = 0    #uses the enter function when the value is changed to 1 
                ctrlA = 0
                ctrlC = 0
                ctrlV = 0
                progPause = 0
                image_found = 0
                sleeper = 1
                
                #this definition contains all the AutiGui functions 
                def doStuff(self):
                    if self.move == 1:
                        auto.moveTo(self.location, duration = self.duration) 
                        auto.click()
                        
                    elif self.doubleclick == 1:
                        auto.moveTo(self.location, duration = self.duration)
                        auto.click(clicks=2)
                        
                    elif self.pri == 1:
                        auto.typewrite(self.message, interval = .05)
                        print(self.message)
                        
                    elif self.dateTime == 1:
                        fileDate = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                        auto.typewrite('file_%s' %(fileDate), interval = .05) #writes file with date, time, and temperature the test was run at
                            
                    elif self.enter == 1:
                        auto.hotkey('enter')
                        
                    elif self.ctrlA == 1:
                        auto.hotkey('ctrl', 'a')
                        
                    elif self.ctrlC == 1:
                        auto.hotkey('ctrl', 'c')
                        
                    elif self.ctrlV == 1:
                        auto.hotkey('ctrl', 'v')
                        
                    elif self.progPause == 1:
                        time.sleep(int(self.sleeper))
                        
                    elif self.image_found == 1:
                        while True:
    
                            if auto.locateOnScreen('img.png') != None:
                                print('Image found')
                                auto.moveTo(auto.locateCenterOnScreen('img.png'), duration = self.duration)
                                break
                                
                            else:
                                print('image not found')
                            time.sleep(2)
                            
                          
    
    step = [] #this variable will contain all the step objects    
    rs = 0 #used to run saved steps
    
    #This loop alows the user to enter multiple steps
    while True:
                
        step.append(automate()) #creates a new object for each step at the begining of the loop
                
        x = input('\nWhat would you like to do with this step: \n1 = Move to and click a location, \n2 = Move to and double click a location \n3 = Type a message, \n4 = Hit enter, \n5 = Prints a file name with the date and time, \n6 = ctrl a, \n7 = ctrl c, \n8 = ctrl v, \n9 = Pause, \n10 = locate image and move to center, \ns = Save steps, \nrs = Run saved steps, \nr = Run steps\n')
                
                
                #this if block changes the variables in the object to determin which function is run
        if x == '1':
            step[len(step) - 1].location = auto.position()
            step[len(step) - 1].move = 1
            print(step[len(step) - 1].location)
            
        elif x == '2': 
            step[len(step) - 1].location = auto.position()
            step[len(step) - 1].doubleclick = 1
                
        elif x == '3': 
            step[len(step) -1].message = input('Enter a message to print: ')
            step[len(step) - 1].pri = 1
                
        elif x == '4': 
            step[len(step) - 1].enter = 1
                         
                         
        elif x == '5': 
            step[len(step) - 1].dateTime = 1
    
        elif x == '6': 
            step[len(step) - 1].ctrlA = 1
    
        elif x == '7': 
            step[len(step) - 1].ctrlC = 1
    
        elif x == '8': 
            step[len(step) - 1].ctrlV = 1
                         
        elif x == '9': 
            step[len(step) - 1].progPause = 1
            step[len(step) - 1].sleeper = input('Enter the amount of time to pause: ')
            
        elif x == 's':
            with open('Saved_steps.pkl', 'wb') as output:
                for g in range(len(step)-1):
                    pickle.dump(step[g], output, pickle.HIGHEST_PROTOCOL)
        
        elif x == '10': 
            step[len(step) - 1].image_found = 1
                    
        elif x == 'rs':
            rs = 1
            break
                
        #breaks the loop when the user wants to run the steps         
        elif x == 'r':
            break
            
        else:
            print('\n\n**Please select a valid option**\n\n')
    ############################################################################end
    
    
    
    
    
    
    
    
    if rs !=1:        
        l = input('How many times would you like these steps to run?\n') or '1'
        input('Press enter to start saved profile\n')

    while True and rs != 1:    
        for n in range(int(l)): #determines how many times the steps are run
            for i in range(int(len(step) - 1)): #this loop call each step object sequentially
                print("Step:", i + 1,",", "Loop count:" , n+1, )
                step[i].doStuff() 
        br = input('Would you like to run the steps again: y/n')
        if br == 'n':
            break
    
    #used to run saved profile
    if rs == 1:
        redo = input('How many times would you like these steps to run?\n' ) or 1
        input('Press enter to start saved profile\n')
        for q in range(int(redo)):
          
            stepsFromSaved = []
            b = 0
            with open('Saved_steps.pkl', 'rb') as i:
                while True:
                        
                    stepsFromSaved.append(None)
                    try:
                        stepsFromSaved[b] = pickle.load(i)
                    except EOFError:
                           break
                    b += 1
                        
                for g in range(len(stepsFromSaved) - 1):
                    stepsFromSaved[g].doStuff()
                    print('Step: ', g+1, ' loop: ', q+1)
                    
                    
    endProgram = input('\nWould you like to run the program again? y\\n: '.center(40))
    if endProgram == 'n':
        break
                    
print('\nEnd of program')     
    
