label r_Aaab:
    koji "詩織が何をしているかは気になるところであったが、食材を抱えているということもあり帰宅することにした。"
    "帰宅途中に綺麗な花を見つけた。"
    koji "見たことない花だ。"
    "うちに植物図鑑が置いてないこともあり僕は植物に詳しくない。"
    koji "ばあちゃんならわかるかも。"
    "花を一輪摘み取る。"
    "せっかくの機会なので栞にしようか。"
    "店に戻ってばあちゃんに聞く。"
    koji "この花って知ってる？"

    baba "はて、わしでも見たことのない花じゃの。"
    "ばあちゃんがわからないなんて珍しいこともあるものである。"
    baba "それで材料はそろったか？"
    "ばあちゃんはウキウキでカレーを作った。"
    "材料を多めに買ってしまったが、カレーは僕が２人分食したので結果オーライである。"
    "我ながらパワフルである。"
    "次の日、詩織が店に来てくれた。"
    scene bg bookstore with fade
    show shiori
    koji "(何か話しかけるにちょうどいい話題はないかな？)"

    menu:
        "＞昨日、てーさいとで見かけた件について":
            jump topic_yesterday

        "＞謎の花について":
            jump topic_flower

label topic_yesterday:
    "昨日、てーさいとで見かけた件について話そうか。"
    # Add more dialogue and actions here
    show shiori at astonished2
    shiori"てーさいとで見かけた？人違いじゃないかな？"
    menu:
        "＞そうかな？":
            koji"そうかな？"
            "会話は弾まなかった"

        "＞そうかも":
            koji"そうかも"
            "会話は弾まなかった"
    jump topic_flower

label topic_flower:
    show shiori
    koji "謎の花について話そうか。"
    # Add more dialogue and actions here
    "詩織に謎の花を見せた"
    show shiori seriously
    shiori"なんだろう、この花。"
    shiori"うちにある植物図鑑になら載ってるかも。"
    "このチャンスを逃すなんてありえないだろう。"
    show shiori
    shiori"一緒にうちにきて確認する？"
    menu:
        "＞そうしよう":
            pass
        "＞遠慮しとく":
            "知らない女の子の姿が思い浮かぶ。"
            "これは..."
            "考えない方が身のためである"
            "やっぱり行こう"
    hide shiori

    scene bg root m with fade
    menu:
        "＞お邪魔します":
            scene bg room2 with fade
            "こうして僕は詩織の家に上がった。"
            "本棚に見たことのない本が大量に並んでいる。"
            "壮観である。"

    show shiori happy
    shiori"これしかなかったけどいいかな"
    "そういってアイスティーを渡される。"

    menu:
        "＞ありがとう":
            koji"ありがとう"
        "＞遠慮しとく":
            koji"遠慮しとく"
    jump r_Aaabbaa