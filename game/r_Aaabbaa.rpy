label r_Aaabbaa:
    scene bg_room_day

    show shiori happy
    shiori "それじゃ探しますかー"
    koji "そうだね。"
    "２人で図鑑と花の写真を比較する。"
    "かなり根気のいる作業である。"
    "かなり疲れた。"
    show shiori tired
    "詩織なんて疲れすぎて目が細くなってる。"
    show shiori sleep
    koji "詩織？"
    "反応がない。"
    "寝てしまったのだろう。"
    "僕は近くにあった毛布を詩織にかけた。"
    koji "(かわいい寝顔だ。)"
    "その後も僕は図鑑とにらめっこした。"
    "図鑑の端から端まで見たが、結局花の正体を暴くことはできなかった。"
    show shiori troubled
    shiori "ん？おはよう？"
    "詩織が起きたようだ。"
    
    menu:
        "おはよう":
            koji "おはよう"
        "もうすぐこんばんはだよ":
            koji "もうすぐこんばんはだよ"
    
    show shiori hawawa
    shiori "はわわ、もうこんな時間！"
    show shiori troubled
    shiori "せっかく来てもらったのにもてなせなくてごめんね。"
    koji "大丈夫だよ"
    koji "それと"
    
    menu:
        "また今度本を読みにきていい？":
            koji "また今度本を読みにきていい？"
    
    show shiori happy
    shiori "もちろん。今日は紹介できなかったけど君に見せたい本もいっぱいあるよ。"
    "詩織はにこやかにそういった。"
    koji "日が暮れてきたし今日はもう帰るね"
    show shiori
    shiori "うん、また今度"
    
    menu:
        "ばいばい":
            koji "ばいばい"
        "またね":
            koji "またね"
    
    hide shiori
    scene black with fade

    "それからはたびたび詩織の家に招かれて一緒に本を読んだ。"
    "ただ毎回、僕か詩織が途中で寝てしまう。"
    "今日も詩織の家にいるが寝てしまうのだろうか。"

    scene bg room with fade

    koji "(やはりいつも寝てしまうのは、なぜなんだろう)"
    
    menu:
        "気にしない":
            jump r_Aend2
        "考察してみる":
            jump think_about_it

label think_about_it:
    koji "そういえば詩織は両親と一緒に住んでいるけど見かけたことは一切ないな。"
    "ZZZ"
    "その時、隣の部屋から寝息が聞こえた。"
    koji "誰かいるのかな"
    menu:
        "気にしない":
            jump r_Aend2
        "見に行ってみる":
            scene black with fade
            "その部屋には詩織の両親と思われる人が寝ていた。"
            "今日は週末であるが朝に僕が来た時から昼にさしかかろうという今の今までずっとねていたのだろうか"
            "それだけお仕事を頑張ったということだろうか"
            menu:
                "気にしない":
                    "もう頭が回らない。"
                    jump r_Aend2
    return