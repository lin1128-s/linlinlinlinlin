# 白雨 · 第一章

一个用 Ren'Py 8.5.3 制作的中文视觉小说 Demo，改编自同名第一章剧本。

- 时长：约 12–15 分钟
- 分辨率：1920×1080
- 语言：简体中文
- 引擎：Ren'Py 8.5.3（Python 3.12）

## 启动

开发环境（需要本机装有 Ren'Py SDK）：

```
D:\renpy\renpy-8.5.3-sdk\renpy.exe C:\Users\Administrator\Desktop\game
```

打包版：解压 `dist/` 下的 zip，双击 `BaiYu.exe`。

## 操作

| 操作 | 按键 |
|---|---|
| 推进对话 | 鼠标左键 / 空格 / 回车 |
| 快进 | 按住 Ctrl |
| 自动播放 | 底部「自动」 |
| 菜单（存档/读档/设置） | 鼠标右键 / Esc |
| 全屏 | Alt+Enter 或设置内切换 |
| 截图 | S |

## 工程结构

```
game/
├─ game/
│  ├─ script.rpy          入口
│  ├─ chapter1.rpy        序幕 + 第二幕全部演出
│  ├─ characters.rpy      角色与旁白
│  ├─ images.rpy          图像定义、立绘站位、闪回/闪电/拉远
│  ├─ audio.rpy           音频别名与雨声/电视声道
│  ├─ screens_custom.rpy  题词页、章节卡、便签、结束卡
│  ├─ options.rpy         项目配置、构建配置
│  ├─ gui.rpy / screens.rpy  标准 UI（基于 Ren'Py 默认 GUI 改写）
│  ├─ images/bg/          3 张场景（1080p，已去水印）
│  ├─ images/sprite/      5 种表情立绘（透明通道）
│  ├─ images/fx/          雨滴、暗角、便签
│  ├─ audio/              10 个程序化音频
│  ├─ fonts/              Noto Sans SC
│  └─ tl/schinese/        中文 UI 翻译
├─ src/raw/               原始素材备份
├─ src/tools/             抠图 / 合成音频脚本
├─ build/shots/           关键帧截图
├─ PLAN.md                开发计划
└─ README.md
```

## 素材处理说明

- 3 张场景图原始为 2048×1152，统一裁切为 1920×1080，同时移除左下角「AI生成」水印。
- 5 张白底立绘（2 张 JPG、3 张 PNG）用边缘泛洪 + 羽化抠成透明通道，并按身高统一缩放；另 2 张原生透明立绘裁去空白。
- 三张几乎相同的微笑立绘保留 2 张作为微差分。
- 音频无现成素材，全部用 Python 标准库程序化合成：雨声两层、雷、敲门、开门、行李箱、电视闷响、心跳、闪白、氛围 BGM。均为占位音，可整包替换。
- 便利贴为程序绘制（纸张、胶带、手写体、兔头/猪头涂鸦），不依赖额外字体分发。

## 已实现 / 后续

已实现：题词页、章节卡、闪回暖色滤镜、便利贴插入、立绘表情切换、闪电隐去人物、结尾拉远、结束卡、存读档/回滚/快进/自动、中文 UI。

后续可做：补白雨「湿身 + 行李箱」登场差分、早餐/玩具熊等缺失 CG、真人配音、Web 版、字体子集化压缩包体。

## 版权

剧本与角色美术：项目作者所有。
字体：Noto Sans SC（SIL Open Font License）。
引擎：Ren'Py（MIT 等开源许可）。
