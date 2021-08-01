data = []
count = 0
with open('reviews.txt', 'r') as f:
      for line in f:
            data.append(line.strip())
            count += 1
            if count % 10000 == 0:
                print(len(data))
print(len(data)) #印出幾筆資料

print(data[0]) #印出清單中第0個位置
print('----------------') #資料中間的分隔線
print(data[1]) #印出清單中第1個位置