> [!IMPORTANT]
>
> - ~~添字请在 [Issue #33](https://github.com/lxgw/LxgwWenKai/issues/33) 反馈~~，字形调整请在 [Issue #14](https://github.com/lxgw/LxgwWenKai/issues/14) 反馈，不要另开议题，以便于整理。**由于字体文件越发臃肿，v1.330 更新发布后，加字反馈通道暂时关闭，不会接受用户加字请求，敬请谅解。**
> - 若需要在网站上使用这款字体，请参阅 [Issue #24](https://github.com/lxgw/LxgwWenKai/issues/24)，或者在 [ZSFT](https://fonts.zeoseven.com/designer/s/2/) 查找「霞鹜文楷」系列字体。
> - 有关 Magisk 字体模块等手机字体替换有关的问题，请移步[模块模板](https://github.com/lxgw/advanced-cjk-font-magisk-module-template)的 Issues 里反馈，不要在本项目开议题。
> - 更多版本 *（可能会随时变动）* ：
>   - [霞鹜文楷屏幕阅读版 / LXGW WenKai Screen](https://github.com/lxgw/LxgwWenKai-Screen)：适用于部分 Android 手机免 ROOT 更换第三方字体。
>   - [霞鹜文楷 轻便版 / LXGW WenKai Lite](https://github.com/lxgw/LxgwWenKai-Lite)：与完整版相比剔除一些较不常用的字符，便于开发者将字体嵌入软件中。
>   - [霞鹜文楷 GB / LXGW WenKai GB](https://github.com/lxgw/LxgwWenkaiGB)：进一步调整字形和笔形，符合 G 源字形规范。[轻便版](https://github.com/lxgw/LxgwWenKaiGB-Lite)
>   - [霞鹜文楷 TC / LXGW WenKai TC](https://github.com/lxgw/LxgwWenkaiTC)：旧字形版参考「一点字坊」的「传承字形标准化文件」对部件进行修改，适用于繁体中文用户及旧字形爱好者。
>   - 与其他西文字体合并的字体：[LXGW Bright](https://github.com/lxgw/LxgwBright)（与 [Ysabeau Office](https://github.com/CatharsisFonts/Ysabeau) 搭配）、[LXGW Bright Code](https://github.com/lxgw/LxgwBright-Code)（与 [Monaspace Argon](https://github.com/githubnext/monaspace) 搭配）。

# LXGW WenKai / 霞鹜文楷

An open-source Chinese font derived from Fontworks' Klee One. 一款开源中文字体，基于 FONTWORKS 出品字体 Klee One 衍生。  

[![开源授权](https://img.shields.io/github/license/lxgw/LxgwWenKai?style=flat-square)](https://github.com/lxgw/LxgwWenKai)
[![最新版](https://img.shields.io/github/release/lxgw/LxgwWenKai?style=flat-square)](https://github.com/lxgw/LxgwWenKai/releases/latest)
[![猫啃网](https://shields.io/badge/%E7%8C%AB%E5%95%83%E7%BD%91-fe5e52?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACEAAAAfCAMAAABeSlSAAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAHyUExURQAAAAAA//8AAAAA//8AAAAA/wAA//8AAAAA//8AAAAA//8A//8AAAAA//8AAAAA//8AAAAA/wD///8AAAD/////AAD/////AP//AP//////AAD/////AAD/////AP///wD/////AP//AP//////AP//////AP///wD//////wD//wD/////////AP///wD//wD//wD/////AP///////////wD/////AP///wD///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f////39/f39/f39/f39/f39/f7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v////7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v////7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v///y6UHskAAACldFJOUwADAwQEBQYGBwcICAkLCwwMDQ0NDhESEhMWFxgYGRkbHBwdHR8hIyQlJygpKSwsLS4yMjQ1Njc3ODk6PD5BQkNFRkdNUFFTVldaXF1fYGdqbnBxcnZ4eXt8gIGEhYaJio6RkpWXmJqbnJ2goqOlpqirrrCxs7S1trm7vr/BwsTHyMvMzc/Q0tPU2Nrb3N3f4uTm5+jp6+zt7vDx8vP19vf4+/z9/iyQxCoAAAAJcEhZcwAAFxEAABcRAcom8z8AAAHPSURBVDhPvZDpOxtRFIdvCJ1olaCLoqW1BF1U2tpJSlpFiK17NNE1DbGVoFVL20TRoMFUDDKS83+6Z+6tJjx9Hp+8X+b+fued88xcckLcmnl9nR8PkfVizoDPewHYcRYqVRQZr0TYfYinii0A2LReVOoDEiwrtN5txPNtMTj2B8BTH6OMGHc/A0huaduEoXg52FwwIEPY+7a1+opalV5uts/KEPp0s07aqkIj2wMv1XHmDbo0AqlTQ9rklRtoJI3DWLJ+MsxHf5mtFT7A98toCG/A9/jQBkR6/gNGzqJBLHu8O4pVrRgGiecjBJsUgeiWWPYNOtwBWk99dHlZs17KDO24Ep3nVHdMlV7ffaNRI/SEsPLkMENwYApUkUfb0K/XW0N7XTElv7GbSGZGghOTWBpno29dpT8PfWd0vxQjlRmJw8yItwPM52onAPq5MX3huIbw/n8GvzBC75+mzbJIo3iZVuFn7MIIKcIX5I7TEUZLkFb+ci6Q2G5cstrQC7CQf/4rgKtmEVfYNFwgJO0dXpAs0vbLKLXFHRrBfYmPkZQe3BpFyJXJhwxV/Tc+4fw0n+KjA+Ibhvx8CmvDjf8+IYprJsuTp+0P8ng8OQjZB5l3H1123DZyAAAAAElFTkSuQmCC)](https://www.maoken.com/freefonts/9704.html)

## 项目简介

2020 年 12 月，日本著名字体厂商 FONTWORKS 在 GitHub 上发布了 [7 款日文字体](https://github.com/fontworks-fonts)，分别为 **Train、Klee、Stick、Rock-n-Roll、Reggae、Rampart 和 DotGothic16**，根据 SIL Open Font License 1.1 授权许可开源。7 款开源日文字体各有各的特点，而这 7 款字体中，字符数量最多的是 [Klee](https://github.com/fontworks-fonts/Klee)。

这是一款有着日本教科书体风格的字体，兼有仿宋和楷体的特点。一些 DIY 字体爱好者曾先后用仿宋等字体补全这款字体，作为手机系统的美化字体移植在 iOS、Android 等手机系统中，受到很多玩机发烧友的欢迎。不过这样补全的字体有一些不足之处。 **第一**，原有字体和后补字体之间有着一定的差异，致使一些不同的文字（如 Klee 原有汉字与后补简体字）混排之后会有一定的违和感。 **第二**，由于补字所用的字体为商业版权字体，补全之后不可用于商业用途，还会有侵权的风险。此外，目前现有的开源中文字库里，楷体类寥寥无几，仿宋类则几乎没有。

鉴于此，也为了丰富开源中文字体中的楷体门类，2021 年 1 月 20 日起，本人开始了为 Klee One 这一高质量的日文开源字体补全简繁常用字的尝试。因该字体具有一定的「文艺气息」，命名 **「霞鹜文楷」***（其实当初是感觉这款字体适合正文阅读定名「文楷」，后来发现这款字体可能并不太适合大段正文排版，相比之下更加适合诗词之类的中等长度文本排版，或者注释排版）*。由于 Klee One 字体的 Regular 字重太细不太适合阅读，选取原字体 SemiBold 字重作为 Regular 字重。经过长时间的积累，目前已发展成简繁日韩均支持的 3 字重字体家族 ~~（虽然拙劣粗糙了点）~~ 。

有关补字过程的更多信息，请参阅本人 GitHub.io 博客里的文章：[《为 Klee 试制简化字》](https://lxgw.github.io/2021/01/28/Klee-Simpchin/)。

「霞鹜文楷」支持 Unicode 变体序列（Unicode Variation Sequences, UVS），用于蝌蚪引号`“‘’”`宽度的选择，[点击此处查看一览表](documentation/uvs.pdf)。

## 字体预览

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-1.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-2.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-3.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-4.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-5.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-6.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-7.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-8.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/documentation/wenkai-9.png)

<!-- [查看详细更新记录。](https://github.com/lxgw/LxgwWenKai/blob/main/History.md) -->
历史版本的 Release，请在 [Release](https://github.com/lxgw/LxgwWenKai/releases) 页面查看。文字版本的更新记录 `HISTORY.MD` 不再维护，敬请谅解。

## 字汇

### 主要汉字部分

请参阅[「霞鹜文楷 轻便版」加字计划](https://github.com/lxgw/LxgwWenKai-Lite#%E5%8A%A0%E5%AD%97%E8%AE%A1%E5%88%92)。

### 其他部分

- [x] 补完 CJK 统一汉字基本区 20992 个汉字、扩展 A 区 6592 个汉字 *（目前完整版有 1 万多个字形由 zi2zi 深度学习生成，字形较粗糙。）* ；
- [x] 补全常用谚文（韩语/朝鲜语）音节 2376 个。 *（做得比较拙劣。轻便版不包含。）*

<!-- [点击此处查看后续加字及调整计划。](https://github.com/lxgw/LxgwWenKai/projects) -->

## 获取字体

### ⅰ. 直接下载

1. 进入 [Release](https://github.com/lxgw/LxgwWenKai/releases) 界面下载对应版本的 TTF 格式文件，或在本仓库 `fonts/TTF` 文件夹中下载。
2. 在 [Gitee 官方镜像仓库](https://gitee.com/mirrors/lxgw-wenkai) `fonts/TTF` 文件夹中下载。
3. 进入 [猫啃网](https://www.maoken.com/freefonts/9704.html)、[Zfont.cn](https://zfont.cn/cn/font_286.html)、[自由字体](https://ziyouziti.com/mianfeiziti-302.html) 进行下载。GitHub 项目更新后，会联系站长进行更新，更新会稍晚些。 **注意：** 其它收录免费商用字体的网站上可能也收录了本字体，但可能不是最新版。 
4. [永硕Ｅ盘](http://lxgw.ysepan.com/)、[蓝奏云（密码：8ppk）](https://lxgw.lanzoui.com/b0cqwpt3i) 会在 GitHub 项目更新后 72 小时之内更新。
5. 如果您使用 macOS，已经安装过 [Homebrew](https://brew.sh/)，可以在终端输入命令：`brew install font-lxgw-wenkai` 来安装本字体。
6. 如果您使用 Windows，已经安装过 [Scoop](https://scoop.sh/)，可以在终端输入命令：`scoop bucket add nerd-fonts && scoop install LXGWWenKai` 或者 `scoop bucket add nerd-fonts && scoop install LXGWWenKaiMono` 来安装本字体。亦可查看微软官方教程：[如何在 Windows 中安装或删除字体](https://support.microsoft.com/zh-cn/windows/如何在-windows-中安装或删除字体-f12d0657-2fc8-7613-c76f-88d043b334b8)。

### ⅱ. 从源代码生成

请运行 `./sources/build.bat` 或 `./sources/build.sh`。需要安装 [`fontmake`](https://github.com/googlefonts/fontmake)：`pip3 install fontmake` 和 [`fontTools`](https://github.com/fonttools/fonttools)：`pip3 install fonttools`。

## 注意事项

1. 截至目前，完整版本字体含有全部 CJK 基本区和扩展 A 区汉字，以及零星扩展 B~I 区汉字。 ~~**如有补字需求，请在 [Issue #33](https://github.com/lxgw/LxgwWenKai/issues/33) 提出，不要另开 Issue**，以便于整理。~~ **由于字体文件越发臃肿，v1.330 更新发布后，加字反馈通道暂时关闭，不会接受用户加字请求，敬请谅解。**
2. 本人并不是专业的设计师，并未考虑设计美感，所以看起来可能略丑，补进去的字与原版可能略有违和感，且在 Medium 字重中部分字的轮廓曲线会有毛刺，Light 字重中部分字的轮廓会存在飞点；此外由于时间仓促，并没有多余的时间细修，部分字的部件拼接会很生硬。**如有字形优化建议，请在 [Issue #14](https://github.com/lxgw/LxgwWenKai/issues/14) 提出，不要另开 Issue**，以便于整理。 *（以上两个 issue 均已加上 long term 标签，且均已在 Issues 页面置顶。）*
3. **若需要在网站上使用这款字体，请参阅 [Issue #24](https://github.com/lxgw/LxgwWenKai/issues/24)，或者在 [ZSFT](https://fonts.zeoseven.com/designer/s/2/) 查找「霞鹜文楷」系列字体。**
4. 对于搭配的西文字体，个人推荐 [Ysabeau](https://github.com/CatharsisFonts/Ysabeau) 系列字体。另有 Ysabeau Office 与霞鹜文楷轻便版的合并字体 [LXGW Bright](https://github.com/lxgw/LxgwBright)，采用 [字体合并补全工具](https://github.com/nowar-fonts/Warcraft-Font-Merger) 将两款字体合并而成。亦有中英文合并的等宽字体 [LXGW Bright Code](https://github.com/lxgw/LxgwBright-Code)，采用 [Monaspace Argon](https://github.com/githubnext/monaspace) 经缩窄调整后与霞鹜文楷轻便版合并而成。
5. 该字体的更多版本 *（可能会随时变动）*
   1. [霞鹜文楷屏幕阅读版 / LXGW WenKai Screen](https://github.com/lxgw/LxgwWenKai-Screen)：以 Medium 字重为基准，调整度量数据与 Android 默认西文字体 Roboto 一致，适用于部分 Android 手机免 ROOT 更换第三方字体。
   2. [霞鹜文楷 轻便版 / LXGW WenKai Lite](https://github.com/lxgw/LxgwWenKai-Lite)：剔除谚文及较不常用的汉字，便于开发者将字体嵌入软件中。若完整版有字形优化或特性更新，精简版也将会跟进。
   3. [霞鹜文楷 GB / LXGW WenKai GB](https://github.com/lxgw/LxgwWenkaiGB)：在文楷基础上进一步调整字形和笔形，符合 G 源字形规范。包含 GB 18030-2022 实现级别 2 范围内所有汉字。另有[文楷 GB 轻便版](https://github.com/lxgw/LxgwWenkaiGB-Lite)。
   4. [霞鹜文楷 TC / LXGW WenKai TC](https://github.com/lxgw/LxgwWenkaiTC)：供繁体中文用户和旧字形爱好者使用，基于轻便版制作，采用旧字形写法，主要采用 Klee One 的隐藏字形，部分部件手动修改 （大部分部件参考[一点字坊「传承字形标准化文件」](https://github.com/ichitenfont/inheritedglyphs)，借助[「汉文博士」](https://www.cnblogs.com/hanbox/)[「国学迷」](http://www.guoxuemi.com/zidian/bujian/)[「字统网」](http://zi.tools) 等工具按部件查字，对字形进行修改）。此外已有基于 Klee One 改造的繁体中文字体 [芫荽 / Iansui](https://github.com/ButTaiwan/iansui)，采用台湾地区的教育标准字形；另有采用香港地区字形标准的 [芫茜雅楷 / JyunsaiKaai](https://github.com/ItMarki/jyunsaikaai)。
6. **本项目为字体项目，有关 Magisk 字体模块等手机字体替换有关的问题，请移步[模块模板](https://github.com/lxgw/advanced-cjk-font-magisk-module-template)的 Issues 里反馈，不要在本项目开议题。**

## 协助完善

霞鹜文楷仍是一款完成度不算高的字体，诸多地方仍然存在瑕疵。欢迎更多志同道合的朋友在此基础上完善这款字体，您可以通过以下方式与本人联系。

- **Telegram：** [@lxgwtg](https://t.me/lxgwtg) | [频道](https://t.me/lxgwfont)
- **微信公众号：** 霞鹜 *（ID: lxgwshare）*
- **[即刻](https://m.okjike.com/users/2e826735-48e6-46c5-b0c2-278cb1853b54?ref=PROFILE_CARD&source=user_card&s=eyJ1IjoiNWVlMzkwZGRkNWNhNTgwMDE3NjljZjFiIiwiZCI6MX0%3D&utm_source=create_card)、[少数派](https://sspai.com/u/ng008g7q)、[小红书](https://www.xiaohongshu.com/user/profile/64770ed70000000012035f3b)、[站酷](https://www.zcool.com.cn/u/26715019)、[~~酷安~~](https://www.coolapk.com/u/633884)：** @落霞孤鹜lxgw
- **微博：** [@孤鹜先森](https://weibo.com/6624339726)
- **哔哩哔哩：** [@霞鹜lxgw](https://space.bilibili.com/3461565661579301)
- **Email：** calxgw2018@gmail.com srtong2006@126.com lxgw1999@qq.com

## 授权信息

本字体是基于 SIL Open Font License 1.1 改造的 FONTWORKS 开发并发布的 [Klee](https://github.com/fontworks-fonts/Klee) 开源项目。Klee 是 FONTWORKS 的商标。

> [猫啃网](https://www.maoken.com/)提供 SIL Open Font License 1.1 非官方[简体中文译本](https://www.maoken.com/ofl)便于理解，仅供参考。

### 许可

- 这款字体无论是个人还是企业都可以自由商用，无需付费，也无需知会或者标明原作者。 *（但如果告知，我会很感激。）*
- 这款字体可以自由传播、分享，或者将字体安装于系统、软件或APP中也是允许的，可以与任何软件捆绑再分发以及／或一并销售。
- 这款字体可以自由修改、改造，制作衍生字体。修改或改造后的字体也必须同样以 [SIL OFL](https://openfontlicense.org) 公开。

### 限制

- 在制作衍生字体时，字体名称不可使用原有字体的「保留名称」。本字体保留名称「霞鹜」「LXGW」，基于本字体二次衍生的字体，名称不可出现「霞鹜」或「LXGW」字样；而在没有对字体源代码进行修改的情况下，重新编译出来的字体，可以继续使用本字体的保留名称「霞鹜」「LXGW」。
- 根据 [SIL Open Font License 1.1](https://openfontlicense.org)「许可与条件」中第 1 条的规定， **禁止单独出售字体文件(OTF/TTF文件)的行为。**
- 该字体不可在 [SIL Open Font License 1.1](https://openfontlicense.org) 以外的授权许可下发行。

## 鸣谢

- [FONTWORKS 株式会社](http://fontworks.co.jp) 提供原始开源字体； [开发者 GitHub 主页](https://github.com/fontworks-fonts/)
- 原始字体的设计师周建豪（Francis Chow）先生，以及 [@CL-Jeremy](https://github.com/CL-Jeremy)、[@夜煞之乐](https://github.com/NightFurySL2001) 等为字形设计提供指导；
- [@夜煞之乐](https://github.com/NightFurySL2001) 等为本项目的运营提供帮助；
- [@北辰極致卑微](https://weibo.com/u/5327681980?)、[@Georgome](https://github.com/GeorgomeFont)、[@Magmeta](https://github.com/Des-Magmeta)、[@Steve-Yuu](https://github.com/Steve-Yuu) 等协助完善字体；
- [Iosevka](https://github.com/be5invis/Iosevka) / [Nerd-Fonts](https://github.com/ryanoasis/nerd-fonts) 提供等宽字体所用的 Powerline 符号；
- [zi2zi_pytorch](https://github.com/EuphoriaYan/zi2zi-pytorch) 以及深度学习生成字形的源头字体 [思源宋体](https://github.com/adobe-fonts/source-han-serif)；
- 制表符、表意文字结构描述符（Ideographic Description Character, IDC）等字符借自 [思源黑体](https://github.com/adobe-fonts/source-han-sans)；
- 吉祥图案、CC 许可图标等字符衍生自 [煮豆黑体](https://github.com/Buernia/Zhudou-Sans)；
- 缺字标记 `.notdef` 的「🤔」外部轮廓取自 [Noto Emoji (Monochrome)](https://github.com/googlefonts/noto-emoji)。

## 由本字体衍生的字体

- [澳声通拼音文楷](https://github.com/jeffreyxuan/toneoz-font-pinyin-wenkai) (需配合 [选音编辑器](http://toneoz.com/ime) 使用)
- [计划楷 / PlanKai](https://github.com/Des-Magmeta/PlanKai)

## 更多「霞鹜」系列字体
### 「霞鹜文楷」系列
- **霞鹜文楷 / LXGW WenKai** | [Lite](https://github.com/lxgw/LxgwWenKai-Lite)
- [霞鹜文楷 GB / LXGW WenKai GB](https://github.com/lxgw/LxgwWenKaiGB) | [Lite](https://github.com/lxgw/LxgwWenKaiGB-Lite)
- [霞鹜文楷 TC / LXGW WenKai TC](https://github.com/lxgw/LxgwWenKaiTC)
### 「晰致尚铭」系列
- [霞鹜新晰黑 / LXGW Neo XiHei](https://github.com/lxgw/LxgwNeoXiHei)
- [霞鹜新致宋 / LXGW Neo ZhiSong](https://github.com/lxgw/LxgwNeoZhiSong)
- [霞鹜晰黑 / LXGW XiHei](https://github.com/lxgw/LxgwXiHei)
- [霞鹜致宋 / LXGW ZhiSong](https://github.com/lxgw/LxgwZhiSong)
- [霞鹜尚智黑 / LXGW Fasmart Gothic](https://github.com/lxgw/LxgwFasmartGothic) 停止维护
- [霞鹜铭心宋 / LXGW Heart Serif](https://github.com/lxgw/LxgwHeartSerif) 停止维护
### 其他
- [霞鹜漫黑 / LXGW Marker Gothic](https://github.com/lxgw/LxgwMarkerGothic)
- [霞鹜臻楷 / LXGW ZhenKai](https://github.com/lxgw/LxgwZhenKai) 停止维护
- [小赖字体 / Xiaolai](https://github.com/lxgw/kose-font)
- [悠哉字体 / Yozai](https://github.com/lxgw/yozai-font)
  
## 打赏支持

[点击进入打赏页面。](https://github.com/lxgw/lxgw/blob/main/Donate.md)


## Stargazers over time

[![Stargazers over time](https://starchart.cc/lxgw/LxgwWenKai.svg)](https://starchart.cc/lxgw/LxgwWenKai)

