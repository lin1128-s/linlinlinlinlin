################################################################################
## 第一章 · 雨季
################################################################################

init python:

    POEM = [
        "我打江南走过",
        "那等在季节里的容颜如莲花的开落",
        "东风不来，三月的柳絮不飞",
        "你的心如小小的寂寞的城",
        "恰若青石的街道向晚",
        "跫音不响。三月的春帷不揭",
        "你的心是小小的窗扉紧掩",
        "我达达的马蹄声是美丽的错误",
        "我不是归人。是个过客……",
    ]


label chapter_one:

    scene black

    $ renpy.music.set_volume(0.55, delay=0.0, channel="music")
    play music audio.bgm fadein 8.0

    pause 1.2

    call screen poem_card(POEM)

    pause 0.4

    ## 雨声起 ##################################################################

    $ renpy.music.set_volume(0.55, delay=0.0, channel="rain")
    play rain audio.rain fadein 6.0

    call screen chapter_card("序", "开幕", "九月十七日 · 雨")

    scene bg room night
    with Dissolve(2.2)

    pause 0.8

    "早晨，我是在雨声中醒来的。"

    "窗外的雨似乎比睡前更大了一些，玻璃上翻涌的水珠几乎快要逆流。"

    "我迷惑地睁开眼，盯着窗外发了很长时间的呆。"

    "在过去几个月里，我睁开眼睛面对的似乎都是同样的场景——"

    "一片白茫茫的、隐藏在瓢泼大雨中的嘈杂世界。一切光影与声音都蒸腾着水汽，直至融为一体，仿佛凝结的时间。"

    "A市的雨季似乎永远不会有尽头。从四月开始，雨就一场接着一场，没完没了。"

    "它冲走了飘飞的柳絮，又将枝头的桂花打落，连空气闻起来也快要发霉。"

    "一切都笼罩在一层水雾中，朦胧不清。每到这时候，A市就仿佛进入了另一个世界。"

    "人们都说，这是厄尔尼诺现象带来的。圣婴的哭泣带来了太平洋踯躅的水汽，淹没了这座小小的城市。"

    heart "可我却觉得，这场旷日持久的大雨仿佛并非真实的，而是在人们心里坠下的。"

    "我翻了个身，看着自己醒来的房间，只感到一种熟悉的陌生。"

    "为了图便宜，我在学校附近租了一间廉价的一居室。这栋楼由废弃的大学教职工宿舍改造而成，房东是许多年前毕业、如今已经秃顶的老学长。"

    "他买下这栋楼本来是想开麻将馆，后来受限于政策，只好改成公寓，租金也只是象征性地收一点点。"

    "如果抛开那些关于鬼怪、狐狸和连环杀人犯的荒诞传闻，这里是A大学生除了狭小逼仄的六人间外，为数不多的第二选择。"

    "房间的采光算不上很好。不过在这样一座阴雨连绵的城市，倒也无所谓——天空的色调永远是铅灰色，太阳有一半的时间都是缺席的。"

    "这里的一切陈设都是纯白的：白床、白桌椅、白色五斗柜、白油漆墙面、白油布地板。就连不锈钢衣架上也永远晾着一排排带着水汽味的白棉布衬衫。"

    heart "看起来就像病房。"

    "唯一不同的是那些到处都是的书和电子设备。"

    "尤其是书籍。它们到处都是，却唯独不在书架上。"

    "我熟悉这里的每一处角落，却总有种奇怪的感觉——房间里有一块地方是空的。"

    "这种感觉就像一栋房子里搬走了一件家具，地板上还留着四个浅浅的印子。你知道那里曾经放过什么东西，却怎么也想不起来。"

    "我想找寻这种感觉的源头，头却开始疼痛——"

    ## 闪回 ####################################################################

    $ renpy.block_rollback()

    stop rain fadeout 1.0
    play sound audio.heart

    show white_flash at flash_anim

    pause 0.22

    hide white_flash

    scene bg room white at warm_light
    with flash_white

    $ renpy.music.set_volume(0.30, delay=0.0, channel="music")

    "一个巨大的玩具熊。"

    scene bg room white at warm_light_wide
    with cut_fast

    "一个女孩的背影。"

    scene bg room white at warm_light
    with cut_fast

    "一些干枯的花朵。"

    scene bg room white at warm_light_wide
    with flash_white

    "男孩在老旧的电脑前，女孩趴在地上的毯子上看书……"

    scene bg room white at warm_light
    with cut_fast

    "太阳、雨、玩水的声音和孩子的笑声。"

    pause 0.9

    scene black
    with flash_white

    "消失——"

    scene bg room night
    with Dissolve(1.4)

    play rain audio.rain fadein 2.0
    $ renpy.music.set_volume(0.55, delay=1.0, channel="music")

    "除此之外，什么声音都没有。"

    heart "真安静。就好像这个世界上只剩下我一个人了。"

    "……一定是最近没睡好。"

    "我揉了揉太阳穴，希望能将这种晕眩的感觉按回去。"

    "手机屏幕亮着：7:02，9月17日，星期四，雨转阴。"

    lin "尽他妈扯淡，这雨哪有停的迹象。"

    "雨确实停了。"

    "就好像我说完这句话后，梦突然醒了，世界被刷新了一样。"

    stop rain fadeout 3.0

    "汽笛声、人声，从很远的地方浮上来。"

    "我趿拉着拖鞋，去卫生间刷牙。"

    ## 便利贴 ##################################################################

    "镜子上贴着一张便利贴。字迹清秀——"

    call screen note_card

    "「早上第一节有课，别又不吃早饭。雨」"

    "旁边还画了个可爱的兔子头和一个大大的猪头。"

    "我盯着那张便利贴看了几秒。"

    lin "雨？"

    ## 早餐 ####################################################################

    "等我来到客厅时，桌子上已经摆放着炸好的油条、辣酱和胡辣汤，还冒着腾腾的热气。"

    heart "这是谁买的？"

    "雨啊。"

    heart "「雨」是谁？"

    "我努力想着这个问题，但就好像脑海中有什么雾气将答案遮挡。"

    play rain audio.rain fadein 2.0

    "雨，又重新下了起来。"

    "带着胡椒香气的热流驱散了无处不在的湿气，人总算是活过来了些。"

    "吃完饭后，我把伞扛到肩上，走进了雨里。"

    heart "雨到底是谁呢？"

    pause 0.7

    "……白雨啊。"

    "我拍了一下自己的脑袋。记忆像是突然插进来一块。"

    heart "为什么我总是会下意识忘掉她？白雨怎么能忘呢。"

    scene black
    with Dissolve(1.2)

    stop rain fadeout 2.0

    pause 0.6

    call screen chapter_card("第二幕", "归人", "同日 · 夜")

    ## 第二幕 ##################################################################

    scene black

    play rain audio.rain_heavy fadein 2.0
    $ renpy.music.set_volume(0.55, delay=0.0, channel="rain")

    show rain_far
    show rain_near

    "黑色的雨如同沥青，将霓虹碾作点点荧光。"

    "居住在鸽笼里的人和城市一样，都变为孤岛。"

    pause 0.8

    hide rain_far
    hide rain_near

    scene bg room night
    with Dissolve(1.6)

    play amb audio.tv fadein 2.0
    $ renpy.music.set_volume(0.55, delay=0.0, channel="amb")

    "新闻里女主持人甜美的嗓音推送着2607号台风登陆的最新消息。伴随的，是窗外狂怒的风声。"

    "一盏昏黄的台灯，书桌上摊着几本教材，旁边是一杯凉透的咖啡。"

    "我坐在电脑前，屏幕上是气象数据的图表。"

    "我揉了揉眼睛，伸了个懒腰。"

    ## 敲门 ####################################################################

    play sound audio.knock

    "咚、咚、咚。"

    "声音不大，却异常清晰，在雨声中显得突兀。"

    "我愣了一下，转头看向房门。"

    heart "……谁啊？"

    unknown "我！抄水表的。"

    "一个清脆的女声传来。"

    "来了。"

    "我拉开门——"

    ## 门外 ####################################################################

    scene bg corridor
    with Dissolve(0.7)

    play sound audio.door

    show baiyu calm at slide_in_left, night_light

    "门外的走廊灯昏暗。一个娇小的女孩站在那里。"

    "她穿着一件洗得发白的蓝色连衣裙，整体看上去湿漉漉的，却奇怪地——身上没有一滴水。"

    "这种矛盾的感觉还体现在其他地方：她身后拖着一口巨大的行李箱，箱子几乎比她人还高，轮子在地板上留下一道浅浅的水痕。"

    play sound audio.suitcase

    show baiyu laugh
    with Dissolve(0.2)

    baiyu "嗨，我回来啦。"

    lin "……你是？"

    show baiyu calm
    with Dissolve(0.2)

    baiyu "白雨啊。"

    "你小时候最好的朋友，后来转学离开的那个。你不记得了吗？"

    "她歪了歪头，笑容里带着点狡黠，像是在说一件再自然不过的事。"

    lin "白雨……？我好像……听过这个名字。"

    baiyu "当然听过。你爸妈肯定经常提起我呢。"

    baiyu "你小时候总跟着我跑，像个跟屁虫。你那时候一直白雨姐姐、白雨姐姐地喊呢。"

    "她往前一步，凑得很近。我几乎能闻见她发间充满糖果香气的柑橘味洗发露气味，一时间有些心慌。"

    "我下意识退了退。"

    "这时我看到了她的眼睛——与那副中学生般的娇小身体不同，这双眼睛充满了怜悯、疲惫和一种难言的复杂。"

    "我的警惕没来由地消失了，随之升起的，是一种奇怪的柔软的心情。"

    heart "（或许要很久很久之后，我才能明白，这是某种已被遗忘的愧疚。）"

    show baiyu smile
    with Dissolve(0.2)

    baiyu "我回A市上学啦，就在你隔壁的K大。从你爸妈那儿问到地址，就直接过来了。没想到吧？"

    "我看着她，脑子里像是有什么东西在轻轻晃动。"

    "记忆的碎片——雨声、白衣服的影子、模糊的笑声——一闪而过，抓不住。"

    "她说得那么自然。自然得让我觉得……如果我追问，反而显得我奇怪。"

    lin "……进来吧。外面雨大。"

    ## 屋内 ####################################################################

    scene bg room night
    with Dissolve(0.6)

    show baiyu smile at stand, night_light

    play sound audio.suitcase

    "白雨拖着箱子走进来。箱子擦过门框，发出轻微的摩擦声。"

    "她环顾四周，目光落在书桌上那杯凉咖啡上。"

    show baiyu calm
    with Dissolve(0.2)

    baiyu "你还是这个习惯，咖啡放凉了也不喝。"

    "我关上门。"

    $ renpy.music.set_volume(0.30, delay=1.2, channel="rain")

    "雨声被隔在外面，突然安静下来。"

    show baiyu sad
    with Dissolve(0.3)

    baiyu "我其实一点也不喜欢下雨，但……"

    "她的声音忽然变得很轻，像是水汽弥散在空气中。后面的话，模糊不清。"

    lin "什么？"

    "白雨已经走到窗边，拉开窗帘一角，望着外面的雨幕。"

    baiyu "没什么。就是觉得……这雨，下得真好。"

    ## 新闻 ####################################################################

    "电视新闻的声音从卧室里隐约传来——"

    news "……台风「丁香」已于今日登陆A市，预计未来一周将持续强降雨，市民需注意防范……"

    "白雨转过头，看着我，眼睛亮亮的。"

    show baiyu smile
    with Dissolve(0.25)

    baiyu "我们又会成为邻居了哦。"

    "就像小时候那样。"

    "我站在原地，看着她。"

    ## 收束 ####################################################################

    "窗外的雨还在下。"

    "玻璃上的水痕，像是一张模糊的脸。"

    heart "很奇怪。我明明不记得她，却觉得她早就该在这里了。"

    heart "像是这间屋子，本来就留着她的位置。"

    pause 0.6

    play sound audio.thunder

    show white_flash at flash_anim

    pause 0.10

    hide baiyu

    pause 0.22

    hide white_flash

    "一道闪电划过——"

    scene bg room night at pull_back
    with Dissolve(0.8)

    "房间里，只剩下一个人的身影。"

    pause 1.0

    scene black
    with Dissolve(2.4)

    stop amb fadeout 2.0
    stop rain fadeout 3.0

    "雨还在下。"

    pause 0.8

    call screen end_card

    return
