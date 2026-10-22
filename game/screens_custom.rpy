################################################################################
## 自定义界面：题词、章节卡、便签、结束卡
################################################################################

## 样式 ########################################################################

style poem_line is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 40
    color "#d3dfea"
    text_align 0.5
    xalign 0.5
    line_spacing 8

style poem_credit is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 24
    color "#6d7f93"
    xalign 1.0

style poem_hint is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 20
    color "#46525f"

style cc_kicker is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 22
    color "#70839a"
    kerning 8
    xalign 0.5

style cc_title is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 76
    color "#e9f1fa"
    kerning 14
    xalign 0.5

style cc_sub is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 24
    color "#8b9db1"
    kerning 3
    xalign 0.5

style end_kicker is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 24
    color "#6f8196"
    kerning 10
    xalign 0.5

style end_title is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 96
    color "#e9f1fa"
    xalign 0.5

style end_line is default:
    font "fonts/NotoSansSC-VF.ttf"
    size 28
    color "#93a5b9"
    xalign 0.5

## 题词页 ######################################################################

screen poem_card(lines):

    modal True
    zorder 100

    add Solid("#05070a")

    button:
        xysize (1920, 1080)
        background None
        action Return()

    vbox:
        align (0.5, 0.42)
        spacing 18

        for line in lines:
            text line style "poem_line"

        null height 20

        text "—— 郑愁予《错误》" style "poem_credit"

    text "点击任意处继续" style "poem_hint" xalign 0.5 yalign 0.94

    key "dismiss" action Return()
    timer 18.0 action Return()

## 章节卡 ######################################################################

screen chapter_card(kicker, title, sub):

    modal True
    zorder 100

    add Solid("#05070a")

    button:
        xysize (1920, 1080)
        background None
        action Return()

    vbox:
        align (0.5, 0.45)
        spacing 18

        text kicker style "cc_kicker"
        text title style "cc_title"
        add Solid("#3d4c5e", xysize=(240, 1)) xalign 0.5
        text sub style "cc_sub"

    key "dismiss" action Return()
    timer 3.6 action Return()

## 便利贴 ######################################################################

screen note_card():

    modal True
    zorder 90

    add Solid("#00000066")
    add "images/fx/note.png" at note_pop

    button:
        xysize (1920, 1080)
        background None
        action Return()

    text "点击任意处继续" style "poem_hint" xalign 0.5 yalign 0.93

    key "dismiss" action Return()
    timer 12.0 action Return()

## 结束卡 ######################################################################

screen end_card():

    modal True
    zorder 110

    add Solid("#05070a")

    button:
        xysize (1920, 1080)
        background None
        action Return()

    vbox:
        align (0.5, 0.44)
        spacing 14

        text "第一章" style "end_kicker"
        text "完" style "end_title"

        null height 26

        text "雨还在下。" style "end_line"

    text "点击任意处返回标题" style "poem_hint" xalign 0.5 yalign 0.92

    key "dismiss" action Return()
