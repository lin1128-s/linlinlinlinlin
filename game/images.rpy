################################################################################
## 图像与变换
################################################################################

## 背景 ########################################################################

image bg room night = "images/bg/bg_room_night.jpg"
image bg room white = "images/bg/bg_room_white.jpg"
image bg corridor = "images/bg/bg_corridor.jpg"

## 立绘 ########################################################################
## 每张图按 1010px 的目标身高烘焙 zoom，保证切换表情时人物高度一致。

image baiyu smile:
    "images/sprite/baiyu_smile.png"
    zoom 0.6885

image baiyu smile soft:
    "images/sprite/baiyu_smile_soft.png"
    zoom 0.6619

image baiyu calm:
    "images/sprite/baiyu_calm.png"
    zoom 0.6632

image baiyu annoyed:
    "images/sprite/baiyu_annoyed.png"
    zoom 0.6658

image baiyu sad:
    "images/sprite/baiyu_sad.png"
    zoom 0.6640

image baiyu laugh:
    "images/sprite/baiyu_laugh.png"
    zoom 0.6662

## 特效 ########################################################################

image white_flash = Solid("#ffffff")
image vignette = "images/fx/vignette.png"
image note_paper = "images/fx/note.png"

image rain_near = SnowBlossom(
    Transform("images/fx/rain_drop.png", alpha=0.55),
    count=70, border=140, xspeed=(-45, 45), yspeed=(1500, 2200), start=0, fast=True)

image rain_far = SnowBlossom(
    Transform("images/fx/rain_drop.png", alpha=0.30, zoom=0.62),
    count=130, border=110, xspeed=(-25, 25), yspeed=(700, 1100), start=0, fast=True)

## 转场
define flash_white = Fade(0.06, 0.0, 0.22, color="#ffffff")
define cut_fast = Dissolve(0.10)

## 站位 / 表演 #################################################################

transform stand:
    xalign 0.5
    yalign 1.0

transform stand_right:
    xalign 0.62
    yalign 1.0

transform stand_close:
    xalign 0.5
    yalign 1.0
    zoom 1.06
    yoffset 30

## 让立绘轻轻呼吸
transform breathe:
    yoffset 0
    ease 3.2 yoffset -5
    ease 3.2 yoffset 0
    repeat

## 夜色压暗
transform night_light:
    matrixcolor BrightnessMatrix(-0.07) * TintMatrix("#c8d7e9")

## 暖色闪回
transform warm_light:
    matrixcolor TintMatrix("#ffd6a2") * SaturationMatrix(0.62) * BrightnessMatrix(-0.02)

transform warm_light_wide:
    matrixcolor TintMatrix("#ffd6a2") * SaturationMatrix(0.58) * BrightnessMatrix(0.04)

## 闪电 / 闪白
transform flash_anim:
    alpha 0.0
    linear 0.04 alpha 0.92
    linear 0.26 alpha 0.0

## 结尾拉远
transform pull_back:
    zoom 1.12
    linear 9.0 zoom 1.0

## 立绘入场
transform slide_in_left:
    xalign 0.5
    yalign 1.0
    xoffset -60
    alpha 0.0
    ease 0.45 xoffset 0 alpha 1.0

## 便签弹出
transform note_pop:
    align (0.5, 0.5)
    zoom 0.86
    alpha 0.0
    ease 0.35 zoom 0.9 alpha 1.0
