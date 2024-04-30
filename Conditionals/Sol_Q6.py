# Transport Selector

distance = int(input("Please Specify the Distance (in km) you are going to cover:"))
if distance <3:
    print('Mode of Transport: Walk')
elif 3<distance<15:
    print('Mode of Transport: Bike')
elif 15<distance:
    print('Mode of Transport: Car')
else:
    print('Americaya!')
