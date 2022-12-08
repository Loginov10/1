from math import *
#10
print("Kasutaja sisestab aja minutites. Sinu valem leiab ja väljastab tunnid ja minutid. Näiteks: sisestus 72, vastus 1:12")
n=float(input("aja minutites: "))
t=int(n//60)
s=int(n%60)
print(f"minutit {t}: sekundid {s}")





print()
print()
from math import *
#9
print("Rulluisutaja keskmine kiirus on 29,9km/h Kui kaugele jõuab 24minutiga")
print("otsime mitu tundi 24 minutit" )
t=24/60
print(f"Vastus: {t} tundi")
print("otsime kui kaugele jõuab 24 minutiga" )
r=0.4*29.9
print(f"Vastus: Te kaugele jõuate: {r} kilomeetrid ")




print()
print()
from math import *
#8
print("Kütusekulu arvutamine")
k=float(input("tangitud kütuse liitrid: "))
n=float(input("läbitud kilomeetrid: "))
q=(k/n)*100
print(f"keskmine kütusekulu 100 km kohta: {q}")











print()
#7
print("Võtsite 3 sõbraga suure pitsa hinnaga 12,90€. Jätate teenindajale 10% jootraha")
q=(12.90*10)/100
print(f"Te jääte {q} eur")
print("otsime kui plaju igaüks maaksab")
w=12.90/3
print(f"igaüks maksab: {round(w,2)}")










print()
#6
from random import *
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"külg a={a}\nKülg b={b}\nKülg c={c}")   #рандомные значения
print(f"Kolmurga ümbermõõt = {a+b+c}")
         






print()
#5
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("  ^^ "'""'" ^^  ")
   
  





#4
a=int(input("Number:"))
b=int(input("Number:"))
c=int(input("Number:"))
d=int(input("Number:"))
e=int(input("Number:"))
p=(a+b+c+d+e)/2
print(f"Vastus:keskmise suvalisest on {p}")






#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print("Sinu kiirus oli"  + str(kiirus) +  "km/h")







#2
print()
from math import *
print("kui pikk on ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Vastus:Maatüki diagonaal on {d} m**2")





#1 
print()
from math import *
print("Puu läbimõõdu arvutamine")
c=float(input("Puu ümbermõõt: "))
d=2*(c/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {c} ümbermõõt võrdub {d}")
