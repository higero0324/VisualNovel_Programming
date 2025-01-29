label r_A:
    show shiori troubled
    shiori "私の言ってる内容とあんまりかみ合ってないよ？大丈夫？しんどいの？"
    menu:
        "ちょっとしんどいかも":
            koji"ちょっとしんどいかも"
            jump r_Aa


        "大丈夫":
            koji"大丈夫"
            show shiori seriously
            shiori "もう一回いうからちゃんと聞いてね"
            jump r_aaaad

label r_Aa:
    show shiori 
    shiori"わかった。"
    show shiori seriously
    "詩織は『二銃士』を読んでくれた。"
    show shiori happy
    "澄んだ声での朗読には心底うっとりした。"
    "それはもう素晴らしいものであった気がする。"
    "気がする..."
    hide shiori
    scene white with fade
    #寝る
    pause

    scene bg bookstore with fade
    "あまりにも心安らかになりすぎていつの間にか寝てしまったらしい。"
    show baba at truecenter
    baba "起きたか。詩織さんが面倒見てくれてたんだからこんどお礼するんじゃぞ。"
    koji "わかった。ところで詩織さんは？"
    baba "あんたが寝てる間に日が暮れたから帰っていったわ。"
    show baba happy at truecenter
    baba "かわいい寝顔ですねーーだってさ"
    "そういわれた後、あまりの紅潮のせいでまたぶっ倒れたらしい。"
    hide baba
    scene white with fade
    #次の日
    "次の日"
    pause
    
    scene bg bookstore with fade
    koji"今日はもっとしっかりしないと。" 
    "昨日は快眠だった分、気合が入る。"
    "店の掃除、ポップ作成、ばあちゃんの肩たたき... "
    "だがその日、詩織が店に来ることはなかった。"
    koji"（人間忙しいときもあるよなぁ）"
    "翌日も詩織は姿を見せなかった。"
    "ほぼ毎日来店する彼女がこれほど来ないとなると色々と心配になる。"
    "体調が優れないのだろうか。"
    show baba at truecenter
    baba"どうした、元気がないのぉ。"
    baba"じゃあ今晩は元気が出るわしの特製カレーを作ってやる。"
    baba"じゃから材料のお使いを頼みたい。"
    menu:
        "＞合点承知の助":
            koji"合点承知の助"

        "＞了解":
            koji"了解"

        "＞はい、よろこんで":
            koji"はい、よろこんで"

    "恐らく適当に理由を付けて自らの好物であるカレーを作りたいだけな気がするが、"
    "こちらとしてもあのカレーの為ならばお使いを拒めるわけがない。"
    koji"ばあちゃんのカレーは世界一だもんね"
    show baba happy 
    baba"嬉しいコト言ってくれるねぇ。"
    hide baba
    scene white with fade
    scene bg shop with fade
    "こうして僕はカレーの材料を揃えに買い物に出た。"
    "カレーというのは肉や野菜にはじまりルーなど様々なものが要求される。"
    "悔しいがこういう時はスーパーの品ぞろえの良さが頼りになる。"
    "そのため、スーパーが内蔵されている謎の本屋てーさいとに行くことにした。"
    "そして..."
    scene bg Tsite with fade
    koji"買いすぎてしまった。"
    "スーパーに行って材料を揃えたはいいものの完全に量を誤ってしまった。"
    "いつもの癖で３人分の材料を買ってしまったのだ。"
    menu:
        "＞（仕方がないから僕が２人分食べるか）":
            koji"（仕方がないから僕が２人分食べるか）"

        "＞（仕方がないからばあちゃんに2人分おしつけるか）":
            koji"（仕方がないからばあちゃんに2人分おしつけるか）"
    
    "さて帰ろうかと思っていた矢先であった。"
    show shiori at semiright
    "本屋のほうに見慣れた姿が見える。"
    koji"詩織？"
    "その声は当然人ごみのなかにかき消されて彼女には届かない。"
    hide shiori
    "そして彼女は奥の方へと消えていった。"
    koji"(後を追ってみるべきだろうか？)"
    menu:
        "＞もちろんだ":
            koji"もちろんだ"
            jump r_Aend1

        "＞やめておこう":
            koji"やめておこう"
            jump r_Aaab

