import random

# 初始血量
player_hp = 7
ai_hp = 7

# 道具池
items_pool = ["藥水","雞腿","手銬","炸彈","護盾","放大鏡"]
item_map = {"p":"藥水","c":"雞腿","h":"手銬","b":"炸彈","s":"護盾","m":"放大鏡"}
player_items = []
ai_items = []

# 初始狀態
player_shield = False
player_bomb = 0
player_handcuff = False
ai_shield = False
ai_bomb = 0
ai_handcuff = False

# 生成彈夾
def generate_mag():
    true_bullets = random.randint(1,5)
    magazine = ["真"] * true_bullets + ["假"] * (6 - true_bullets)
    random.shuffle(magazine)
    return magazine

# 發道具
def deal_items():
    return random.sample(items_pool, 2)

print("歡迎來到生死遊戲")
print("兩人共用一把手槍，每發有無子彈不明，可選擇射向自己或對方。")
print("此發若為空包彈，1.射向對方即轉換手槍控制權。2.射向自己則不換，下一發仍是你的操作回合。")
print("此發若為實彈，1.不論射向對方或自己，都轉換手槍控制權。")
print("\n道具如下，每回合隨機發派兩個，可延續回合使用，改變戰局。")
print("雞腿:自身恢復1點生命值。")
print("藥水:自身恢復1點生命值或是扣除2點生命值。")
print("手銬:禁錮對方，使用後下一發子彈無條件是自身回合，使用一次後消失。")
print("護盾:保護自己，受到傷害時將受到的傷害反彈，使用一次後消失。")
print("炸彈:下一發造成的+1傷害，可疊加。")
print("放大鏡:查看下一發空包與否。")
print("\n實彈造成傷害，善用道具，思考到最後一刻直到打敗對方!")

while player_hp > 0 and ai_hp > 0:

    mag = generate_mag()
    player_items += deal_items()
    ai_items += deal_items()

    print("\n新回合開始")
    true_count = mag.count("真")
    fake_count = mag.count("假")
    print("彈夾:", true_count, "真", fake_count, "假")

    turn = "player"

    while mag and player_hp > 0 and ai_hp > 0:
        if turn == "player":
            print("\n你的回合")
        else:
            print("\n對方回合")

        #玩家回合
        if turn == "player":
            print("你的血量:", player_hp, "對方血量:", ai_hp)
            print("你的道具:", player_items)

            action = input("射自己(s) / 射對方(o) / 使用道具(u): ")
            #玩家道具
            if action == "u":
                if not player_items:
                    print("你沒有道具可以使用!")
                    continue
                print("你的道具:", player_items)
                print(" p=藥水, c=雞腿, h=手銬, b=炸彈, s=護盾, m=放大鏡")
                item_choice_code = input("選擇使用道具: ")
                if item_choice_code not in item_map:
                    print("輸入代號錯誤!")
                    continue
                item_choice = item_map[item_choice_code]
                if item_choice not in player_items:
                    print("你沒有此道具!")
                    continue
                if item_choice == "雞腿":
                    player_hp += 1
                    print("使用雞腿 +1血")
                elif item_choice == "藥水":
                    change = random.choice([-2,1])
                    player_hp += change
                    print(f"使用藥水 {change}血")
                elif item_choice == "護盾":
                    player_shield = True
                    print("使用護盾，反彈自身傷害")
                elif item_choice == "手銬":
                    player_handcuff = True
                    print("使用手銬，下一發射擊仍然是你的回合")
                elif item_choice == "炸彈":
                    player_bomb += 1
                    print("使用炸彈，下一發傷害 +1")
                elif item_choice == "放大鏡":
                    next_bullet = mag[0]
                    print("使用放大鏡看到:", next_bullet)
                player_items.remove(item_choice)
                continue

            bullet = mag.pop(0)
            target = "自己" if action == "s" else "對方"
            damage = 1 + player_bomb
            print("你射向:", target, "結果:", bullet)

            # 玩家射及
            if target == "自己":#如果玩家射自己
                if bullet == "真": #射自己為實彈
                    if player_shield:#如果實彈且自己有盾
                        ai_hp -= damage#反彈傷害
                        player_shield = False#自己護盾消失
                        turn = "ai" #實彈換控制
                        print("護盾反彈!")
                    else:
                        player_hp -= damage#自己受傷
                        turn = "ai"#換控制
                else:#射自己空包
                    turn = "player"#不換回合無傷害
            else: #玩家射對方
                if bullet == "真":
                    if ai_shield:#實彈且對方有盾
                        player_hp -= damage#被反彈
                        ai_shield = False#對方護盾消失
                        print("被護盾反彈!")
                    else:
                        ai_hp -= damage
                turn = "ai"
            #特殊第三種
            if player_handcuff:#玩家用手銬
                turn = "player"#對方有手銬無條件不交換
                player_handcuff = False#玩家手銬消失
                print("禁錮對方一輪!")
            print("目前彈夾剩餘:", mag.count("真"), "真", mag.count("假"), "假")

        #Ai回合
        else:
            print("你的血量:", player_hp, "對方血量:", ai_hp)

            #雞腿判斷
            if ai_hp <= 3 and "雞腿" in ai_items:
                ai_hp += 1
                ai_items.remove("雞腿")
                print("對方使用雞腿 +1血")
            #放大鏡判斷
            target = None
            if "放大鏡" in ai_items and len(set(mag)) > 1:
                if random.random() < 0.7:
                    ai_items.remove("放大鏡")
                    next_bullet = mag[0]
                    print("對方使用放大鏡看到:", next_bullet)
                    target = "ai" if next_bullet == "真" else "player"
                          #ai                        #玩家
            #普攻判斷
            if target is None:
                true_count = mag.count("真")
                fake_count = mag.count("假")
                if true_count == 0:#全是假
                    target = "ai"#射ai
                elif fake_count == 0:#全是真
                    target = "player"#射玩家
                else:
                    target = random.choice(["ai","player"])
      #道具攻擊
            if player_hp <= 5:
                target = "你"
                if "手銬" in ai_items:
                    ai_handcuff = True
                    ai_items.remove("手銬")
                    print("對方使用手銬")
                if "護盾" in ai_items:
                    ai_shield = True
                    ai_items.remove("護盾")
                    print("對方使用護盾")
                if "炸彈" in ai_items:
                    ai_bomb += 1
                    ai_items.remove("炸彈")
                    print("對方使用炸彈")

            #對方射擊
            bullet = mag.pop(0)
            print("對方射向:", target, "結果:", bullet)
            damage = 1 + ai_bomb

            if target == "你": #射的是玩家
                if bullet == "真":
                    if player_shield:
                        ai_hp -= damage
                        player_shield = False
                        print("你的護盾反彈!")
                        turn = "player" #射對方必換回合
                    else:
                        player_hp -= damage
                        turn = "player"
                else:
                    turn = "player"#空包不換回合
            else: #射Ai自己
                if bullet == "真":
                    if ai_shield:
                        ai_hp -= damage  # 反彈扣自己
                        ai_shield = False
                        print("對方護盾反彈!")
                        turn = "ai"
                    else:
                        ai_hp -= damage
                        turn = "player"
                else:
                    turn = "ai"
            if ai_handcuff:
                turn = "ai"
                ai_handcuff = False
                print("你被禁錮，停止行動一輪!")
            ai_bomb = 0
            print("目前彈夾剩餘:", mag.count("真"), "真", mag.count("假"), "假")

        print("你的血量:", player_hp, "對方血量:", ai_hp)

# 遊戲結果
if player_hp <= 0:
    print("你輸了QQ")
else:
    print("你贏了！")