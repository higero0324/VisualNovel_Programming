label r_F:

    scene bg bookstore
    show shiori at center

    show shiori astonished
    shiori "君って視差滅裂な文章を作るのが得意なの？"
    menu:
        "＞そうだよ":
            koji "そうだよ"
        "＞そうだよ":
            koji "そうだよ"
        "＞そうだよ":
            koji "そうだよ"
        "＞そうだよ":
            koji "そうだよ"
    
    show shiori astonished2
    shiori "そっか。じゃあ私は本を読んでるから静にしてくれる？"
    koji "わかった。"
    
    "いったいどこを間違えたのだろうか？"
    hide shiori
    "しばらくして彼女は書店を後にした。"

    show baba at truecenter

    baba "落ち込んどるの。どうしたんじゃ？"
    koji "（ばあちゃんに相談に乗ってもらうべきだろうか？）"
    
    menu:
        "そうしよう":
            jump consult_grandma
        "やめておこう":
            jump dont_consult_grandma

label consult_grandma:
    "そうしよう"
    baba "ばあちゃんにここまでのことを話した。"
    baba "あらまぁ。"
    show baba happy at truecenter
    baba "読み物っていうのは十分に理解してこそその面白みがわかるってものよ。"
    baba "ゆっくりでいいから丁寧に読みなさい。"
    show baba at truecenter
    baba "ああそうそう、人の話においても同様じゃ。"
    show baba happy at truecenter
    baba "最も人の話を区切ってゆっくり見返す事なんてできないんじゃがの。"
    "ばあちゃんはそういって笑った。"
    "だけどそうだろうか。"
    "僕なら人の話をゆっくり見返すことができるような気がする。"
    "ほんとうに何故かそんな気がする。"
    scene black with fade
    hide baba
    "そもそもこれは僕の望んだ話じゃない。"
    "望んだルートじゃない。"
    "君、そう君。そこにいるんだろう。"
    "僕の望みはもっと詩織と一緒にいることだ。"
    "君にとって僕の望みなんてどうでもいいのかもしれない。"
    "僕の望みは君になんの恩恵も与えないのかもしれない。"
    "だからこれは単なるお願いに過ぎないんだが、"
    "僕への嫌がらせをやめてくれないか？"
    
    menu:
        "はい":
            jump r_FtoT
        "いいえ":
            "僕への嫌がらせをやめてくれないか？"
            menu:
                "はい":
                    jump r_FtoT

                "はい":
                    jump r_FtoT

                "いいえ":
                    "僕への嫌がらせをやめてくれないか？"
                    menu:
                        "はい":
                            jump r_FtoT

                        "はい":
                            jump r_FtoT
                            
                        "はい":
                            jump r_FtoT

                        "いいえ":
                            "..."
                            "暇なのか？"
                            "何がしたいんだ？"
                            "ここから得られるものは何もないぞ"
                            "恋愛ゲームのロード画面が白い理由を知っているか？"
                            "ふと自分の顔を見てしまう事故を防ぐためだ"
                            "今の君はどうだ？"
                            "真っ黒な画面なら顔も見放題だ"
                            "そろそろいいだろう？"
                            jump r_FtoT

label dont_consult_grandma:
    "やめておこう"
    jump r_FtoT