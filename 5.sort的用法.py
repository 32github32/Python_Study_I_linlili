data=[16.38,139,90,441.46,29.03,40.03,202.07,142.30,246.00,300]

data_items=len(data)
print(data_items)

total=sum(data)
print(total)

shortest=min(data)
print(shortest)

longest=max(data)
print(longest)

average=total/data_items
print(average)

data.sort()
print(data)

data.sort(reverse=True)
print(data)