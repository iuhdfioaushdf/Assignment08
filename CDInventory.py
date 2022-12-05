#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# EPales, 12/4/2022, updating code to complete assignment
#------------------------------------------#

# -- DATA -- #
strChoice = ''
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
lstTbl = [] 
dicRow = {}
objFile = None

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    def ask_entry (element = None, table = None):
        
        
        if element == None:
            print ('Nothing to be added to table')
        
        elif table == None:
            print ('No information to be added')
            
        else:
            table.append (element)



# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    #load_inventory = open('cdInventory.txt', 'a+')

    @staticmethod
    def read_file(file_name, table):
       """Function to manage data ingestion from file to a list of dictionaries

       Reads the data from file identified by file_name into a 2D table
       (list of dicts) table one line in the file represents one dictionary row in table.

       Args:
           file_name (string): name of file used to read the data from
           table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

       Returns:
           None.
       """
       table.clear()  # this clears existing data and allows to load data from file
       try:
           with open(file_name, 'r') as fileObj:
               table = fileObj.read()
           return table
       except FileNotFoundError as e:
           print('Data file does not exist')
           print(e.__doc__)
       except Exception as e:
           print('General Error')
           print(e.__doc__)
       return table    

    @staticmethod
    def write_file(file_name, table):
       """ Function to write data to file in binary listed from input from user
       
       Reads the data from input storing it in memory (lstTbl) until either 
       contents are written to file or erased from memory.
       
       Args:
           table (lstTbl) to have it's contents emptied and written to file
           
       Returns:
           choice (string) asking if input saved to memory shall be written to
           file (CDInventory.dat)
       """
       
       try:
           with open(file_name, 'a+') as fileObj: ## Don't need to close file since "with" is being used.
               table = fileObj.write()
           return table    
       except FileNotFoundError as e:
           print("Data file does not exist")
           print(e.__doc__)
       except Exception as e:
           print('General Error')
           print(e.__doc__)
       return table
    


# -- PRESENTATION (Input/Output) -- #
class IO:
    
    """Handling Input / Output"""

    @staticmethod
    def if_yes (query, action, *parms):
        work_done = False
        
        try:
            while True:
                questionAnswer = input(query).strip().lower()
                if questionAnswer == 'y':
                    action (*parms)
                    work_done = True
                    break

                elif questionAnswer == 'n':
                    break

                else:
                    print ('Incorrect answer')
        except:
            pass

        return work_done            

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

    Args:
        None.

    Returns:
        None.
    """

    print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

    Args:
        None.

    Returns:
        choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

    """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


    Args:
        table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

    Returns:
        None.

    """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')


    @staticmethod
    def rem_inv(file_name): 
        """Asks for user input to remove an entry from file (CDInventory.dat)   
    
    Args:
        file(file_name) is called when user asks to delete items listed in file 
        
    
    Returns:
        choice to view contensts of file and then to input which row to remove from file
    
    """
    #elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
            IO.show_inventory(lstTbl)
            
    @staticmethod
    def add_cd():
        """Function to ask for new inventory
       
       Asks for the input of new inventory by calling for two strings and an integer
       
       Args:
           strID: Integer used for ID header/column
           strTitle: String used for title header/column
           strArtist: String used for artist header/column
           
       Returns:
           choice (string) asks for inputs in string format to add to cd
        """
        ID = None
        title = None
        artist = None
              
        try:
            while True:
                cd_id = input('Enter ID: ').strip()
                try:
                    ID = int(cd_id)
                            
                            
                except:
                    print ('\'{}\' is not a number. Please enter a number.'.format (ID))
                    continue
                        
                        
                    break
                    
            title = ''
            while(not title):
                title = input('Enter album title: ').strip()
                        
            artist = ''
            while(not artist):
                artist = input('Enter the artist: ').strip()
        except: 
            print ('There was an error, closing program')
        return ID, title, artist
                  


# -- Main Body of Script -- #
# 1. When program starts, read in the currently saved Inventory
lstTbl = FileIO.read_file(strFileName, lstTbl)



# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:  ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileIO.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        intID, strTitle, strArtist = IO.add_cd ()
        if ((intID is None) or (strTitle is None) or (strArtist is None)):
            IO.if_yes ('Save current inventory to file? [y/n] ',
                           FileIO.write_file, strFileName, lstTbl)
            break
        
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        IO.add_cd (dicRow, lstTbl)
        IO.show_inventory(lstTbl)
        
        # 3.3.2 Add item to the table
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except ValueError as e: 
            print('this is not a number')
        except Exception as e:
            print('general error')
        else:
            blnCDRemoved = IO.remove_CD()
            if blnCDRemoved:
                print('The CD was removed')
            else:
                print('could not find this CD!')
                
        # 3.5.2 search thru table and delete CD
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.write_file(strFileName, lstTbl)   
        else:
                  input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')
