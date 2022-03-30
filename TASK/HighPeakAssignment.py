
def maini(imp):
    return combine_helper(imp, [], [])
numEmp=4
class my_dictionary(dict):
    def init(self):
        rr =self.dict()

    def add(self, key, value):
        self[key] = value

def combine_helper(inp, temp, ans):
    for i in range(len(inp)):
        current = inp[i]
        remaining = inp[i + 1:]
        temp.append(current)
        ans.append(tuple(temp))
        combine_helper(remaining, temp, ans)
        temp.pop()
    return ans

count = 0
goodieDict = my_dictionary()
file1 = open("Input_Emp.txt","r")
for x in file1:
    count+=1
    if count>=5 :
        (key, val) = x.split(": ")
        if val[-2]=="\n":
            val = val.rstrip(val[-2])
        goodieDict[(key)] = val
    elif count==1 :
        (numEmpTxt, numEmp) = x.split(": ")

print(goodieDict)
priceList = list(goodieDict.values())
for i in range(0, len(priceList)):
    priceList[i] = int(priceList[i])

dict_obj = my_dictionary()
a = maini(priceList)
for i in a:
    if(len(i) == (int(numEmp))):
        nt = sorted(i)
        diffValue = nt[(int(numEmp)-1)] - nt[0]
        dict_obj.key = diffValue
        dict_obj.value = nt
        dict_obj.add(dict_obj.key, dict_obj.value)

keyList = dict_obj.keys()
sortedKeyList = sorted(keyList)

finalPriceList = dict_obj.get(sortedKeyList[0])
emploNO=int(input("Enter the numbers of employee : "))
wr = open("Output_Emp.txt", "w")
wr.write("The goodies selected for distribution are:\n\n")
for pricee in finalPriceList:
    for kee in goodieDict.keys():
        if pricee == int(goodieDict[kee]):
            wr.write(kee+": "+str(pricee)+"\n")
    wr.write("\n")

difference = finalPriceList[(int(numEmp)-2)] - finalPriceList[0]
wr.write("The difference between the chosen goodie with highest price and the lowest price is "+str(difference))
wr.close()


fdata= open("Output_Emp.txt", "r")
data=fdata.read()

# print(data)

for r in data:
    print(r,end='')

