
age = int( input(' Введите ваш возраст: '))
if age < 0: print("Неверный возраст")
elif age >= 0 and age < 18: print("Вы еще несовершеннолетний")
else: print("Вы стали взрослым")