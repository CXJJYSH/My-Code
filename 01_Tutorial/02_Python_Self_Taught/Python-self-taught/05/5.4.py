wodeshuxing={"height":"172cm","my favourite color":"black","my favourite writer":"Cory Althoff"}
n=input("Type what you want to know:")
if n in wodeshuxing:
    shuxing=wodeshuxing[n]
    print(shuxing)
else:
    print("Not found.")
