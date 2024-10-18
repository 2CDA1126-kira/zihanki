x = int(input('値段: '))
n = int(input('投入金額: '))

oturi = n - x
oturigoukei = oturi

oturi_500 = oturi//500         
oturi = oturi%500
oturi_100 = oturi//100        
oturi = oturi%100
oturi_50 = oturi//50           
oturi = oturi%50
oturi_10 = oturi//10           


print(f"お釣りは {oturigoukei} 円")
print(f"500円: {oturi_500} 枚")
print(f"100円: {oturi_100} 枚")
print(f"50円: {oturi_50} 枚")
print(f"10円: {oturi_10} 枚")