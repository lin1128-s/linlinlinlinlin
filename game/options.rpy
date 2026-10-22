################################################################################
## 《白雨》· 项目配置
################################################################################

## 游戏基本信息 ################################################################

define config.name = _("白雨")
define gui.show_name = True
define config.version = "0.1.0"
define gui.about = _("第一章 · 雨季\n\n改编自同名章节剧本。\n\n本作使用 Ren'Py 制作。")

define build.name = "BaiYu"
define build.directory_name = "BaiYu-0.1.0"
define build.executable_name = "BaiYu"

## 存档目录（跨设备唯一） ####################################################

define config.save_directory = "baiyu-20261022"

## 窗口与图标 ##################################################################

define config.window_icon = "gui/window_icon.png"
define config.window_title = "白雨"

## 界面语言（使用 Ren'Py 自带中文 UI 翻译）
define config.language = "schinese"

## 声音与字幕 ##################################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = "audio/bgm.wav"

## 默认偏好 ####################################################################

default preferences.text_cps = 34
default preferences.afm_time = 15
default preferences.afm_enable = False

## 回滚与历史 ##################################################################

define config.rollback_enabled = True
define config.hard_rollback_limit = 128

## 开发与构建 ##################################################################

define config.developer = "auto"
define config.console = False

init python:

    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.png", "archive")
    build.classify("game/**.jpg", "archive")
    build.classify("game/**.wav", "archive")
    build.classify("game/**.ttf", "archive")

    build.classify("build/**", None)
    build.classify("dist/**", None)
    build.classify("src/**", None)
    build.classify("ref-*", None)
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)

    build.documentation("README.md")
