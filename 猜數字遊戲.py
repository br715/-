import random

target = random.randint(1, 99)
times = 5

print('猜數字遊戲開始，請猜100以內的整數')

while times != 0:
    num = int(input('請輸入你要猜的數字：\n'))

    if num > target:
        print('你輸入的數字有點大，請繼續猜！\n')
        continue

    elif num < target:
        print('你輸入的數字有點小，請繼續猜！\n')
        continue

    else:
        print('恭喜你！猜對了，正確答案是', target)
        break
times -= 1

if times == 0:
    print('次數用完了，答案是：', target)
