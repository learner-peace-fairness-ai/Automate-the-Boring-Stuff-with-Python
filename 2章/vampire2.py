name = input("name: ")
age = int(input("age: "))

if name == "Alice":
    print("やぁ、Alice。")
elif age < 12:
    print("Aliceじゃないね、お嬢ちゃん。")
elif age > 100:
    print("Aliceじゃないね。お婆ちゃん。")
elif age > 2000:
    print("Aliceはお前のような不死身ではない、吸血鬼め。")
