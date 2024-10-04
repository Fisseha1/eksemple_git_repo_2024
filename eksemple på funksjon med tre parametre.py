 # eksemple på funksjon med tre parametre : firekant av tegn som en funksjon

def stjern_firkant(hoyde, bredde, tegn="*"):
    for y in range(hoyde):
        for x in range(bredde):
            print(tegn,end="")# end="" for å ikke få newline på slutten
        print()
    hoyde= hoyde +6
    print("økt hoyde inni funksjon", hoyde)
 
  
 
 # kode som demonstrerer funksjon
stjern_firkant(6,5,"#")
hoyde=int(input("skriv inn høyde:"))
bredde= int(input(" skriv inn bredde"))
stjern_firkant(hoyde, bredde)
print("høyde til slut", hoyde)
stjern_firkant(tegn="0", bredde =8, hoyde =3)
stjern_firkant(tegn="+",bredde=4, hoyde=7)

