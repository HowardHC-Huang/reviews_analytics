## 留言分析程式 ##

#1.建立github repository
#2.程式:讀出留言檔,並寫進清單
#3.測試印出data清單看看
#4.[延伸1]讀取進度顯示(透過記數知道我們的狀態):每1000筆,印一次len(data);每1筆印一次會非常慢(print很耗時間)
#5.先上傳一次github
#6.[延伸2]計算留言平均字數
#7.Final上傳github
#8.學了字典後, 一百萬筆留言中最常出現的字為何:
#字的計數:統計每字出現幾次,之後取出現次數最大者
#字有沒出現過:沒有就記下來; 再遇到就+1    "單字":1"單字":2... (非常適合以字典處理)

data = []
count = 0						#1-2.印到哪就顯示進度而創
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1		#1-2.印到哪就顯示進度而創
		if count % 1000 == 0:	#1-1.印到哪就顯示進度,每1000筆印一次 [插花]%用來求餘數
			print(len(data))
print('檔案讀取完畢, 共記', len(data), '筆資料')

#print(data[0])

wc = {}    #word_count
for d in data:
	words = d.split(' ')    #words是清單, 從d切完而來的
	for word in words:
		if word in wc:
			wc[word] += 1   #[重要!!!!!]易不熟,wc字典中去查找word的值(次數),並+1
		else:
			wc[word] = 1    #[重要!!!!!]用等號用等號用等號! 講到"新增"字典,就想到等號

for word in wc:
		if wc[word] > 1000000:    #出現次數大於一百萬次才印
			print(word, wc[word])    #印出key,value

while True:
	word = input('請輸入你想查的字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('這個字沒出現過喔!')
print('感謝使用')




# print(len(data))	#0.測試:觀察留言有幾筆

# #print(data)		#0.看100萬筆留言印出會如何→真的會印出,非常長,非常非常非常久
# print(data[0])	#0.只印第1筆留言:中括號0
# print('----- -----')
# print(data[1])

#[思考]求留言平均字數

# sum_len = 0
# for d in data:			#2.把清單data中,每筆資料命名為d
# 	sum_len = sum_len + len(d)	#2-1.利用[關鍵!!!]"字串可當清單",再創sum_len加總
#
# print('留言平均字數為:', sum_len / len(data), '個字')	#2-2.留言總字數/一百萬,印出
#
#
# #8.[延伸3]篩選留言字數>100字者
# new = []
# for d in data:	#清單data的資料一筆筆拿出,叫做d
# 				#[重要!!!]所以上面,每個d就是一筆留言,data就是裝著百萬筆留言的清單(d是字符,data是清單)
# 				#你一定要很清楚每個東西是什麼,不然等下在寫時,語法面會出錯
# 	if len(d) < 100:
# 		new.append(d)	#如果長度<100,就把你裝進新清單new裡(到此篩選完畢)
# print('共有', len(new), '筆留言,字數小於100字')
#
# #9.[延伸4]篩選留言中有good字樣者
# good = []
# for d in data:
# 	if 'good' in d:		#[易忘]如果good在d裡
# 		good.append(d)
# print('共有', len(good), '筆留言,提到good')
#
# #print(good[0])	#自己測試看看印出第一筆
#
# #10.List comprehension 清單快寫法
# good = [d for d in data if 'good' in d]
#
# #[重要!!!!!]整句: [運算]:想對清單做的動作+ [循環]:清單中的每筆數據出來+ [篩選條件]:你有沒有包含good