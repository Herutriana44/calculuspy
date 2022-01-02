from sympy import *
import os
from os import system, name
from os import *

hasil = "Hasil nya adalah "
init_printing(use_unicode=True)

def help ():
	print("tambah => (+) => 2x+3")
	print("pengurangan => (-) =>  2x-3")
	print("perkalian => (*) => 2x*3")
	print("pembagian atau pecahan => (/) => 2x/3x")
	print("pangkat => (**) => 2x**2")
	print("akar pangkat 2 => (**(1/2)) => 4x**(1/2)")
	print ("akar pangkat n => (**(1/n)) => 4x**(1/3)")
	
def logo():
	print("┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿")
	print("─=≡Σ((( つ◕ل͜◕)つ")
	print("(´・ω・)っ由")
	print("༼ つ ◕_◕ ༽つ")
	
def garis():
	print("================================================")
	
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
def task():
	print("Program Kalkulus")
	print("By. Heru Triana")
	garis()
	logo()
	garis()
	help()
	garis()
	print("[1]. turunan")
	print("[2]. integral 1")
	print("[3]. integral 2")
	print("[4]. limit")
	print("[5]. penyederhanaan aljabar")
	print("[6]. ekspansi aljabar")
	print("[7]. pemfaktoran aljabar")
	print("[8]. Interval fungsi")
	print("\n[0]. keluar")
	garis()
	per = int(input("masukkan perintah : "))
	clear()
	if(per == 1):
		turunan()
	elif(per == 2):
		integral1()
	elif(per == 3):
		integral2()
	elif(per == 4):
		limitpy()
	elif(per == 5):
		simple()
	elif(per == 6):
		ekspansi()
	elif(per == 7):
		faktor()
	elif(per==8):
		intervalFungsi()
	elif(per == 0):
		os.system("exit")
	else:
		print("perintah tidak terdefinisi!")


def intervalFungsi():
	print("x = y")
	xx = sympify(input("masukkan x : "))
	yy = sympify(input("masukkan y : "))
	var = symbols(input("masukkan variabel yg ingin dioperasikan : "))
	clear()
	print(hasil)
	print(solveset(Eq(xx,yy),var))
	
def turunan():
	fx = input("masukkan fungsi : ")
	var = symbols(input("masukkan variabel yg ingin dioperasikan : "))
	jumlahturunan = int(input("masukkan jumlah turunan(default 1) : "))
	clear()
	if(jumlahturunan>1):
		print(hasil)
		print(diff(fx,var,jumlahturunan))
	else:
		print(hasil)
		print(diff(fx,var))
		
def integral1():
	fx = input("masukkan fungsi : ")
	var = symbols(input("masukkan variabel yg ingin dioperasikan : "))
	clear()
	print(hasil)
	print(integrate(fx,(var,bb,ba)))

def integral2():
	fx = input("masukkan fungsi : ")
	var = symbols(input("masukkan variabel yg ingin dioperasikan : "))
	bb = input("masukkan batas bawah integral : ")
	ba = input("masukkan batas atas integral : ")
	clear()
	print(hasil)
	print(integrate(fx,(var,bb,ba)))
		
def limitpy():
	fx = input("masukkan fungsi : ")
	var = symbols(input("masukkan variabel yg ingin dioperasikan : "))
	varo = int(input("masukkan limit ke berapa : "))
	batas = input("masukkan batas(limit keatas(+)/limit kebawah(-)/default tanpa keduanya) : ")
	clear()
	if(batas=="0"):
		print(hasil)
		print(limit(fx,var,varo))
	elif(batas=="+"):
		print(hasil)
		print(limit(fx,var,varo,symbols(batas)))
	elif(batas=="-"):
		print(hasil)
		print(limit(fx,var,varo,symbols(batas)))
	else:
		print(hasil)
		print(limit(fx,var,varo))
			
def simple():
	fx = input("masukkan fungsi aljabar : ")
	clear()
	print(hasil)
	print(simplify(fx))

def ekspansi():
	fx = input("masukkan fungsi aljabar : ")
	clear()
	print(hasil)
	print(expand(fx))
	
def faktor():
	fx = input("masukkan fungsi aljabar : ")
	clear()
	print(hasil)
	print(factor(fx))

#main
while(true):
	clear()
	task()
	print()
	tany = input("apakah mau diulangi(y/t) : ")
	clear()
	if(tany=="t" or tany=="T"):
		print("Program Berhenti!!")
		print("(*・‿・)ノ⌒*:･ﾟ✧")
		print("(ʘ‿ʘ)╯\t Terima Kasih")
		break
