

with open("Redes de Computadores.md","a") as file:
    for i in range(1,114):
        if (i<10):
            dato=f"00{i}"
        elif(i<100):
            dato=f"0{i}"
        else:
            dato=str(i)
        file.write(f"![[Chapter_8_v8.0_page-0{dato}.jpg]]\n\n")
