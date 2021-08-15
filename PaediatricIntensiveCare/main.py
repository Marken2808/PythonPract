import csv
from Patient import Patient

list_A1 = []
list_A2 = []
list_A3 = []
list_B1 = []
list_B2 = []
list_B3 = []
list_B4 = []
list_B5 = []
list_B6 = []
list_B7 = []
bigList = []

def main():
    

    with open("PATIENT DATA - PATIENT A1.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_A1.append(line)
            
    with open("PATIENT DATA - PATIENT A2.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_A2.append(line)
    
    with open("PATIENT DATA - PATIENT A3.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_A3.append(line)
            
    with open("PATIENT DATA - PATIENT B1.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_B1.append(line)
            
    with open("PATIENT DATA - PATIENT B2.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_B2.append(line)

    with open("PATIENT DATA - PATIENT B3.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_B3.append(line)
            
    with open("PATIENT DATA - PATIENT B4.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_B4.append(line)
            
    with open("PATIENT DATA - PATIENT B5.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_B5.append(line)
            
    with open("PATIENT DATA - PATIENT B6.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_B6.append(line)
            
    with open("PATIENT DATA - PATIENT B7.csv", 'rt') as f:
        data = csv.reader(f,skipinitialspace=True)

        for line in data:
            list_B7.append(line)

    
    bigList.append(list_A1) #0
    bigList.append(list_A2) #1
    bigList.append(list_A3) #2
    bigList.append(list_B1) #3
    bigList.append(list_B2) #4
    bigList.append(list_B3) #5
    bigList.append(list_B4) #6
    bigList.append(list_B5) #7
    bigList.append(list_B6) #8
    bigList.append(list_B7) #9
    
    #print(bigList)
    
    a=Patient()
    a.print_sorting_patients_issues(bigList)

 
if __name__ == '__main__':main()



























