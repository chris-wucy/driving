conutry = input('請輸入您的國家： ')
age = input('請輸入年齡： ')
age = int(age)
if conutry == '台灣':
	if age >= 18:
		print('你可以考駕照！')
	else:
		print('你還不能開車！')