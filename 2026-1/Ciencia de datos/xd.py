

with open("Ciencia de datos.md","a") as file:
    for i in range(1,57):
        if (i<10):
            dato=f"0{i}"
        else:
            dato=str(i)
        file.write(f"![[W1_13__Deployment_page-00{dato}.jpg]]\n\n")
