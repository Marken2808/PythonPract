class Patient:


    #def __init__(self,day,time,feed,grv,issues):
        #self.day = day
        #self.time = time
        #self.feed = feed
        #self.grv = grv
        #self.issues = issues

    #def __str__(self):
        #return self.day + self.time + self.feed + self.grv + self.issues 

    def is_not_empty(self,s):    #check blank
        return bool(s and s.strip())
    
    def is_integer(self,n):      #check numeric string is integer
        try:
            float(n)
        except ValueError:
            return False
        else:
            return float(n).is_integer()
       
    def is_empty(self,arr):
        if not arr:
            arr.append("NONE")
        return arr[0]
    
    def Sorting(self,array):
        Sort_list = []   
        while array:
            smallest = min(array)
            Sort_list.append(smallest)
            array.pop(array.index(smallest))
        return Sort_list
    
    def sort_return_index(self,new_array):
         
        sort_array=[] 
        for i in range(len(new_array)): 
            sort_array.append([new_array[i],i]) 
        temp = self.Sorting(sort_array) 
        return_index = [] 
          
        for i in temp: 
            #print(i)
            return_index.append(i[1]) 
          
        return return_index
    
    def get_row(self,new_file,new_cell):  #print row selected
        
        row = 0
        for i in range(len(new_file)):
            for j in range(len(new_file[i])):
                if new_file[i][j] == new_cell:
                    row = new_file[i]
        return row
    
    def get_column(self,new_file,new_col):
    
        col=[]
        cell_col=0
        for i in range(len(new_file)):
            for j in range(len(new_file[i])):
                if j == new_col:
                    cell_col = j
    
    
        for i in range(len(new_file)):
            col.append(new_file[i][cell_col])
        return col
    
    def read_GRV(self,new_file,new_string):
        col = self.get_column(new_file,3)
        grv_index = []
        grv_data = []
        for i in range(len(col)):
            if self.is_not_empty(col[i]) == True:
                if self.is_integer(col[i]) == True:
                        grv_index.append(i)
                        grv_data.append(col[i])
                        
        if new_string == "index":
            return grv_index
        elif new_string == "data":
            return grv_data
        
    def read_Feed(self,new_file,new_string):
        col = self.get_column(new_file,2)
        feed_data = []
        for i in range(3,len(col)):
            feed_data.append(col[i])
        return feed_data
        
    def get_cell(self,new_file,new_row,new_column):
        cell = 0
        for i in range(len(new_file)):
            for j in range(len(new_file[i])):
                if j == new_column:
                    cell = new_file[new_row][new_column]
            break
        return cell
                
    def get_weight(self,new_cell):
        string = new_cell
    
        for i in string.split():
            try:
                weight = float(i)
            except ValueError:
                pass    
        return weight
    
    def get_age(self,new_file):
        age = self.get_cell(new_file,0,2)
        return age
    
    def get_status(self,new_file):
        status = self.get_cell(new_file,0,1)
        return status
        
        
    def get_critical_value(self,new_file):
        cell= self.get_cell(new_file,0,4)
        weight = float(self.get_weight(cell))
    
        return weight * 5
    
    def compare_GRV(self,new_file):
        cri = self.get_critical_value(new_file)
        grv_data = self.read_GRV(new_file,"data")
        grv_index = self.read_GRV(new_file,"index")
        
        if self.get_status(new_file) == "LR":
            for i in range(len(grv_index)):
                print("At index: "+ str(grv_index[i]))
                if (int(grv_data [i]) < cri) == True:
                    print(str(grv_data [i]) + "\tLess than\t" + str(cri))
                    
                    
                elif (int(grv_data[i]) == cri):
                    print(str(grv_data [i]) + "\tEqual\t\t" + str(cri))
                    
                else:
                    print(str(grv_data [i]) + "\tGreater than\t" + str(cri))
                print("at row: " + str(grv_index[i]+1) + ":\t"+ str(new_file[grv_index[i]])+"\n") 
                
                
        else:
            print("this is HIGH RISK!!!")
     
    def get_day(self,new_file):
        
        day_data = []
        day_index = []
        col = self.get_column(new_file,0)
        for i in range(len(col)):
            if self.is_integer(col[i]) == True:
                day_data.append(col[i])
                day_index.append(i)
    
        
        return day_index
    
    def index_combo_grv_in_day(self,new_file,new_day):
        day_index = self.get_day(new_file)
    
        grv_index = self.read_GRV(new_file,"index")
        
        day_1 = []
        day_2 = []
        day_3 = []
        day_4 = []
        day_5 = []
    
        for i in range(len(grv_index)):
            
            if (grv_index[i] < day_index[1]) == True :
                day_1.append(grv_index[i])
                
            elif (grv_index[i]<day_index[2] and grv_index[i]>=day_index[1]) == True:
                day_2.append(grv_index[i])
                
            elif (grv_index[i]<day_index[3] and grv_index[i]>=day_index[2]) == True:
                day_3.append(grv_index[i])
                
            elif (grv_index[i]<day_index[4] and grv_index[i]>=day_index[3]) == True:
                day_4.append(grv_index[i])
            
            else:
                day_5.append(grv_index[i])
                
        #print("day1: " +str(day_1))
                
        #print("day2: " +str(day_2))
                    
        #print("day3: " +str(day_3))
        
        #print("day4: " +str(day_4))
        
        #print("day5: " +str(day_5))
        
        if(new_day == 1):
            return day_1
        elif(new_day == 2):
            return day_2
        elif(new_day == 3):
            return day_3
        elif(new_day == 4):
            return day_4
        elif(new_day == 5):
            return day_5
    
    #def get_issue(new_file,new_index):
        #get_cell(new_file,new_row,new_column)
    
    #def get_last_issue(new_file,new_day):
        #day = index_combo_grv_in_day(new_file,new_day)
        
        #print(day)
        
    def set_issue(self,new_file,new_string):
        cell=self.get_cell(new_file,0,4)
        weight = float(self.get_weight(cell))
        
        cri = self.get_critical_value(new_file)
        grv_data = self.read_GRV(new_file,"data")
        grv_index = self.read_GRV(new_file,"index")
        
        stop = 0
        
        diet = []
        pause = []
        none = []
        
        
        for i in range(len(grv_index)):
         
            if (int(grv_data [i]) > cri) == True:  
                #print("at row: " + str(grv_index[i]+1) + "==> "+ str(new_file[grv_index[i]])) 
                #print(str(grv_data [i]) + "\tGreater than\t" + str(cri))
                if weight <= 40 :
                    #if get_status(new_file) == "LR":
                    stop = stop +1
                    if stop > 2 : 
                        #print("\t\t\t\t\tStatus: Refer diet\n")
                        stop = 0
                        #return "Refer diet"
                        diet.append(grv_index[i])    
                    else:
                        #print("\t\t\t\t\tStatus: Stop Feeding\n")
                        #return "Stop Feeding"
                        pause.append(grv_index[i])    
                    #elif get_status(new_file) == "HR":
                        
                        
                        
                        
                elif weight>40: 
                    if int(grv_data[i]) > 250:
                        stop = stop +1
                        if stop > 2 :
                            #print("\t\t\t\t\tStatus: Refer diet\n")
                            stop = 0
                            #return "Refer diet"
                            diet.append(grv_index[i])
                        else:
                            #print("\t\t\t\t\tStatus: Stop Feeding\n")
                            #return "Stop Feeding"
                            pause.append(grv_index[i])
                    else:
                        #print("\t\t\t\t\tStatus: None")
                        #return "None"
                        none.append(grv_index[i])  
            else:
                #print("at row: " + str(grv_index[i]+1) + "==> "+ str(new_file[grv_index[i]])) 
                #print(str(grv_data [i]) + "\tLess than or Equal\t" + str(cri))
                #print("\t\t\t\t\tStatus: None\n")
                stop = 0
                #return "None"
                none.append(grv_index[i])
        if new_string == "refer":
            #print(diet)
            return diet
        elif new_string == "pause":
            #print(pause)
            return pause
        elif new_string == "none":
            #print(none)
            return none
        
        
    def index_combo_issue_in_day(self,new_file,new_day):
        day_index = self.index_combo_grv_in_day(new_file,new_day)
        #grv_index = read_GRV(new_file,"index")
        diet_index = self.set_issue(new_file,"refer")
        pause_index = self.set_issue(new_file,"pause")
        none_index = self.set_issue(new_file,"none")
    
        temp_day = []
        
        
        #print("comparing:\t\t" + str(index_combo_grv_in_day(new_file,new_day)))
        #print("diet:\t\t\t" + str(diet_index))     
        #print("pause:\t\t\t" + str(pause_index))
        #print("none:\t\t\t" + str(none_index))
        
        
        for i in range(len(day_index)):
            for a in range(len(diet_index)):
                if day_index[i] == diet_index[a]:
                    temp_day.append("REFER")
            for b in range(len(pause_index)):
                if day_index[i] == pause_index[b]:
                    temp_day.append("PAUSE")
            for c in range(len(none_index)):
                if day_index[i] == none_index[c]:
                    temp_day.append("NONE")
    
        return temp_day
    
    def take_last_issue_5_day(self,new_file):
        
        
        
        day1 = self.index_combo_issue_in_day(new_file,1)
        day2 = self.index_combo_issue_in_day(new_file,2)
        day3 = self.index_combo_issue_in_day(new_file,3)
        day4 = self.index_combo_issue_in_day(new_file,4)
        day5 = self.index_combo_issue_in_day(new_file,5)
       
        report_in_5_days = []
        report_in_5_days.append(self.is_empty(day1[-1:]))
        report_in_5_days.append(self.is_empty(day2[-1:]))
        report_in_5_days.append(self.is_empty(day3[-1:]))
        report_in_5_days.append(self.is_empty(day4[-1:]))
        report_in_5_days.append(self.is_empty(day5[-1:]))
        return report_in_5_days
    
    def take_last_issue_a_patient(self,new_file):
        report_5_days = self.take_last_issue_5_day(new_file)
        #print("report_5_days: " + format(report_5_days))
        return report_5_days
 
    def nametag(self,i):
        nametag = i
        if nametag == 0:
            nametag = "A1"
        if nametag == 1:
            nametag = "A2"
        if nametag == 2:
            nametag = "A3"
        if nametag == 3:
            nametag = "B1"
        if nametag == 4:
            nametag = "B2"
        if nametag == 5:
            nametag = "B3"
        if nametag == 6:
            nametag = "B4"
        if nametag == 7:
            nametag = "B5"
        if nametag == 8:
            nametag = "B6"         
        if nametag == 9:
            nametag = "B7"
        return nametag
    
    def print_tracking_table(self,new_big_file):
        patients = self.combo_patients(new_big_file)
        for i in range(len(patients)): 
            
            nametag = self.nametag(i)
            cell= self.get_cell(new_big_file[i],0,4)
            feed_data = self.read_Feed(new_big_file[i],2)
            age = self.get_age(new_big_file[i])
            status = self.get_status(new_big_file[i])
            weight = float(self.get_weight(cell))
            cri = self.get_critical_value(new_big_file[i])
          
            print("———————————▄▄▄▄——————————")
            print("| Patient  ▌"+nametag+"▐  info\t|") 
            print("———————————▀▀▀▀——————————")
            print("|Age: " +str(age)+"\t|")
            print("|Status: " + status+"\t\t|")
            print("|weight: " + str(weight)+"\t\t|")
            print("|feed: " + feed_data[0]+" \t|")
            print("|critical value: "+ str(cri)+"\t|")
            print("---------------------------------------------------------------------------------------------")
            
            print(self.index_combo_grv_in_day(new_big_file[i],1))
            day1 = self.index_combo_issue_in_day(new_big_file[i],1)
            print("day1:" + str(day1))
            print("\t\t\t\t\t\t===================================>" + str(self.is_empty(day1[-1:])))
            
            print(self.index_combo_grv_in_day(new_big_file[i],2))
            day2 = self.index_combo_issue_in_day(new_big_file[i],2)
            print("day2:" + str(day2))
            print("\t\t\t\t\t\t===================================>" + str(self.is_empty(day2[-1:])))
            
            print(self.index_combo_grv_in_day(new_big_file[i],3))
            day3 = self.index_combo_issue_in_day(new_big_file[i],3)
            print("day3:" + str(day3))
            print("\t\t\t\t\t\t===================================>" + str(self.is_empty(day3[-1:])))
            
            print(self.index_combo_grv_in_day(new_big_file[i],4))
            day4 = self.index_combo_issue_in_day(new_big_file[i],4)
            print("day4:" + str(day4))
            print("\t\t\t\t\t\t===================================>" + str(self.is_empty(day4[-1:])))
            
            print(self.index_combo_grv_in_day(new_big_file[i],5))
            day5 = self.index_combo_issue_in_day(new_big_file[i],5)
            print("day5:" + str(day5))
            print("\t\t\t\t\t\t===================================>" + str(self.is_empty(day5[-1:])))
            print("---------------------------------------------------------------------------------------------\n")    
        
    def combo_patients(self,new_big_file):
        patients = []
        for i in range(len(new_big_file)):
            temp = self.take_last_issue_a_patient(new_big_file[i])
            
            patients.append(temp)

        return patients 
    
    def set_level_a_patients(self,new_big_file):   
        level = []
        patients = self.combo_patients(new_big_file)
        self.print_tracking_table(new_big_file)
        print("Before Sorting:")
        for i in range(len(patients)): 
            nametag = self.nametag(i)
            
            print("Patient["+nametag+"] "+str(patients[i])) 

            for j in range(len(patients[i])):           
                if patients[i][j] == "NONE":
                    patients[i][j] = 0                 
                elif patients[i][j] == "PAUSE":
                    patients[i][j] = 1
                else:
                    patients[i][j] = 2
                #print("\t\t\t------------------------------>"+ str(patients[i][j]))           
            level.append(patients[i])

        return level
            
    def print_sorting_patients_issues(self,new_big_file):

        patients = self.combo_patients(new_big_file)
        level = self.set_level_a_patients(new_big_file)
        reverse =[]
        index =[]
        for i in range(len(level)):
            re = level[i][::-1]    
            reverse.append(re)
           
    
        index = self.sort_return_index(reverse)
        print("=====================================================") 
        print("After Sorting:")
        for i in range(len(index)):
            for j in range(len(patients)):
                if index[i] == j:
                    nametag = self.nametag(index[i])
                    
                    
                    print("Patient["+nametag+"] "+str(patients[j])) 
                    
        

    

        
        
        
    


    
