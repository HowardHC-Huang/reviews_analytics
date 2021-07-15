## 留言分析程式 ##

#1.建立github repository
#2.程式:讀出留言檔,並寫進清單
#3.測試印出data清單看看
#4.[延伸]讀取進度顯示(透過記數知道我們的狀態):每1000筆,印一次len(data);每1筆印一次會非常慢(print很耗時間)
#5.先上傳一次github


data = []
count = 0						#1-2.印到哪就顯示進度而創
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1		#1-2.印到哪就顯示進度而創
		if count % 1000 == 0:	#1-1.印到哪就顯示進度,每1000筆印一次 [插花]%用來求餘數
			print(len(data))	
print(len(data))	#0.測試:觀察留言有幾筆

#print(data)		#0.看100萬筆留言印出會如何→真的會印出,非常長,非常非常非常久
print(data[0])		#0.只印第1筆留言:中括號0
print('----- -----')
print(data[1])