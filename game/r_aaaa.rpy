label r_aaaa:
    show shiori
    koji "「何の本を読んでるの？」"
    shiori "『二銃士』っていう本。"

    menu:
        "＞知ってる！ある黒板アート職人の伝記だよね。":
            koji"知ってる！ある黒板アート職人の伝記だよね。"
            show shiori astonished
            shiori"何言ってるの？"
            koji"（どうやら間違えたみたいだ）"
            jump r_aaaa
        "＞知ってる！4人の銃士についての物語だよね。":
            koji"知ってる！4人の銃士についての物語だよね。"
            show shiori astonished2
            shiori"それは『三銃士』じゃないかな？" 
            koji"（確かにそうかも）"
            jump r_aaaa
        "＞知ってる！東急リバブルは年間2万件仲介してるって。":
            koji"知ってる！東急リバブルは年間2万件仲介してるって。"
            show shiori happy
            shiori"よく知ってるね"
            scene white with fade
            hide shiori
            "2人はそのまま東急リバブルの話をした。"
            "マンボウが1億匹の卵を産むことも、"
            "マジって言葉が江戸時代からあったことも知らなかったが、"
            "東急リバブルが海外展開していることは知っている。"
            "そのまま２人は大人になり上京し、東急リバブルで家を買った。"
            "そして東急リバブルの窓の景色に想いを馳せ、東急リバブルのベットで横になる。"
            "そして瞼を閉じる。"
            scene bg bookstore with fade
            show baba at truecenter
            baba "何をボーとしている。話をちゃんときかんか。"
            koji "どうやら夢だったようだ。"
            "そしてまたばあちゃんの長話が始まる..."
            jump prologue2

        "＞知らない！なにその本？":
            koji"知らない！なにその本？"
            jump r_aaaad

