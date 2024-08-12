import math

#Noktalarin tanimlanmasi
points = [(0,0),(1,2),(3,4),(5,6)]

#Oklid mesafesi icin fonksiyon tanimlanmasi
def euclideanDistance(point1,point2):
        x1, y1=point1
        x2, y2=point2
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return distance

#Mesafe hesaplanmasi
distances = []

for i in range(len(points)):
  for j in range(i+1,len(points)):
      distance=euclideanDistance(points[i],points[j])
      distances.append(distance)

#Minimum mesafe hesaplanmasi
min_distance = min(distances)

print("Minimum mesafe:", min_distance)
