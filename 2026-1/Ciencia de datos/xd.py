

with open("Ciencia de datos.md","a") as file:
    for i in range(1,53):
        if (i<10):
            dato=f"0{i}"
        else:
            dato=str(i)
        file.write(f"![[W1_9__Bagging_and_Boosting_page-00{dato}.jpg]]\n\n")
