# LXGW WenKai / 霞鹜文楷
An open-source Chinese font derived from Fontworks' Klee One. 一款基于 FONTWORKS 的 Klee One 的开源中文字体。  

[![开源授权](https://img.shields.io/github/license/lxgw/LxgwWenKai)](https://github.com/lxgw/LxgwWenKai)
[![最新版](https://img.shields.io/github/release/lxgw/LxgwWenKai)](https://github.com/lxgw/LxgwWenKai/releases)

## 项目简介

2020 年 12 月，日本著名字体厂商 FONTWORKS 在 GitHub 上释出了 [7 款开源日文字体](https://github.com/fontworks-fonts)，分别为 **Train、Klee、Stick、Rock-n-Roll、Reggae、Rampart 和 DotGothic16。** 7 款开源日文字体各有各的特点，而这七款字体中，字符数量最多的是 [Klee](https://github.com/fontworks-fonts/Klee)。

这是一款有着日本教科书体的写法的字体，兼有仿宋和楷体的特点，可读性高。一些 DIY 字体爱好者曾先后用**仿宋、刻本仿宋、仓耳今楷**补全这款字体，做为手机系统的美化字体移稙在 iOS、Android 等手机系统中，受到很多机友的欢迎。不过这样补全的字体有一些不足之处。 **第一**，原有字体和后补字体之间有着一定的差异，致使一些不同的文字（如 Klee 原有汉字与后补简体字）混排之后会有违和感。 **第二**，由于补字所用的字体（如刻本仿宋、仓耳今楷等）为商业版权字体，补全之后不可用于商业用途，还会有侵权的风险。此外，目前现有的开源中文字库里，楷体类寥寥无几，仿宋类则几乎没有。

鉴于此，也为了丰富开源中文字体中的楷体门类，本人开始了为 Klee 这一高质量的日文字体补全简繁常用字的尝试。补全后的字体拟命名 **「霞鹜文楷」**。选取原字体 SemiBold 字重做为 Regular 字重。

有关补字的更多信息，请参阅本人博客里的文章：[《为 Klee 试制简化字》](https://lxgw.github.io/2021/01/28/Klee-Simpchin/)

## 字体预览

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/image/wenkai-1.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/image/wenkai-2.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/image/wenkai-3.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/image/wenkai-4.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/image/wenkai-5.png)

![](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/image/wenkai-6.png)

## 补字计划与历史纪录

[查看 2 月 27 日前的历史纪录。](https://github.com/lxgw/LxgwWenKai/blob/main/History.md)

2 月 27 日及以后的历史纪录将不再写入 History.md，请在 [Release](https://github.com/lxgw/LxgwWenKai/releases) 页面查看。

### 简体部分

- [x] 补完原字库所含繁体字对应的简化字；
- [x] 补完简体中文 3603 常用汉字 <sup>①</sup>;
- [x] 补完「信息交换用汉字编码字符集（GB 2312-80）」 6763 个汉字；
- [x] 补完「通用规范汉字表」8105 个汉字；
- [ ] 修改及优化字形 *（范围为 GB 2312 及通用规范汉字表）*。目前修改字形的任务已基本完成，但仍有一些字形待优化。

**<sup>①</sup>** 包括「现代汉语常用字表」（老 3500 字）及「义务教育语文课程常用字表」（新 3500 字，《通用规范汉字表》一级字表），新老 3500 加一起共 3603 字。

### 繁体部分 

- [x] 补完繁体中文 4808 常用汉字 *（台湾地区「常用国字标准字体表」）* ；
- [x] 补完「GB/T 12345-90」6866 个汉字；
- [x] 补完 BIG5 一级（常用）汉字 5401 个；
- [x] 补完「通用规范汉字表」内汉字对应的繁体字或港台异体字；
- 补完常用粤语、闽南语、客家语用字。*（基于 [「常用香港外字表」](https://github.com/ichitenfont/suppchara)）*
  - [x] 常用香港外字表 A-C 级
  - [x] 常用香港外字表 1-2 级
  - [x] 常用香港外字表 3 级
  - [x] 台湾闽客汉字（外字表ㄅ级）

## 下载字体

1. 进入 [Release](https://github.com/lxgw/LxgwWenKai/releases) 界面下载对应版本的 TTF 格式文件。以后 TTF 文件仅在 Release 页面更新。
3. 进入 [猫啃网](https://www.maoken.com/freefonts/9704.html) 进行下载。GitHub 项目更新后，会联系猫啃网站长进行同步更新。 **注意：** 其它收录免费商用字体的网站上可能也收录了本字体，但可能不是最新版。
3. 本仓库 FCP 文件夹内为增补字的 Font Creator 工程文件，包含 **部分** 笔画分离的字形，可用 Font Creator 打开查看。

## 注意事项

1. 本字体仍处于测试版，为单字重字体，部分汉字还是处于日本写法，且字库并不是很全。 
2. 本人并不是专业的设计师，并未考虑设计美感，所以看起来可能略丑，补进去的字与原版可能略有违和感；此外由于时间仓促，并没有多余的时间细修，部分字的部件拼接会很生硬。但聊胜于无。欢迎大家通过 Issues 反馈。

## 协助完善

欢迎更多志同道合的朋友在此基础上继续让这款字体更臻完善，您可以通过以下方式与本人联系。

- **Telegram：** @lxgwtg
- **微信公众号：** 霞鹜 *（ID: lxgwshare）*
- **酷安：** [@落霞孤鹜lxgw](https://www.coolapk.com/u/633884)
- **微博：** [@孤鹜先森](https://weibo.com/6624339726)
- **Email：** calxgw2018@gmail.com srtong2006@126.com lxgw1999@qq.com

## 授权信息

本字体是基于 SIL Open Font License 1.1 改造的 FONTWORKS 开发并发布的 [Klee](https://github.com/fontworks-fonts/Klee) 开源项目。Klee 是 FONTWORKS 的商标。

### 许可

- 这款字体无论是个人还是企业都可以自由商用，无需付费，也无需知会或者标明原作者。 *（但如果告知，我会很感激。）*
- 这款字体可以自由传播、分享，或者将字体安装于系统、软件或APP中也是允许的，可以与任何软件捆绑再分发以及／或一并销售。
- 这款字体可以自由修改、改造，制作衍生字体。修改或改造后的字体也必须同样以 [SIL OFL](https://scripts.sil.org/OFL) 公开。

### 限制

- 在制作衍生字体时，字体名称不可使用原有字体的「保留名称」。
- 这款字体不能用于违法行为，如因使用这款字体产生纠纷或法律诉讼，作者不承担任何责任。
- 根据 [SIL Open Font License 1.1](https://scripts.sil.org/OFL) 的规定， **禁止单独出售字体文件(OTF/TTF文件)的行为。**

## 鸣谢

- [FONTWORKS 株式会社](http://fontworks.co.jp) 提供原版开源字体； [开发者 GitHub 主页](https://github.com/fontworks-fonts/)
- 部分汉字结构参考 [仓耳今楷](http://tsanger.cn/product) 字体；
- [@CL-Jeremy](https://github.com/CL-Jeremy)、[@夜煞之乐](https://github.com/NightFurySL2001) 为字形设计提供指导；
- [@北辰極致卑微](https://weibo.com/u/5327681980?) 协助补全字体。

## 使用本字体的实例

- [「BV1qV41147tu」木鱼水心X《觉醒年代》主创：终于等到你！独家披露创作细节](https://www.bilibili.com/video/BV1qV41147tu)

## 其它项目

### 日系字体中文化

- [霞鹜晰黑 / Lxgw Clear Gothic](https://github.com/lxgw/LxgwClearGothic)
- [霞鹜新晰黑 / Lxgw New Clear Gothic](https://github.com/lxgw/LxgwNewClearGothic)
- [霞鹜漫黑 / Lxgw Marker Gothic](https://github.com/lxgw/LxgwMarkerGothic)
- [小赖字体 / Xiaolai](https://github.com/lxgw/kose-font)
- [悠哉字体 / Yozai](https://github.com/lxgw/yozai-font)

### 975 系列

- [975 圆体 / 975 Maru](https://github.com/lxgw/975maru)
- [975 黑体 / 975 Gothic](https://github.com/lxgw/975gothic)

## 打赏支持
[点击进入打赏页面。](https://github.com/lxgw/lxgw/blob/main/Donate.md)
