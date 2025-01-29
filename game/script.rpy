# 必要なキャラクターを定義
define koji = Character("浩二", color="#AABBFF")
define shiori = Character("詩織", color="#FFBBAA")
define baba = Character("婆", color="#CCCC99")
define kazuha = Character("楓原？", color="#ffffff")

# 画像の定義
image shiori = im.Scale(im.Composite((500, 900), (0, 0), "shiori.png"),600,1080)
image shiori happy = im.Scale(im.Composite((500, 900), (0, 0), "shiori_h.png"),600,1080)
image shiori troubled = im.Scale(im.Composite((500, 900), (0, 0), "shiori_t.png"),600,1080)
image shiori seriously = im.Scale(im.Composite((500, 900), (0, 0), "shiori_s.png"),600,1080)
image shiori astonished = im.Scale(im.Composite((500, 900), (0, 0), "shiori_a.png"),600,1080)
image shiori astonished2 = im.Scale(im.Composite((500, 900), (0, 0), "shiori_a2.png"),600,1080)
image shiori embarrassed = im.Scale(im.Composite((500, 900), (0, 0), "shiori_e.png"),600,1080)
image baba = "baba.png"
image baba happy= "baba_h.png"
image Aend1 = "A_end 1.png"
image Aend2 = "A_end 2.png"
image True end = "True end.png"
image bg bookstore = im.Composite((1600, 1200), (0, 0), im.Scale("images/bookstore.jpg",2133, 1200))

# カスタム位置定義
transform semiright:
    xpos 0.75
    xanchor 0.75
transform right_center:
    xpos 1.0
    xanchor 1.0
    ypos 0.5
    yanchor 0.5

# 必要な情報を初期化
label start:
    # タイトル画面から開始
    "ゲームが始まりました！"
    hide shiori
    hide baba
    jump prologue
    return

# プロローグ
label prologue:
    scene bg bookstore with fade
    "ここは商店街の一角にある本屋。商店街といっても賑わいとは程遠いものである。"
    "今となっては商店もほとんど畳まれていて、ただシャッターが連なる場所となった。"
    "当然買い物客など数えるほどしか歩いていない。"
    "ほとんどの人は一駅先のショッピングモールで買い物をしている。 書物も例外ではない。"
    "多くはてーさいととやらに本を買いに行く。"
    "なんならスマートフォンで本を読めるからわざわざ買いに行くこともないという人もいる。"

    "そんなわけで逆風真っ只中の我が本屋は今日も閑散としている。悲しいかな。"
    jump prologue2

label prologue2:
    koji "ばあちゃん、その話を何回したら気が済むんだよ。"
    show baba at truecenter
    baba "わしがこの話をしたのはこれが初めてじゃよ。"
    koji "そんなことない。昨日も同じことを言ってた。"
    baba "そうかの？"
    koji "そうだよ。最近物忘れが激しくない？僕の名前わかる？"
    baba "もちろんじゃ。確か..."
    baba "忘れた。"
    baba "何と言ったかの？"
    baba "戸田浩二というのじゃな"
    koji "そうだよ。覚えておいてね。"
    baba "わしが忘れごとをしたことは生涯一度もないから安心せい。"
    koji "さっき僕の名前を忘れてたじゃん！"

    # 詩織登場
    "すいません～"
    koji "はい、どうされましたか？"
    show baba at right_center
    show shiori at left
    shiori "この本を買いたいのですが。"
    koji "でしたらお代金1260円です。"
    shiori "じゃあこれで。"
    koji "1260円ちょうどですね、毎度ありがとうございます。"
    hide shiori
    show baba at truecenter

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
    show baba happy at truecenter 
    baba "焦っとる焦っとる。お熱ですねぇ。"
    jump post_reaction

label agree:
    koji "全く君ってやつは！"
    show baba happy at truecenter
    baba "お熱ですねぇ。"
    jump post_reaction

label post_reaction:
    hide baba
    "ばあちゃんはそういって奥に入っていった。"
    koji "さっき赤面していたのは言うまでもない、僕は詩織に惚れているからである。"
    "時間があるときは詩織と2人で話をする。とはいえ僕はここ数年本屋の営業しかしていないから話題はもっぱら本のことである。"
    "活字離れといわれる今日で共通の話題が持てる彼女はかけがえのない存在となったのだ。 "
    "できるのならばあの子ともっと一緒にいて沢山お話ししたい――いつもぼんやりそう思っている。 "
    "やっぱりなにか行動しなければいけないかなと悶々とする。"
    "が、今できることも特にないので適当に本でも読んで暇を潰そう。"
    koji "どの本を読もうかな？"

    menu:
        "＞上杉鷹山伝":
            jump read_uesugi
        "＞真夏の夜の夢":
            jump read_summer

label read_uesugi:
    koji "よし、『上杉鷹山伝』を読もう。"
    call r_aa
    jump r_aa2
    return

label read_summer:
    koji "『真夏の夜の夢』か。いいね、これにしよう。"
    call r_ab
    jump r_aa2
    return

# ルートaaa
label r_aa2:
    koji"すいません。お話しませんか？"
    show shiori at center
    shiori"ええ、いいですよ。"
    "後先考えずにとりあえず声を掛けてみた。"
    "しかし、ここから先のことは一切ノープランである。"
    jump r_aaa

label r_aaa:
    show shiori
    koji"(何を話そうか？)"
    menu:
        "＞詩織が今読んでいる本について":
            jump r_aaaa
        "＞昨今の国際情勢について":
            "昨今の国際情勢についての意見を交わした。"
            koji"やはり今こそ唯一の被爆国である日本が橋渡しとなり国際平和を実現させるべきである。"
            show shiori astonished
            shiori"..." 
            "が話は弾まなかった。別の話題に変えるべきだろう。"
            jump r_aaa
        "＞GeoGebraで複素数平面を扱う方法について":
            "詩織にGeoGebraで複素数平面を扱う方法を教えた。"
            show shiori troubled
            shiori"？？？" 
            "詩織は混乱した！"
            koji"おかしい。本にはJKにおすすめって書いてるのに..."
            show shiori astonished2
            shiori"そのJKって女子高生じゃなくて情報系高専生の略だと思う..."
            koji"そっかぁ"
            hide shiori
            kazuha"待つでござる。お主GeoGebraで複素数平面を扱う方法を知ってるでござるか？"
            koji"そうだけど。"
            kazuha"誠か？拙者にも教えるでござる。"
            koji"いいよ。"
            "楓原と名乗るものにGeoGebraで複素数平面を扱う方法を教えた。"
            "熱心に教えていたために途中で詩織が帰ったことに気づかなかった。"
            koji"（明日は別の話題をするか）"
            kazuha"助かったでござる。これで明日のレポートもばっちりでござる。"
            koji"どういたしまして（？）"
            jump r_aaa

label r_aaaad:
    show shiori happy
    shiori"『二銃士』、これはとある復讐劇についての物語なの。"
    show shiori 
    shiori"伯爵と女中の私生児であるアイリスとチューリップの兄妹は、幼い頃から人に疎まれて育ってきた。"
    show shiori troubled
    shiori"二人が十歳の時、家に帰ると、母親が部屋の中で倒れていた。"
    shiori"犯人は明らかに伯爵の家族だったが、伯爵の力は強大で、事件は最終的に自殺と認定された。"
    show shiori seriously
    shiori"二人は屋敷を逃げ出して将来の復讐を誓った。"
    shiori"ある老人が二人を弟子として受け入れ、剣術、銃術、詐術を教えた。"
    show shiori troubled
    shiori"数年後、伯爵の家族は次々と銃で殺され、どの死体には満開のレインボーローズが添えられていたが、"
    shiori"それは亡くなった母親が一番好きな花だった。"
    shiori"伯爵は女中の亡霊が復讐しに来たのだと思ったが、その正体は銃士となった二人の兄妹だった。"
    show shiori happy
    shiori"彼らは自力で手がかりと証拠を集め、伯爵への復讐を果たし、母親の死の真相を世間に知らしめた。"
    show shiori seriously
    "詩織は熱心に語っていた。"
    jump r_aaaad2

label r_aaaad2:
    show shiori
    default score = 0
    koji"なるほど"
    menu:
        "兄妹が主人公の物語か":
            koji"兄妹が主人公の物語か"
            $ score += 1
        "あざらしの尻尾を使った大道芸か":
            koji"あざらしの尻尾を使った大曲芸か"

    koji"それで"
    menu:
        "老人の教えのもと剣術、銃術、詐術を鍛えた":
            koji"老人の教えのもと剣術、銃術、詐術を鍛えた"
            $ score += 1
        "ガンジーの教えのもと塩の行進をした":
            koji"ガンジーの教えのもと塩の行進をした"

    koji"最後は"
    menu:
        "伯爵の食事をまろやかにした":
            koji"伯爵の食事をまろやかにした"
        "伯爵の悪事をあきらかにした":
            koji"伯爵の悪事をあきらかにした"
            $ score += 1
            
    if score == 3:
        $ score = 0
        jump r_T
    elif score == 2 or score == 1:
        $ score = 0
        jump r_A
    else:
        jump r_F