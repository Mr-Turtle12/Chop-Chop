import json

def GetJson():
    json_file_path = "C:/Uni work/Operation Custard/Repo/comp6000-chop-chop/Prototypes/Object-Detection/recipts.json"
    with open(json_file_path, "r") as json_file:
        # Load the JSON data from the file
        data = json.load(json_file)

    receipts = data.get("receipts", [])
    return receipts


receipts = GetJson()
pancakeReceipt = receipts[0]["pancake"]

#print step one 
print(pancakeReceipt[0])
#print step two
print(pancakeReceipt[1])
#print number of step in receipt
print(len(pancakeReceipt))



