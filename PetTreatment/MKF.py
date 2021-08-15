    
import csv

table1 = []
table2 = []
table3 = []


def table_file(tbl):
   
    if tbl == 1:
        return "DADSA 2019-20 CWK A DATA PETS.csv"
        
    if tbl == 2:
        return "DADSA 2019-20 CWK A TREATMENT.csv"
        
    if tbl == 3:
        return "DADSA 2019-20 CWK A WILD ANIMALS.csv"
        
def table_array(which_table):
    if which_table == 1:
        return table1
    if which_table == 2:
        return table2
    if which_table == 3:
        return table3

def merge_animal():
    return table_array(1)+table_array(3)

def loadTestingData():
    
    global table1
    global table2
    global table3
    
    table1 = []
    table2 = []
    table3 = []
      
    with open(table_file(1),'rt') as f:
        f = csv.reader(f,skipinitialspace=True)   
        for line in f:
            table1.append(line)

    with open(table_file(2),'rt') as f:
        f = csv.reader(f,skipinitialspace=True)     
        for line in f:     
            table2.append(line)

    with open(table_file(3),'rt') as f:
        f = csv.reader(f,skipinitialspace=True)
        next(f)
        for line in f:  
            table3.append(line)

    for i in range(len(table3)):   
        table3[i].insert(2," ")
        table3[i].insert(4," ")
        table3[i].insert(5," ")

def matchData(row,col):  #row from table(pet&wild) #col from table2
    for j in range(1,len(table2)):
        if merge_animal()[row][0] == table2[j][0]:
            return table2[j][col]
############## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def matchData2toAll(row,col):
    for j in range(1,len(merge_animal())):
        if table2[row][0] == merge_animal()[j][0]:
            return merge_animal()[j][col]
   ############### >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def mBoAni(line):
    print("\n【"+str(line)+"】Sanctuary Identification:  ◄",merge_animal()[line][0],"►",
    "\n  |  |----Type:-----------------",merge_animal()[line][1],
    "\n  |  |----Breed:----------------",merge_animal()[line][2],
    "\n  |  |----Vaccinated:-----------",merge_animal()[line][3],
    "\n  |  |----Neutered:-------------",merge_animal()[line][4],
    "\n  |  |----Microchip Number:-----",merge_animal()[line][5],
    "\n  |  |----Reason for admission:-",merge_animal()[line][6],
    "\n  |  |----Date of Arrival:------",merge_animal()[line][7],
    "\n  |  |----Date of Departure:----",merge_animal()[line][8],
    "\n  |  |----Destination:----------",merge_animal()[line][9],
    "\n  |  |----Destination Address:--",merge_animal()[line][10],
    "\n  |----ID:----------------------",matchData(line,0),
    "\n  |----Surgery:-----------------",matchData(line,1),
    "\n  |----Surgery Date:------------",matchData(line,2),
    "\n  |----Medication:--------------",matchData(line,3),
    "\n  |----Medication Start:--------",matchData(line,4),
    "\n  |----Medication Finish:-------",matchData(line,5),
    "\n  |----Responsible for Abuse:---",matchData(line,6),
    "\n  |----Responsible for Abandon:-",matchData(line,7),
    "\n")
    
def mBoTreatment(line):   #compare id surgery and id sec
    print("【"+str(line)+"】Sanctuary Identification:  ◄",matchData2toAll(line,0),"►",
    "\n  |  |----Type:-----------------",matchData2toAll(line,1),
    "\n  |  |----Breed:----------------",matchData2toAll(line,2),
    "\n  |  |----Vaccinated:-----------",matchData2toAll(line,3),
    "\n  |  |----Neutered:-------------",matchData2toAll(line,4),
    "\n  |  |----Microchip Number:-----",matchData2toAll(line,5),
    "\n  |  |----Reason for admission:-",matchData2toAll(line,6),
    "\n  |  |----Date of Arrival:------",matchData2toAll(line,7),
    "\n  |  |----Date of Departure:----",matchData2toAll(line,8),
    "\n  |  |----Destination:----------",matchData2toAll(line,9),
    "\n  |  |----Destination Address:--",matchData2toAll(line,10),
    "\n  |----ID:----------------------",table_array(2)[line][0],
    "\n  |----Surgery:-----------------",table_array(2)[line][1],
    "\n  |----Surgery Date:------------",table_array(2)[line][2],
    "\n  |----Medication:--------------",table_array(2)[line][3],
    "\n  |----Medication Start:--------",table_array(2)[line][4],
    "\n  |----Medication Finish:-------",table_array(2)[line][5],
    "\n  |----Responsible for Abuse:---",table_array(2)[line][6],
    "\n  |----Responsible for Abandon:-",table_array(2)[line][7],
    "\n")
    
def mBoAnimals():
    
    loadTestingData()
    thisa = a()
    for row in range(1,len(merge_animal())): 
        print("【"+str(row)+"】Sanctuary Identification:  ◄",merge_animal()[row][0],"►",
        "\n  |  |----Type:-----------------",merge_animal()[row][1],
        "\n  |  |----Breed:----------------",merge_animal()[row][2],
        "\n  |  |----Vaccinated:-----------",merge_animal()[row][3],
        "\n  |  |----Neutered:-------------",merge_animal()[row][4],
        "\n  |  |----Microchip Number:-----",merge_animal()[row][5],
        "\n  |  |----Reason for admission:-",merge_animal()[row][6],
        "\n  |  |----Date of Arrival:------",merge_animal()[row][7],
        "\n  |  |----Date of Departure:----",merge_animal()[row][8],
        "\n  |  |----Destination:----------",merge_animal()[row][9],
        "\n  |  |----Destination Address:--",merge_animal()[row][10],
        "\n  |----ID:----------------------",matchData(row,0),
        "\n  |----Surgery:-----------------",matchData(row,1),
        "\n  |----Surgery Date:------------",matchData(row,2),
        "\n  |----Medication:--------------",matchData(row,3),
        "\n  |----Medication Start:--------",matchData(row,4),
        "\n  |----Medication Finish:-------",matchData(row,5),
        "\n  |----Responsible for Abuse:---",matchData(row,6),
        "\n  |----Responsible for Abandon:-",matchData(row,7)
        )   
        
        for i in range(len(thisa)):
            if merge_animal()[row][0] == thisa[i][0]:
                print("-----------------------------------------------------------TWICE------",
                "\n  |----ID:----------------------",thisa[i][0],
                "\n  |----Surgery:-----------------",thisa[i][1],
                "\n  |----Surgery Date:------------",thisa[i][2],
                "\n  |----Medication:--------------",thisa[i][3],
                "\n  |----Medication Start:--------",thisa[i][4],
                "\n  |----Medication Finish:-------",thisa[i][5],
                "\n  |----Responsible for Abuse:---",thisa[i][6],
                "\n  |----Responsible for Abandon:-",thisa[i][7]
                )
        print("")

def a():                                                                        #search animal repeated only twice
    loadTestingData()
    temp = []
    for i in range(1,len(table2[0])):
        for j in range(i+1,len(table2)):
            if table2[i][0] == table2[j][0]:  
                temp.append(table2[j]) 
    return temp

############################----method return ----###################################

def check_Yes_No(enter):
    if enter=='yes' or enter=='Yes' or enter=='y' or enter=='Y' or enter=='YES': 
        return "Yes"
    elif enter=='no' or enter=='No' or enter=='n' or enter=='N'or enter=='NO':
        return "No"
    else:
        return False

def ID_checker(tbl,ID):
    loadTestingData()
    
    if tbl == '13L':#--------------------------------------1+3
        for line in range(1,len(merge_animal())):
            if ID == merge_animal()[line][0]:
                return line
    elif tbl == '13B':          #return true false
        for i in range(1,len(merge_animal())):
            if ID == merge_animal()[i][0]:
                return True
    elif tbl == '1L':#-----------------------------------------1
        for line in range(1,len(table_array(1))):
            if ID == table_array(1)[line][0]:
                return line
    elif tbl == '1B':          #return true false
        for i in range(1,len(table_array(1))):
            
            if ID == table_array(1)[i][0]:
                return True
    elif tbl == '2L':#------------------------------------------2
        for line in range(1,len(table_array(2))):
            if ID == table_array(2)[line][0]:
                return line
    elif tbl == '2B':
        for i in range(1,len(table_array(2))):
            if ID == table_array(2)[i][0]:
                return True
    elif tbl == '3L':#------------------------------------------3
        for line in range(len(table_array(3))):
            if ID == table_array(3)[line][0]:
                return line
    elif tbl == '3B':
        for i in range(len(table_array(3))):
            if ID == table_array(3)[i][0]:
                return True
    else:
        return False

def list_ele_match(which_string,which_col,which_col_2): 
    loadTestingData()
    temp_array = []
    for i in range(1,len(merge_animal())):
        if which_string in merge_animal()[i][which_col]:
            for j in range(1,len(table2)):
                if merge_animal()[i][0] == table2[j][0]:
                    temp_array.append(table2[j][which_col_2])
    print(ETF.RmDupSrt(temp_array),"\n")
  
def list_ani_adopt(which_string):
    loadTestingData()
    temp_array = []
    for i in range(1,len(merge_animal())):
        if merge_animal()[i][1] == which_string :
            if (bool(merge_animal()[i][3]) and bool(merge_animal()[i][4] and bool(merge_animal()[i][5]))) == True:
                temp_array.append(merge_animal()[i][0])
    temp = ETF.Sorting(temp_array)  

    for i in range(len(temp)):
        temp_Bo = mBoAni(ID_checker('13L',temp[i]))
    return temp_Bo

def list_ani_return_funct(temp_array):
    
    loadTestingData() 
    tempAfter =[]
    #print(temp_array)
    for i in range(1,len(merge_animal())): 
        for j in range(len(temp_array)):
            if temp_array[j] in merge_animal()[i][9]:
                tempAfter.append(merge_animal()[i][0])
    tempAfter = ETF.Sorting(tempAfter)  
    #print("temp: ",tempAfter)
    for i in range(len(tempAfter)):
        temp_Bo = mBoAni(ID_checker('13L',tempAfter[i]))
    return temp_Bo 
    
###############################__method not return__##################################
def list_data_ID(ID):   #===> list_ID()
    
    if ID_checker('13B',ID) == True:
        print("\nLoading data from ID",ID,"...\n")
        line = ID_checker('13L',ID)
        mBoAni(line)
    #elif ID_checker('3B',ID) == True:
        #line = ID_checker('3L',ID)
        #mBoAni(line)
    else:
        print("Cannot find that ID",ID)
def check_entry(tbl,nameObj):
    newEntry = []
    for i in range(len(nameObj)):
        enter = input("Enter "+nameObj[i]+": ")
        newEntry.append(enter)
    if tbl == 1 or tbl == 3:
        if newEntry[3] != check_Yes_No(newEntry[3]):
            newEntry.remove(newEntry[3])
            newEntry.remove(newEntry[3])
            enter = "Enter Only Yes/No"
            
            newEntry.insert(3,enter)
            newEntry.insert(4,enter)
        else:
            return "Enter Only Yes/No"
    return newEntry
            

def rt_new_line(tbl,nameObj):
    loadTestingData()
    
    newEntry = check_entry(tbl,nameObj)
    
    aID = []
    bID = []
    for a in range(1,len(merge_animal())):
            aID.append(merge_animal()[a][0])
        
    for b in range(1,len(table_array(2))):
            bID.append(table_array(2)[b][0])      
    
    
        
    if tbl == 1:  
        if newEntry[0] not in aID: 
            with open(table_file(tbl),'a',newline='') as f_out:
                wrt=csv.writer(f_out)
                wrt.writerow(newEntry) 
            #set it added then call its index to print only this entry    
            table_array(tbl).append(newEntry)
            line = table_array(tbl).index(newEntry)
            return line #return index that line
        else:    
            return False
            
        
    elif tbl == 2:
        print(newEntry)
        if newEntry[0] not in bID:
            if newEntry[0] in aID:
                with open(table_file(2),'a',newline='') as f_out:
                    wrt=csv.writer(f_out)
                    wrt.writerow(newEntry) 
                #set it added then call its index to print only this entry    
                table_array(tbl).append(newEntry)
                line1 = table_array(tbl).index(newEntry)
                
                return line1 #return index that line

        else:   
            return False
        
    elif tbl == 3:
        if newEntry[0] not in aID:
            newEntry.remove(newEntry[2])
            newEntry.remove(newEntry[3])
            newEntry.remove(newEntry[3]) 
            with open(table_file(tbl),'a',newline='') as f_out:
                wrt=csv.writer(f_out)
                wrt.writerow(newEntry)   
            newEntry.insert(1,"")
            newEntry.insert(4,"")
            newEntry.insert(5,"")
            
            table_array(tbl).append(newEntry)
            line = merge_animal().index(newEntry)
            return line #return index that line
        else:  
            return False
    
    


def write_entry(tbl):    
    if tbl == 1 or tbl ==3:
        print("\nChoose table",tbl,"successfully")
        nameObj = ["Sanctuary Identification","Type","Breed","Vaccinate","Neutered","Mircochip","Reason for admission","Date of Arrival","Date of Departure","Destination","Destination Address"]
        line = rt_new_line(tbl,nameObj)
        
        if line != False:
            print("\n")
            mBoAni(line)
            ans = input("Do you want add its treatment? Yes/No (y/n): ")
            if check_Yes_No(ans) == 'Yes' :
                nameObj1 = ["Sanctuary Identification","Surgery","Surgery Date","Medication","Medication Start","Medication Finish","Responsible for Abusing","Responsible for Abandoning"]
                line1 = rt_new_line(2,nameObj1)
                if line1 != False:  #error not match with "ID above when iput same time"
                                    # only show ID match with exist ID in array
                    if ID_checker('2B',table_array(2)[line1][0]) == True:
                        print("\n")
                        mBoTreatment(line1)
                        print("Added treatment that animal successfully")
                    else: # A not same ID with B
                        print("\nTreatmentID not match AnimalID, Please check!")
                else: # same treatment ID
                    print("\nAdded only Animal because Treatment ID from file already exist!!!\nDo you want edit?\n")
                    mBoAni(line)  
            else: #chose NO
                print("\nAnimal without Treatment added\n")
                mBoAni(line) 
        else: # same Id animal
            print("\nPlease input same ID animal above!!!\n")
    else: #only choose option 1 and 3, if not:
        print("\nPlease choose table 1 (Pet) or table 3 (Wild animal)\n")
        
def ovwrt_ele(tbl,which_row,which_col,enter):   #edit ele #make temptable overwrite old one
   
    temp_table = []
    
    with open(table_file(int(tbl)),'rt') as f:
        
        f = csv.reader(f)
        for line in f:     
            temp_table.append(line)
   
    temp_table[int(which_row)].pop(int(which_col))
    temp_table[int(which_row)].insert(int(which_col),enter)

    return temp_table
        
def ovwrt_ele_details(which_table,which_row,which_col,enter):   #compare ID and edit ele
    #loadTestingData()

    if which_table == 1:
        
        temp_table = ovwrt_ele(1,which_row,which_col,enter)
     

        wrt=csv.writer(open(table_file(int(which_table)),'w', newline=''))
        wrt.writerows(temp_table) 
        
        table_array(1)[int(which_row)].pop(int(which_col))
        table_array(1)[int(which_row)].insert(int(which_col),enter)
        
        return mBoAni(which_row)
            
    elif which_table == 3:

        temp_table = ovwrt_ele(3,which_row,which_col,enter)


        wrt=csv.writer(open(table_file(int(which_table)),'w', newline=''))
        wrt.writerows(temp_table) 

        if which_col >= 3:
            #wrong when input vaccinated, but still right in csv file
            table_array(3)[int(which_row)-1].pop(int(which_col)+3)
            table_array(3)[int(which_row)-1].insert(int(which_col)+3,enter)
            
        elif which_col == 2:
            table_array(3)[int(which_row)-1].pop(int(which_col)+1)
            table_array(3)[int(which_row)-1].insert(int(which_col)+1,enter)
        else:
            table_array(3)[int(which_row)-1].pop(int(which_col))
            table_array(3)[int(which_row)-1].insert(int(which_col),enter)
            
        return mBoAni(which_row-1+len(table_array(1)))   #only right in csv file
            
    elif which_table == 2:
        
        temp_table = ovwrt_ele(2,which_row,which_col,enter)

        wrt=csv.writer(open(table_file(int(which_table)),'w', newline=''))
        wrt.writerows(temp_table) 

        table_array(2)[int(which_row)].pop(int(which_col))
        table_array(2)[int(which_row)].insert(int(which_col),enter)
        
        return mBoTreatment(which_row)

def input_date_funct():

    dd = int(input("Enter day: "))
    mm = int(input("Enter month: "))
    yyyy = int(input("Enter year: "))
    return ETF.dateChecker(dd,mm,yyyy)
 


    
def edit_arrival_funct(rowID):
    
    if ID_checker('1B',rowID) == True:    
        line = ID_checker('1L',rowID)   
        print("\nEnter Date of Arrival")
        ovwrt_ele_details(1,line,7,input_date_funct()) 
        
    elif ID_checker('3B',rowID) == True:    
        line = ID_checker('3L',rowID)+1
        print("\nEnter Date of Arrival")   
        ovwrt_ele_details(3,line,4,input_date_funct()) #4 real col
        
    else:
        print("\nPlease only input ID of Pet or Wild to edit Arrival")
    
def edit_departure_funct(rowID):
    #rowID = input("Enter ID need to be edited Departure: ")
    if ID_checker('1B',rowID) == True:    
        line = ID_checker('1L',rowID)
        print("\nEnter Date of Departure")
        ovwrt_ele_details(1,line,8,input_date_funct()) 
        
    elif ID_checker('3B',rowID) == True:    
        line = ID_checker('3L',rowID)+1  
        print("\nEnter Date of Departure")
        ovwrt_ele_details(3,line,5,input_date_funct()) #5 real col
        
    else:
        print("\nPlease only input ID of Pet or Wild to edit Departure")



def edit_destination_funct(rowID):#pet+wild
    #rowID = input("Enter ID need to be edited Destination: ")
    if ID_checker('1B',rowID) == True:    
        line = ID_checker('1L',rowID)
        enter = input("Enter Destination: ")
        ovwrt_ele_details(1,line,9,enter) 
        
    elif ID_checker('3B',rowID) == True:    
        line = ID_checker('3L',rowID)+1
        enter = input("Enter Destination: ")
        ovwrt_ele_details(3,line,6,enter) 
        
    else:
        print("\nPlease only input ID of Pet or Wild to edit Destination")
    
def edit_address_funct(rowID): #---> editAddress()

    if ID_checker('1B',rowID) == True:    
        line = ID_checker('1L',rowID)
        enter = input("Enter Address: ")
        ovwrt_ele_details(1,line,10,enter) 
        
    elif ID_checker('3B',rowID) == True:    
        line = ID_checker('3L',rowID)+1
        enter = input("Enter Address: ")
        
        print("line:",line)
        
        ovwrt_ele_details(3,line,7,enter) 
        
    else:
        print("\nPlease only input ID of Pet or Wild to edit Address")

######################____HERE___####################################        
def list_ID():          #<=== list_data_ID(ID)
    
    ask = input("Do you want to search specific ID? (y/n) ")
    if check_Yes_No(ask) == 'Yes':
        ID = input("Enter ID: ")
        list_data_ID(ID)
    
def list_ppl_abused():
    
    print("---------list of Identified people that have Abused animals:---------\n")
    list_ele_match("Abused",6,6)

def list_ppl_abandoned():
    
    print("---------list of Identified people that have Abandoned animals:---------\n")
    list_ele_match('Abandoned',6,7)

def list_cat_adopt():
    
    print("---------list of CATs are ready for adoption:---------")
    list_ani_adopt("Cat")
    
def list_dog_adopt():    
               
    print("---------list of DOGs are ready for adoption:---------")
    list_ani_adopt("Dog")
    
def list_ani_return():
    print("---------list of Animals are ready to be returned:---------")
    temp_array = ["return","zoo"]
    list_ani_return_funct(temp_array)
    
def add_new_line():
    input_table = int(input("Which table need new entry (1: Pet & 3: Wild): "))
    write_entry(input_table)

def add_new_pet():
    print("Adding new pet ...")
    write_entry(1)
    
def add_new_wild():
    print("Adding new wild ...")
    write_entry(3)  

def edit_ID():
    rowID = input("Enter ID need to be set up new ID: ")
    list_data_ID(rowID)
    if ID_checker('1B',rowID) == True:
        enter = input("Enter new ID for pet: ")
        line = ID_checker('1L',rowID)
        ovwrt_ele_details(1,line,0,enter) 
        if ID_checker('2B',rowID) == True:
            line = ID_checker('2L',rowID)
            print("Updating............")
            ovwrt_ele_details(2,line,0,enter)
        else:
            print("There is no Treatment ID exist for that pet")
    elif ID_checker('3B',rowID) == True:
        enter = input("Enter new ID wild animal: ")
        line = ID_checker('3L',rowID)+1
        ovwrt_ele_details(3,line,0,enter)
        if ID_checker('2B',rowID) == True:
            line = ID_checker('2L',rowID)
            print("Updating............")
            ovwrt_ele_details(2,line,0,enter)
        else:
            print("There is no Treatment ID exist for that wild animal")
    else:
        print("\nPlease only input ID of Pet or Wild to set up new ID")
       
def edit_type():
    rowID = input("Enter ID need to be edited Type: ")
    
    list_data_ID(rowID)
    if ID_checker('1B',rowID) == True:
        enter = input("Enter pet Type: ")
        line = ID_checker('1L',rowID)
        ovwrt_ele_details(1,line,1,enter) 
    elif ID_checker('3B',rowID) == True:
        enter = input("Enter wild animal Type: ")
        line = ID_checker('3L',rowID)+1
        ovwrt_ele_details(3,line,1,enter)
    else:
        print("\nPlease only input ID of Pet or Wild to edit Type")

def edit_breed(): 
    rowID = input("Enter ID need to be edited Breed: ")
    list_data_ID(rowID)
    if ID_checker('1B',rowID) == True:
        line = ID_checker('1L',rowID)
        enter = input("Enter pet's Breed: ")
        ovwrt_ele_details(1,line,2,enter)
        
    else:
        print("Only Pet has Breed to edit") 
        
def edit_vaccinated():  
    rowID = input("Enter ID need to be edited Vaccinated: ")
    
    list_data_ID(rowID)
    if ID_checker('1B',rowID) == True:
        enter = input("Enter pet Vaccinated (Yes/No): ")
        line = ID_checker('1L',rowID)
        ovwrt_ele_details(1,line,3,check_Yes_No(enter)) 
    elif ID_checker('3B',rowID) == True:
        enter = input("Enter wild animal Vaccinated (Yes/No): ")
        line = ID_checker('3L',rowID)+1
        ovwrt_ele_details(3,line,2,check_Yes_No(enter))
    else:
        print("\nPlease only input ID of Pet or Wild to edit Vaccinated")
        
def edit_neutered():
    rowID = input("Enter ID need to be edited Neutered: ")
    
    if ID_checker('1B',rowID) == True:
        list_data_ID(rowID)
        line = ID_checker('1L',rowID)
        #print("That row table1 is",line)
        enter = input("Enter Neutered (Yes/No): ")    
        ovwrt_ele_details(1,line,4,check_Yes_No(enter))
    else:
        print("Only Pet has Neutered to edit")
    
        
def edit_microchip(): 
    rowID = input("Enter ID need to be edited Mircochip: ")
    list_data_ID(rowID)
    if ID_checker('1B',rowID) == True:
        line = ID_checker('1L',rowID)
        #print("That row table1 is",line)
        enter = input("Enter Mircochip number: ")
        ovwrt_ele_details(1,line,5,enter)
    else:
        print("Only Pet has Mircochip to edit")  
        
def edit_reason_admiss():
    rowID = input("Enter ID need to be edited reason: ")
    
    list_data_ID(rowID)
    if ID_checker('1B',rowID) == True:
        enter = input("Enter reason for admiss pet: ")
        line = ID_checker('1L',rowID)
        ovwrt_ele_details(1,line,6,enter) 
    elif ID_checker('3B',rowID) == True:
        enter = input("Enter reason for admiss wild animal: ")
        line = ID_checker('3L',rowID)+1
        ovwrt_ele_details(3,line,3,enter)
    else:
        print("\nPlease only input ID of Pet or Wild to edit reason for admission")  
        
def edit_arrival():
    rowID = input("Enter ID need to be edited Arrival: ")
    list_data_ID(rowID)
    edit_arrival_funct(rowID)
        
def edit_departure():
    rowID = input("Enter ID need to be edited Departure: ")
    list_data_ID(rowID)
    edit_departure_funct(rowID)
    
def edit_destination():
    rowID = input("Enter ID need to be edited Destination: ")
    list_data_ID(rowID)
    edit_destination_funct(rowID)
    
def edit_address():
    rowID = input("Enter ID need to be edited Address: ")
    list_data_ID(rowID)
    edit_address_funct(rowID)
    
def edit_surgery():
    rowID = input("Enter ID need to be edited Surgery: ")
    list_data_ID(rowID)
    if ID_checker('2B',rowID) == True:
        line = ID_checker('2L',rowID)
        #print("That row is",line)
        enter = input("Enter Surgery: ")
        ovwrt_ele_details(2,line,1,enter)
    else:
        print("\nThat animal have no treatment\nPlease check again!")
        
def edit_surgery_date():
    rowID = input("Enter ID need to be edited Surgery Date: ")
    list_data_ID(rowID)
    if ID_checker('2B',rowID) == True:    
        line = ID_checker('2L',rowID)   
        print("\nEnter Surgery Date, please")
        ovwrt_ele_details(2,line,2,input_date_funct()) 
    else:
        print("\nThat animal have no treatment\nPlease check again!")
        
def edit_medication():
    rowID = input("Enter ID need to be edited Medication: ")
    list_data_ID(rowID)
    if ID_checker('2B',rowID) == True:
        line = ID_checker('2L',rowID)
        #print("That row is",line)
        enter = input("Enter Medication: ")
        ovwrt_ele_details(2,line,3,enter)
    else:
        print("\nThat animal have no treatment\nPlease check again!")  
    
def edit_medication_start():
    rowID = input("Enter ID need to be edited Medication-start Date: ")
    list_data_ID(rowID)
    if ID_checker('2B',rowID) == True:    
        line = ID_checker('2L',rowID)   
        print("\nEnter Medication-start Date please")
        ovwrt_ele_details(2,line,4,input_date_funct()) 
    else:
        print("\nThat animal have no treatment\nPlease check again!")
 
def edit_medication_finish():
    rowID = input("Enter ID need to be edited Medication-finish Date: ")
    list_data_ID(rowID)
    if ID_checker('2B',rowID) == True:    
        line = ID_checker('2L',rowID)   
        print("\nEnter Medication-finish Date, please")
        ovwrt_ele_details(2,line,5,input_date_funct()) 
    else:
        print("\nThat animal have no treatment\nPlease check again!")
        
def edit_ppl_abused():
    rowID = input("Enter ID need to be edited ID people for abusing: ")
    list_data_ID(rowID)
    if ID_checker('2B',rowID) == True:
        line = ID_checker('2L',rowID)
        #print("That row is",line)
        enter = input("Enter people ID: ")
        ovwrt_ele_details(2,line,6,enter)
    else:
        print("\nThat animal have no treatment\nPlease check again!")
    
def edit_ppl_abandoned():
    rowID = input("Enter ID need to be edited ID people for abandoning: ")
    list_data_ID(rowID)
    if ID_checker('2B',rowID) == True:
        line = ID_checker('2L',rowID)
        #print("That row is",line)
        enter = input("Enter people ID: ")
        ovwrt_ele_details(2,line,7,enter)
    else:
        print("\nThat animal have no treatment\nPlease check again!")
        
 ############################__EXTERNAL_FUNCT__####################
   
class ETF:
    
    def RemoveDup(array): 
        Dup_list = [] 
        for num in array: 
            if num not in Dup_list: 
                Dup_list.append(num) 
        return Dup_list 
    
    def Sorting(array):
        Sort_list = []   
        while array:
            smallest = min(array)
            Sort_list.append(smallest)
            array.pop(array.index(smallest))
        return Sort_list
        
    def RmDupSrt(array):        #combine RemoveDup+Sorting = RmDupSrt
        return ETF.RemoveDup(ETF.Sorting(array))
        
    

    def dateChecker(dd,mm,yyyy):
        mmList_31=["1","3","5","7","8","10","12"]
        mmList_30=["4","6","7","9","11"]
        
        if yyyy in range(2000,2020):
            if str(mm) in mmList_31:
                if dd in range(1,31):
                    return str(dd)+"/"+str(mm)+"/"+str(yyyy)
                else:
                    return "Wrong day"
            elif str(mm) in mmList_30:
                if dd in range(1,30):
                    return str(dd)+"/"+str(mm)+"/"+str(yyyy)
                else:
                    return "Wrong day"
            elif mm == 2:
                if yyyy % 4 == 0 and (yyyy % 100 != 0 or yyyy % 400 == 0):
                    if dd in range(1,29):
                        return str(dd)+"/"+str(mm)+"/"+str(yyyy)
                    else:
                        return "Leap year has limit 29 days"
                else:
                    if dd in range(1,28):
                        return str(dd)+"/"+str(mm)+"/"+str(yyyy)
                    else:
                        return "Wrong day"
            else:
                return "Wrong month"
        else:
            return "Wrong year"

 
    
    ############################___MAIN___####################



    