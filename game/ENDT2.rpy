label r_a_a_a_a_b_T2_a_a_a:
    "気づかれないように詩織の後を追った。"
    "詩織は本の試し読みをしていた。"
    "「転生するのスランプだった件」"
    "知らないタイトルの本である。"
    "うちには置いていない。"

    koji "(もしかしてうちにある本には飽きちゃったのかな...)"
    "それはつまり今後うちに来なくなるということであり大変ショッキングである。"
    "対するてーさいとには見渡す限り大量の本が並んでおり、"
    "全て読み切ることはほぼ不可能なほどである。"
    "悲しいかな物量差は歴然であった。"

    "ウゥ、ウゥ、ウゥ……。ア゛ーーーーーア゛ッア゛ーー！！！！"
    "突然背後からとんでもない轟音が響く。"
    "どうやら純愛ものだと思っていたら唐突なNTRれにより脳が破壊されたようだ。"
    "合掌。"

    shiori "あれ、浩二くん？"
    "いつの間にか詩織が側にいた。"
    "さしずめ轟音の方向に目を向けたら経路上にいた僕に気づいたのだろう。"

    shiori "お使いに来たの？"
    koji "そうだよ。詩織は何をしてたの？"
    "戸惑いのせいか我ながら愚問を投げてしまった。"

    shiori "んー、見られちゃったらしょうがないよね。"
    shiori "浩二くんに君が知らないであろう本を読み聞かせようと思って読み漁ってたの。"
    shiori "大きな本屋さんに行かないと君の知らない本なんて見つからないでしょ？"
    shiori "あぁ、もちろん君の本屋が小さいって言ってるわけじゃないからね。"

    koji "僕のために？"
    shiori "そう。あんなに楽しそうに聞いてくれた人は初めてだもん、嬉しかったからね。"
    "そういわれるとこっちも嬉しい。"

    shiori "でもよくよく考えてみたら君に読み聞かせる本なら君が選んだ方がいいんじゃない？"
    "確かにといわんばかりにうなずく。"

    shiori "今日は荷物で大変だろうから明日一緒に見て回らない？"

    menu:
        "いいよ、楽しみ":
            $ choice1 = "いいよ、楽しみ"
            jump T2_next1

label T2_next1:
    shiori "じゃあ決まりだね。"
    shiori "待って、もうこんな時間。私、塾があるから先に失礼するね。"

    koji "わかった、ばいばい～"
    shiori "また明日～"
    "そういって彼女は塾に向かっていった。"

    koji "僕も帰るか。"
    "材料を余分に買ってしまったせいで荷物は重かったが、帰路の足取りは軽かった。"
    "ちなみにばあちゃんがカレーを２人分食したので結果オーライである。"
    "パワフルなばあちゃんである。"

    "翌日、店に詩織がやってきた。"

    shiori "じゃあ本を探しにいこっか。"
    "僕は深くうなづいた。"
    "ばあちゃんに店を任せて２人でてーさいとに向かった。"

    "そこで今まで見たことも聞いたこともない本を大量に買った。"

    shiori "たくさん本を読んだから疲れたでしょ。"
    shiori "ほらこれ。"
    "そういって三角チョコパイを渡してくれた。"

    shiori "糖分の補給は大事だぞ。"
    koji "間違いないね。"

    menu:
        "いただきまーす":
            $ choice2 = "いただきまーす"
            jump T2_final

label T2_final:
    "三角チョコパイを思いっきり頬張る。"
    "とろとろとして甘いチョコとサクサクとしたパイ生地のデュエットが織りなす旋律は至極といって差し支えなく、"
    "後からチョコの苦みも加わり完璧なトリオへと昇華していった。"
    "三角チョコパイが三角である所以は調和のとれたこのトリオを物理的に表現したかったからではないだろうか、そうに決まっている。"

    koji "おいしい。"
    shiori "よかった。"
    shiori "あー"
    "突然、詩織は僕の頬を指でなぞる。"

    shiori "口にチョコがついてたぞ、みっともないぞ"
    "と詩織は笑う。"
    "突然直に触れられた私は赤面することしかできなかった。"

    shiori "なによその顔、こっちまで照れてきたじゃない///"
    "２人が赤面して向かい合うなんとも言えない構図となった。"

    shiori "ちょっと、ここ暑くない？"
    shiori "もう時間も時間だし外の風で涼みながら家に帰ろ？"
    koji "そうだね。"

    "２人は来た道を戻った。"
    "帰り道はお互いに何も話せなかった。"

    "店についてお別れの時間となった。"

    menu:
        "今日は楽しかったよ":
            $ choice3 = "今日は楽しかったよ"
        "今日は面白かったよ":
            $ choice3 = "今日は面白かったよ"

    shiori "うん、わたしも"

    menu:
        "また一緒に回ろう？":
            $ choice4 = "また一緒に回ろう？"
        "また一緒に出かけよう？":
            $ choice4 = "また一緒に出かけよう？"

    shiori "いいね、賛成"

    "ばあちゃんが店の奥から叫ぶ。"

    koji "じゃあ、呼ばれてるからこれでお開きだね。"
    shiori "そうだね、ばいばーい"
    koji "ばいばい！"
    "そして彼女は帰っていった。"
    "熱はまだ残っている。"
    "お持ち帰りのチョコパイですら冷えてしまうほど時間が経ってもなおである。"

    return
