label r_Aend1:
    "気づかれないように詩織の後を追った。"
    show shiori at semiright
    "詩織は本の試し読みをしていた。"
    "「転生するのスランプだった件」"
    "知らないタイトルの本である。うちには置いていない。"
    "（もしかしてうちにある本には飽きちゃったのかな...）"
    "それはつまり今後うちに来なくなるということであり大変ショッキングである。"
    "対するてーさいとには見渡す限り大量の本が並んでおり、全て読み切ることはほぼ不可能なほどである。"
    "悲しいかな物量差は歴然であった。"

    # 突然の轟音
    "{b}ウゥ、ウゥ、ウゥ……。ア゛ーーーーーア゛ッア゛ーー！！！！{/b}"
    "突然背後からとんでもない轟音が響く。"
    "どうやら純愛ものだと思っていたら唐突なNTRれにより脳が破壊されたようだ。"
    "合掌。"
    
    show shiori troubled at center
    shiori "あれ、浩二くん？"
    "いつの間にか詩織が側にいた。"
    "さしずめ轟音の方向に目を向けたら経路上にいた僕に気づいたのだろう。"
    
    show shiori
    shiori "お使いに来たの？"
    koji "そうだよ。詩織は何をしてたの？"
    "戸惑いのせいか我ながら愚問を投げてしまった。"
    show shiori astonished
    shiori "んー、見られちゃったらしょうがないよね。"
    show shiori happy
    shiori "浩二くんに君が知らないであろう本を読み聞かせようと思って読み漁ってたの。"
    show shiori
    shiori "大きな本屋さんに行かないと君の知らない本なんて見つからないでしょ？"
    show shiori troubled
    shiori "あぁ、もちろん君の本屋が小さいって言ってるわけじゃないからね。"

    koji "僕のために？"
    show shiori happy
    shiori "そう。あんなに楽しそうに聞いてくれた人は初めてだもん、嬉しかったからね。"
    
    "そういわれるとこっちも嬉しい。"

    show shiori happy
    shiori "でもよくよく考えてみたら君に読み聞かせる本なら君が選んだ方がいいんじゃない？"
    koji "確かに。"
    show shiori
    shiori "今日は荷物で大変だろうから明日一緒に見て回らない？"
    
    menu:
        ">いいよ、楽しみ":
            koji"いいよ、楽しみ"
            show shiori happy
            shiori "じゃあ決まりだね。"

    show shiori
    shiori "待って、もうこんな時間。私、塾があるから先に失礼するね。"
    koji "わかった、ばいばい～"
    show shiori happy
    shiori "また明日～"
    
    "そういって彼女は塾に向かっていった。"
    hide shiori
    koji "僕も帰るか。"
    "材料を余分に買ってしまったせいで荷物は重かったが、帰路の足取りは軽かった。"
    "ちなみにばあちゃんがカレーを2人分食したので結果オーライである。"
    
    scene black with fade
    scene bg bookstore with fade
    
    show shiori
    "翌日、店に詩織がやってきた。"
    show shiori happy
    shiori "じゃあ本を探しにいこっか。"
    
    "僕は深くうなづいた。"
    scene black with fade

    "ばあちゃんに店を任せて2人でてーさいとに向かった。"
    "そこで今まで見たことも聞いたこともない本を大量に買った。"

    scene bg root
    show shiori
    shiori "たくさん本を読んだから疲れたでしょ。"
    show shiori
    shiori "ほらこれ。"
    
    show shiori happy
    shiori "糖分の補給は大事だぞ。"
    koji "間違いないね。"
    menu:
        ">いただきまーす":
            koji "いただきま-す。"
    "三角チョコパイを思いっきり頬張る。"
    hide shiori
    scene bg my world with fade
    "とろとろとして甘いチョコとサクサクとしたパイ生地のデュエットが織りなす旋律は至極といって差し支えなく、"
    "後からチョコの苦みも加わり完璧なトリオへと昇華していった。"
    "三角チョコパイが三角である所以は調和のとれたこのトリオを物理的に表現したかったからではないだろうか、"
    "そうに決まっている。"
    scene bg root
    show shiori

    koji "おいしい。"
    show shiori happy
    shiori "よかった。"

    shiori "あー"
    show shiori seriously
    shiori "突然、詩織は僕の頬を指でなぞる。"
    shiori "口にチョコがついてた、みっともないぞ。"
    show shiori happy

    "詩織は笑う。"
    "突然直に触れられた私は赤面することしかできなかった。"

    show shiori embarrassed
    shiori "なによその顔、こっちまで照れてきたじゃない///"
    
    "2人が赤面して向かい合うなんとも言えない構図となった。"

    shiori "ちょっと、ここ暑くない？"
    show shiori happy
    shiori "もう時間も時間だし外の風で涼みながら家に帰ろ？"
    
    "静寂を切り裂くように詩織がつぶやく。"
    koji "そうだね。"

    scene black with fade

    "2人は来た道を戻った。"
    "帰り道はお互いに何も話せなかった。"
    

    "店についてお別れの時間となった。"
    
    scene bg front bookstore with fade
    show shiori


    menu:
        ">今日は楽しかったよ":
            show shiori happy
            shiori "うん、わたしも楽しかった。"
        ">今日は面白かったよ":
            show shiori happy
            shiori "そうだね、わたしも面白かった。"

    menu:
        ">また一緒に回ろう？":
            show shiori happy
            shiori "いいね、賛成！"
        ">また一緒に出かけよう？":
            show shiori happy
            shiori "うん、楽しみにしてる。"

    show shiori

    baba "{b}浩二よ、帰ってきたなら手伝ってほしいのぉ～。{/b}"
    koji "じゃあ、呼ばれてるからこれでお開きだね。"

    show shiori happy

    shiori "そうだね、ばいばーい"

    koji "ばいばい！"
    
    "そして彼女は帰っていった。"
    hide shiori
    "熱はまだ残っている。"
    "お持ち帰りのチョコパイですら冷えてしまうほど時間が経ってもなおである。"
    #end

    scene black with fade

    pause

    show Aend1 with fade

    window hide

    pause

    window show

    "Route Escaping Reality"
    return