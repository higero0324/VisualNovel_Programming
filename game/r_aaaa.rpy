label r_aaaa:
    koji "「何の本を読んでるの？」"
    shiori "『二銃士』っていう本。"
    menu:
        "＞知ってる！ある黒板アート職人の伝記だよね。":
            koji"知ってる！ある黒板アート職人の伝記だよね。"
            return
        "＞知ってる！4人の銃士についての物語だよね。":
            koji"知ってる！4人の銃士についての物語だよね。"
            return
        "＞知ってる！東急リバブルは年間2万件仲介してるって。":
            koji"知ってる！東急リバブルは年間2万件仲介してるって。"
            return
        "＞知らない！なにその本？":
            koji"知らない！なにその本？"
            jump r_aaaad

