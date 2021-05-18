def happy(name,age):
    if age < 10:
        print("안녕" + ' ' + name)
    elif age <= 20 and age >= 10:
        print("안녕하세요" + ' ' + name)
    elif age <= 30 and age >= 20:
        print("안녕하십니까"+ ' ' + name)
    else:
        print("좋은아침입니다"+ ' ' + name)


happy("김구라",15)