import json

with open("euro.json","r") as f:
    rates=json.load(f)
    print(rates)

for i in rates['rates']:
    print("Date", "     ","Buying Rate", "     ","Selling Rate")
    print("=====================================================")
    print(i['effectiveDate'], "   ",i['bid'], "   ",i['ask'])