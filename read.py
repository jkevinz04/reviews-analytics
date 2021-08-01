#讀取留言並分析
data = []
count = 0
with open('reviews.txt', 'r') as f:
      for line in f:
            data.append(line.strip())
            count += 1 #每讀取一筆增加一個 count
            if count % 10000 == 0: #每 10000 筆留言印出進度，餘數為 0 則印出
                print(len(data))
print(len(data)) #印出幾筆資料

#print(data[0]) #印出清單中第0個位置
#print('----------------') #資料中間的分隔線
#print(data[1]) #印出清單中第1個位置

print('檔案讀取完了，總共有', len(data), '筆資料')

#平均留言長度1
sum_len = 0 #留言長度起始值 0
for d in data:
    sum_len += len(d) #每讀取一筆資料長度加入 sum_len 並存回
avg_len = sum_len / len(data)
print('平均留言長度為', avg_len, '個字')

#平均留言長度2
wc = [] #建立留言長度清單
for d in data:
	wc.append(len(d)) #每讀取一筆資料長度存回清單
avg_len = sum(wc) / len(data) #加總清單資料並除與幾筆資料得到平均長度
print('平均留言長度為', avg_len, '個字')