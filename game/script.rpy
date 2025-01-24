﻿# script.rpy

# 必要な情報を初期化
label start:
    # タイトル画面から開始
    return

# 必要なキャラクターを定義
define koji = Character("浩二", color="#AABBFF")
define shiori = Character("詩織", color="#FFBBAA")
define baba = Character("婆", color="#CCCC99")

# プロローグ
label prologue:
    scene bg bookstore with fade
    koji "ここは商店街の一角にある本屋。商店街といっても賑わいとは程遠いものである。"
    koji "今となっては商店もほとんど畳まれていて、ただシャッターが連なる場所となった。"
    koji "当然買い物客など数えるほどしか歩いていない。"

    koji "そんなわけで逆風真っ只中の我が本屋は今日も閑散としている。悲しいかな。"

    baba "ばあちゃん、その話を何回したら気が済むんだよ。"
    baba "わしがこの話をしたのはこれが初めてじゃよ。"
    koji "そんなことない。昨日も同じことを言ってた。"
    baba "そうかの？"
    koji "そうだよ。最近物忘れが激しくない？僕の名前わかる？"
    baba "もちろんじゃ。確か..."
    baba "忘れた。"
    baba "何と言ったかの？"
    koji "田所浩二というのじゃな"
    koji "そうだよ。覚えておいてね。"
    baba "わしが忘れごとをしたことは生涯一度もないから安心せい。"
    koji "さっき僕の名前を忘れてたじゃん！"

    # 詩織登場
    "すいません～"
    koji "はい、どうされましたか？"
    shiori "この本を買いたいのですが。"
    koji "でしたらお代金1260円です。"
    shiori "じゃあこれで。"
    koji "1260円ちょうどですね、毎度ありがとうございます。"

    "彼女は買った本を抱えて帰路についた。"

    baba "どうした、顔が赤いぞ"
    menu:
        ">そんなことないって！":
            jump deny
        ">違うって！":
            jump deny
        ">全く君ってやつは！":
            jump agree

label deny:
    koji "そんなことないって！違うって！"
    baba "焦っとる焦っとる。お熱ですねぇ。"
    jump post_reaction

label agree:
    koji "全く君ってやつは！"
    baba "お熱ですねぇ。"
    jump post_reaction

label post_reaction:
    "ばあちゃんはそういって奥に入っていった。"
    koji "さっき赤面していたのは言うまでもない、僕は詩織に惚れているからである。"
    "時間があるときは詩織と2人で話をする。とはいえ僕はここ数年本屋の営業しかしていないから話題はもっぱら本のことである。"
    koji "どの本を読もうかな？"

    menu:
        "＞上杉鷹山伝":
            jump read_uesugi
        "＞真夏の夜の夢":
            jump read_summer

label read_uesugi:
    koji "よし、『上杉鷹山伝』を読もう。"
    return

label read_summer:
    koji "『真夏の夜の夢』か。いいね、これにしよう。"
    return
