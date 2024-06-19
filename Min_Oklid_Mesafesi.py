import math

min=0
c=0
points=[]
distances=[]
nokta=int(input("kaç tane noktayı karşılaştıracaksınız?")) #kullanıcıdan kaç noktayı karşılaştıracağını alalım

for k in range(nokta):
    x=(float(input(f"{k+1}. noktanın X'ini giriniz")))
    y=(float(input(f"{k+1}. noktanın Y'sini giriniz")))
    points.append((x,y))
    
def euclideanDistance(nokta_1,nokta_2):
    x1,y1=points[nokta_1]
    x2,y2=points[nokta_2]
    return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

def min_bul(c,d):
    if distances[c]<distances[d]:
        return distances[c]
    elif distances[c]!=distances[d]:
       return distances[d]
    
    
for nokta_1 in range(len(points)):  #sırayla points içindeki tuple'lardan 2 tanesini fonksiyona gönderir ( a ve b noktalarını)
    for nokta_2 in range((nokta_1+1),len(points)):
        distances.append(euclideanDistance(nokta_1,nokta_2))
print(f"mesafeler= {distances}")
#distances listesindeki min mesafeyi bulur ve yazdırır
for d in range((c+1),len(distances)):  
    # örneğin mesafeler 12,10,10,9,15,17 olsun c=0 distances[0] ile başlar 
    #12<10 mu hayır c=d yapar 
    #yeni min sayısıyla karşılaştırmaya devam eder. 10=10 o zaman c=d yapar ki yine eski c ile karşılaştırmaya devam etmesin
    min=min_bul(c,d)                  
    if min!=distances[c] : #mesafe eşitse veya min=distances[d] ise 
        c=d
print(f"minimum mesafe={min}")     
        