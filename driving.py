conutry = input('請輸入您的國家： ')
if conutry == '台灣':
	age = input('請輸入年齡： ')
	age = int(age)
	if age >= 18:
		print('你可以考駕照！')
	else:
		print('你還不能開車！')
elif conutry == '美國':
	age = input('請輸入年齡： ')
	age = int(age)
	if age >= 16:
		print('你可以考駕照！')
	else:
		print('你還不能開車！')
else:
	print('請輸入 台灣/ 美國')

