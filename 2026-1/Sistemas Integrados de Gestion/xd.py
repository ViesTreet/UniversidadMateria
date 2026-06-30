

with open("Sistemas Integrados de Gestion.md","a") as file:
    for i in range(1,48):
        if (i<10):
            dato=f"00{i}"
        elif(i<100):
            dato=f"0{i}"
        else:
            dato=str(i)
        file.write(f"![[PPT Contenidos tercer certamen SIG-USM 2026_page-0{dato}.jpg]]\n\n")
