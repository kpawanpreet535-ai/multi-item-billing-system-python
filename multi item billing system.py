n = int(input("no. of items ="))

total_bill = 0
items = []
for i in range(n):
    print("\nItem", i+1)
    item = input("Enter Item Name =")
    price = int(input("Enter Price ="))
    qty = int(input("Enter Qty ="))
    amt = price * qty
    total_bill = total_bill+amt
    item_data = {"name":item,
                 "price":price,
                 "qty":qty,
                 "amt":amt
                 }
    items.append(item_data)

    print("Item Total =", amt)
if total_bill >= 1000:
    dis = 10
else:
    dis = 5
disamt = dis*total_bill/100
netamt = total_bill- disamt

print("\n-------FINAL BILL------")
print("Total Bill =", total_bill)
print("Discount =", disamt)
print("Net Amt =", netamt)

print("\n -----Data-----")
print("\nName\tPrice\tQty\tAmount")
for item in items:
    print(item["name"],"\t",item["price"],"\t", item["qty"],"\t", item["amt"])

print("Total Items =", len(items))
