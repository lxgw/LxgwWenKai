
目前源文件版本： **1.234.56**

请运行 `build.bat` 以制作字体。需要安装 [`fontmake`](https://github.com/googlefonts/fontmake)：`pip3 install fontmake` 和 [`fontTools`](https://github.com/fonttools/fonttools)：`pip3 install fonttools`。

目前源文件使用 [UFO 3 ZIP 格式（`.ufoz`）](https://unifiedfontobject.org/versions/ufo3/)，碍于 `fontmake` 暂不支援 `.ufoz` 格式，因此运行 `extract_ufoz.py` 解压缩后使用其 `.ufo` 文件夹制作字体。

`fix_mono.py` 是特别用于修改等宽字符版本（Mono），使其西文与汉字可以以 1:2 比例对应。