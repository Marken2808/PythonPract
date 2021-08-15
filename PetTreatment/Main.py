import sys
import MKF


#MAIN MENU
def mainMenu():
    menu = [" ►► 1: Load All Data ◄◄ │ ►► 2: Add New Record ◄◄ │ ►► 3: Edit Data ◄◄ "]
    menu1= [" ►► 4: Produce List  ◄◄ │ ►► 0: Exit ◄◄ "]
    print("\t\t\t\t\t\t\t\t      ▄▄▄▄▄▄▄▄▄▄▄")
    print("\t\t\t\t\t\t\t\t     ╔▌MAIN MENU▐╗")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print(menu)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print(menu1)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    
    c = int(input("➥Please give an option: "))
    if c == 1:
        print("\t\t\t—————————————▄▄▄————————————————")
        print("\t\t\tChose option ▌1▐ ►LOADING DATA◄")
        print("\t\t\t—————————————▀▀▀————————————————")
        
                
        MKF.mBoAnimals()
        MKF.list_ID()
        #print("⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶⇶")
        mainMenu()
    elif c == 2:
      
        print("\t\t\t—————————————▄▄▄————————————————————")
        print("\t\t\tChose option ▌2▐ ►ADDING NEW RECORD◄")
        print("\t\t\t—————————————▀▀▀————————————————————")
        addMenu()
    
    elif c == 3:
     
        print("\t\t\t—————————————▄▄▄———————————————")
        print("\t\t\tChose option ▌3▐ ►EDITING DATA◄")
        print("\t\t\t—————————————▀▀▀———————————————")
        editMenu()
        
    elif c == 4:
     
        print("\t\t\t—————————————▄▄▄—————————————————")
        print("\t\t\tChose option ▌4▐ ►PRODUCING LIST◄")
        print("\t\t\t—————————————▀▀▀—————————————————")
        produceMenu()
        
    elif c == 0:
        sys.exit()
        
    else:
        print("Error")
        
#ADD SUB MENU
def addMenu():
    menu = ["---1: Add new entry--- | ---2: Add new pet--- | ---3: Add new wild --- | ---0:Return to main---"]
    print("\t\t\t\t\t\t\t\t\t\t\t ╔════════╗")
    print("\t\t\t\t\t\t\t\t\t\t\t╔╣SUB MENU╠╗")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╩▬▬▬▬▬▬▬▬▬▬╩▬▬")
    print(menu)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    
    
    c = int(input("➥Please give an option: "))
    if c == 1:
        
        print("\t\t\t—————————————▄▄▄———————————————————")
        print("\t\t\tChose option ▌1▐ ►ADDING NEW ENTRY◄")
        print("\t\t\t—————————————▀▀▀———————————————————")
        MKF.add_new_line()
        addMenu()
        
    elif c == 2:
        
        print("\t\t\t—————————————▄▄▄—————————————————")
        print("\t\t\tChose option ▌2▐ ►ADDING NEW PET◄")
        print("\t\t\t—————————————▀▀▀—————————————————")
        MKF.add_new_pet()
        addMenu()
        
    elif c == 3:
        
        print("\t\t\t—————————————▄▄▄——————————————————")
        print("\t\t\tChose option ▌3▐ ►ADDING NEW WILD◄")
        print("\t\t\t—————————————▀▀▀——————————————————")
        MKF.add_new_wild()
        addMenu()
    
    else:
        mainMenu()

#EDIT SUB MENU
def editMenu():
    menu = [" 【1】:------Edit ID Animal-----| 【2】:-Edit Type Animal-| 【3】:---Edit Animal Breed----"]
    menu1 =[" 【4】:-----Edit Vaccinated-----| 【5】:--Edit Neutered---| 【6】:-----Edit Mircochip-----"]
    menu2 =[" 【7】:-------Edit Reason-------| 【8】:---Edit Arrival---| 【9】:-----Edit  Departure----"]
    menu3 =[" 【10】:----Edit Destination----| 【11】:--Edit Address---| 【12】:------Edit Surgery-----"]
    menu4 =[" 【13】:---Edit Surgery date----| 【14】:-Edit Medication-| 【15】:-Edit Medication start-"]
    menu5 =[" 【16】:-Edit Medication finish-| 【17】:-Edit ppl Abused-| 【18】:--Edit ppl Abandoned---"]
    
    editBo = [menu,menu1,menu2,menu3,menu4,menu5]
    
    
    print("\t\t\t\t\t\t\t\t\t      ╔════════╗")
    print("\t\t\t\t\t\t\t\t\t     ╔╣SUB MENU╠╗")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╩▬▬▬▬▬▬▬▬▬▬╩▬▬")
    for i in range(len(editBo)):
        print(editBo[i])
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


    c = int(input("➥Please give an option: "))
    
    if c == 1:
        print("\t\t\t—————————————▄▄▄————————————————————")
        print("\t\t\tChose option ▌1▐ ►EDITING ID ANIMAL◄")
        print("\t\t\t—————————————▀▀▀————————————————————")
        MKF.edit_ID()
        editMenu()
        
    elif c == 2:
        print("\t\t\t—————————————▄▄▄——————————————————————")
        print("\t\t\tChose option ▌2▐ ►EDITING TYPE ANIMAL◄")
        print("\t\t\t—————————————▀▀▀——————————————————————")
        MKF.edit_type()
        editMenu()
        
    elif c == 3:
        print("\t\t\t—————————————▄▄▄———————————————————————")
        print("\t\t\tChose option ▌3▐ ►EDITING ANIMAL BREED◄")
        print("\t\t\t—————————————▀▀▀———————————————————————")
        MKF.edit_breed()
        editMenu()
       
    elif c == 4:
        print("\t\t\t—————————————▄▄▄—————————————————————")
        print("\t\t\tChose option ▌4▐ ►EDITING VACCINATED◄")
        print("\t\t\t—————————————▀▀▀—————————————————————")
        MKF.edit_vaccinated()
        editMenu()
    
    elif c == 5:
        print("\t\t\t—————————————▄▄▄———————————————————")
        print("\t\t\tChose option ▌5▐ ►EDITING NEUTERED◄")
        print("\t\t\t—————————————▀▀▀———————————————————")
        MKF.edit_neutered()
        editMenu()
    
    elif c == 6:
        print("\t\t\t—————————————▄▄▄————————————————————")
        print("\t\t\tChose option ▌6▐ ►EDITING MICROCHIP◄")
        print("\t\t\t—————————————▀▀▀————————————————————")
        MKF.edit_microchip()
        editMenu()

    elif c == 7:
        print("\t\t\t—————————————▄▄▄———————————————————————————————")
        print("\t\t\tChose option ▌7▐ ►EDITING REASON FOR ADMISSION◄")
        print("\t\t\t—————————————▀▀▀——————————————————————————————")
        MKF.edit_reason_admiss()
        editMenu()
        
    elif c == 8:
        print("\t\t\t—————————————▄▄▄——————————————————")
        print("\t\t\tChose option ▌8▐ ►EDITING ARRIVAL◄")
        print("\t\t\t—————————————▀▀▀——————————————————")
        MKF.edit_arrival()
        editMenu()
        
    elif c == 9:
        print("\t\t\t—————————————▄▄▄————————————————————")
        print("\t\t\tChose option ▌9▐ ►EDITING DEPARTURE◄")
        print("\t\t\t—————————————▀▀▀————————————————————")
        MKF.edit_departure()
        editMenu()
        
    elif c == 10:
        print("\t\t\t—————————————▄▄▄▄——————————————————————")
        print("\t\t\tChose option ▌10▐ ►EDITING DESTINATION◄")
        print("\t\t\t—————————————▀▀▀▀——————————————————————")
        MKF.edit_destination()
        editMenu()
        
    elif c == 11:
        print("\t\t\t—————————————▄▄▄▄——————————————————")
        print("\t\t\tChose option ▌11▐ ►EDITING ADDRESS◄")
        print("\t\t\t—————————————▀▀▀▀——————————————————")
        MKF.edit_address()
        editMenu()

    elif c == 12:
        print("\t\t\t—————————————▄▄▄▄——————————————————")
        print("\t\t\tChose option ▌12▐ ►EDITING SURGERY◄")
        print("\t\t\t—————————————▀▀▀▀——————————————————")
        MKF.edit_surgery()
        editMenu()
        
    elif c == 13:
        print("\t\t\t—————————————▄▄▄▄———————————————————————")
        print("\t\t\tChose option ▌13▐ ►EDITING SURGERY DATE◄")
        print("\t\t\t—————————————▀▀▀▀———————————————————————")
        MKF.edit_surgery_date()
        editMenu()
        
    elif c == 14:
        print("\t\t\t—————————————▄▄▄▄—————————————————————")
        print("\t\t\tChose option ▌14▐ ►EDITING MEDICATION◄")
        print("\t\t\t—————————————▀▀▀▀—————————————————————")
        MKF.edit_medication()
        editMenu()
        
    elif c == 15:
        print("\t\t\t—————————————▄▄▄▄———————————————————————————")
        print("\t\t\tChose option ▌15▐ ►EDITING MEDICATION START◄")
        print("\t\t\t—————————————▀▀▀▀———————————————————————————")
        MKF.edit_medication_start()
        editMenu()
        
    elif c == 16:
        print("\t\t\t—————————————▄▄▄▄————————————————————————————")
        print("\t\t\tChose option ▌16▐ ►EDITING MEDICATION FINISH◄")
        print("\t\t\t—————————————▀▀▀▀————————————————————————————")
        MKF.edit_medication_finish()
        editMenu()
        
    elif c == 17:
        print("\t\t\t—————————————▄▄▄▄———————————————————————————")
        print("\t\t\tChose option ▌17▐ ►EDITING ID PEOPLE ABUSED◄")
        print("\t\t\t—————————————▀▀▀▀———————————————————————————")
        MKF.edit_ppl_abused()
        editMenu()
        
    elif c == 18:
        print("\t\t\t—————————————▄▄▄▄——————————————————————————————")
        print("\t\t\tChose option ▌18▐ ►EDITING ID PEOPLE ABANDONED◄")
        print("\t\t\t—————————————▀▀▀▀——————————————————————————————")
        MKF.edit_ppl_abandoned()
        editMenu()
        
    else:
        mainMenu()

def produceMenu():
    
    menu = ["---1: Produce People Abused --- | ---2: Produce People Abandoned ---"]
    menu1 =["---3: Produce Cats Adoption --- | ---4:   Produce Dogs Adoption  ---"]
    menu2 =["---5: Produce Animals Return Owners---"]
    print("\t\t\t\t\t\t\t\t\t\t\t ╔════════╗")
    print("\t\t\t\t\t\t\t\t\t\t\t╔╣SUB MENU╠╗")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╩▬▬▬▬▬▬▬▬▬▬╩▬▬")
    print(menu)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(menu1)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(menu2)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    c = int(input("➥Please give an option: "))
    
    if c == 1:
       
        print("\t\t\t—————————————▄▄▄——————————————————————————————————")
        print("\t\t\tChose option ▌1▐ ►PRODUCING PEOPLE ABUSED ANIMALS◄")
        print("\t\t\t—————————————▀▀▀——————————————————————————————————")
        MKF.list_ppl_abused()
        produceMenu()
        
        #MKT.editSugery(which_row,enter)
    elif c == 2:
        
        print("\t\t\t—————————————▄▄▄—————————————————————————————————————")
        print("\t\t\tChose option ▌2▐ ►PRODUCING PEOPLE ABONDONED ANIMALS◄")
        print("\t\t\t—————————————▀▀▀—————————————————————————————————————")
        MKF.list_ppl_abandoned()
        produceMenu()
        
    elif c == 3:
        
        print("\t\t\t—————————————▄▄▄——————————————————————————")
        print("\t\t\tChose option ▌3▐ ►PRODUCING CATS ADOPTION◄")
        print("\t\t\t—————————————▀▀▀——————————————————————————")
        MKF.list_cat_adopt()
        produceMenu()
        
    elif c == 4:
       
        print("\t\t\t—————————————▄▄▄——————————————————————————")
        print("\t\t\tChose option ▌4▐ ►PRODUCING DOGS ADOPTION◄")
        print("\t\t\t—————————————▀▀▀——————————————————————————")
        MKF.list_dog_adopt()
        produceMenu()
        
    elif c == 5:
       
        print("\t\t\t—————————————▄▄▄——————————————————————————")
        print("\t\t\tChose option ▌5▐ ►PRODUCING RETURN OWNERS◄")
        print("\t\t\t—————————————▀▀▀——————————————————————————")
        MKF.list_ani_return()
        produceMenu()
    else:
        mainMenu()
        
        
mainMenu()

