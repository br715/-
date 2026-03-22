import random
#新題庫
questions = [
    {"answer": "岳陽樓記", "hint": "陰風怒號，濁浪排空", "author": "范仲淹", "dynasty": "宋", "type": "散文",
     "story": "出自范仲淹的岳陽樓記，表達了洞庭湖在陰雨連綿的天氣下的景象。"},

    {"answer": "晚遊六橋待月記", "hint": "一日之盛，為朝煙，為夕嵐", "author": "袁宏道", "dynasty": "明", "type": "散文",
     "story": "出自袁宏道的晚遊六橋待月記，表達西湖一天當中最美的兩個時段。"},

    {"answer": "桃花源記", "hint": "芳草鮮美，落英繽紛", "author": "陶淵明", "dynasty": "東晉", "type": "詩序",
     "story": "出自陶淵明的桃花源記，描寫了桃花源中的景色。"},

    {"answer": "天淨沙秋思", "hint": "枯藤老樹昏鴉", "author": "馬致遠", "dynasty": "元", "type": "曲",
     "story": "出自馬致遠的天淨沙秋思，描繪了深秋黃昏的蕭瑟景象，抒發了遊子漂泊天涯的孤獨與悲愁。"},

    {"answer": "浪淘沙", "hint": "羅衾不耐五更寒", "author": "李煜", "dynasty": "五代十國", "type": "詞",
     "story": "出自李煜的浪淘沙令簾外雨潺潺，亡國後身為階下囚的凄慘孤獨、身體寒冷與心靈痛楚的淒涼寫照。"},

    {"answer": "出師表", "hint": "先帝創業未半而中道崩殂", "author": "諸葛亮", "dynasty": "三國", "type": "表",
     "story": "出自諸葛亮的出師表，表達諸葛亮對劉備辭世的痛惜，以及蜀漢基業未穩的危急感。"},

    {"answer": "赤壁賦", "hint": "寄蜉蝣於天地，渺滄海之一粟", "author": "蘇軾", "dynasty": "宋", "type": "文賦",
     "story": "出自蘇軾的赤壁賦，表達人對於天地而言是如此的渺小。"},

    {"answer": "師說", "hint": "句讀之不知，或之不解，或師焉，或否焉", "author": "韓愈", "dynasty": "唐", "type": "論說文",
     "story": "出自韓愈的師說，意爲人遇到大問題不求問於師，只問在句字標點停頓這種小問題方面，批評當時士大夫顛倒主次、不肯真正求師的「小學而大遺」錯誤態度，諷刺其不明智。"},

    {"answer": "禮記．禮運大同篇", "hint": "老有所終，壯有所用，幼有所長", "author": "孔子", "dynasty": "春秋",
     "type": "論說文",
     "story": "出自大同與小康，表達孔子理想中的大同世界。"},

    {"answer": "論語", "hint": "知之為知之，不知為不知，是知也", "author": "孔子", "dynasty": "春秋", "type": "語錄體",
     "story": "出自論語，強調實事求是、誠實不虛假的治學與處世態度，反對不懂裝懂。"}]

print("=== 射覆遊戲 ===")
print("你詢問後，我回答正確與否，推測到次數用盡為止吧!")
score = 0
num_questions = 10
asked = random.sample(questions, num_questions)

for q in asked:
    print("\n提示句：", q["hint"])
    attempts = 20
    while attempts > 0:
        print(f"\n剩餘次數：{attempts}")
        print("你可以做的事：")
        print("1. 問作者")
        print("2. 問朝代")
        print("3. 問體裁")
        print("4. 猜詩名")
        print("5. 選單提示")
        choice = input("請輸入選項 (1-5)：")

        if choice == "1":
            guess = input("你猜作者是：")
            print("是" if guess == q["author"] else "否")
            attempts -= 1

        elif choice == "2":
            guess = input("你猜朝代是：")
            print("是" if guess == q["dynasty"] else "否")
            attempts -= 1

        elif choice == "3":
            guess = input("你猜體裁是：")
            print("是" if guess == q["type"] else "否")
            attempts -= 1

        elif choice == "4":
            guess = input("請輸入詩名：")
            if guess in q["answer"]: #模糊輸入答案的一部分就算對
                print("答對了！正確答案是：", q["answer"])
                print("典故：", q["story"])
                score += 1
                break
            else:
                print("答錯")
                attempts -= 1

        elif choice == "5":
            print("\n--- 選擇提示 ---")
            print(
                "\n答案在之中:岳陽樓記、晚遊六橋待月記、桃花源記、天淨沙秋思、浪淘沙、出師表、赤壁賦、師說、禮記．禮運大同篇、論語")
            attempts -= 1

        else:
            print("輸入錯誤，請輸入 1~5")

    else:
        print("次數用完了，正確答案是：", q["answer"])
        print("典故：", q["story"])

print("\n=== 遊戲結束 ===")
print("你總共答對了", score, "題 /", num_questions)
