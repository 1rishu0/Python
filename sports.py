import pandas as pd
from pandas import DataFrame
data=pd.read_csv("Sports.csv") #ensure csv file exists in the same folder as the python code.
columnlength=data.shape[1]     #obtain number of columns
print(data)


h=["0"]*(columnlength-1)
hp=[]                   #initialize list hp i.e list of hypotheses for positive training examples
hn=[]


for trainingExample in data.values:     #this loop is used to build the hypothesis list for every row.
    if trainingExample[-1]!="no":       #if the trainingexample is positive ,then it is appended to hp else to hn
        hp.append(list(trainingExample))
    else:
        hn.append(list(trainingExample))
        
        
for i in range(len(hp)):            #update the hypothesis h from most specific to maximally specific
    for j in range(columnlength-1): #if the hypothesis attribute value is 0, it is updated to the attributes in the first hypotesis
        if (h[j]=="0"):             
            h[j]=hp[i][j]
        if (h[j]!=hp[i][j]):        #if the attribute value in the hypothesis is not same as the attribute value in the successive hypotheses
            h[j]="?"                #then it is update to "?" indicating that any value is acceptable.
        else:                       #if the attribute inthe hypothesis is the same as the attribute value in the successive hypotheses
            h[j]=hp[i][j]
            
print("\nThe positive Hypotheses are")
print(hp)
print("\nThe negative Hypotheses are")
print(hn)
print("\nThe Maximally Specific Hypothesis h is")
print(h)