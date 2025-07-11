rm -r sources/temp
rm -r sources/build
mkdir -p sources/temp
mkdir -p sources/build
# unzip
python3 sources/shared/scripts/extract.py sources/shared/lite lite
python3 sources/shared/scripts/extract.py sources/shared/fulldiff fulldiff
# standard full
ufomerge --output sources/build/LXGWWenKai-Light.ufo --skip-existing --ignore-layout sources/temp/lite/Light.ufo sources/temp/fulldiff/Light.ufo
ufomerge --output sources/build/LXGWWenKai-Regular.ufo --skip-existing --ignore-layout sources/temp/lite/Regular.ufo sources/temp/fulldiff/Regular.ufo
ufomerge --output sources/build/LXGWWenKai-Medium.ufo --skip-existing --ignore-layout sources/temp/lite/Medium.ufo sources/temp/fulldiff/Medium.ufo
# mono fulll
ufomerge --output sources/build/LXGWWenKaiMono-Light.ufo --skip-existing --ignore-layout sources/shared/monolgc/Light.ufo sources/build/LXGWWenKai-Light.ufo
ufomerge --output sources/build/LXGWWenKaiMono-Regular.ufo --skip-existing --ignore-layout sources/shared/monolgc/Regular.ufo sources/build/LXGWWenKai-Regular.ufo
ufomerge --output sources/build/LXGWWenKaiMono-Medium.ufo --skip-existing --ignore-layout sources/shared/monolgc/Medium.ufo sources/build/LXGWWenKai-Medium.ufo
# fontinfo override
cp sources/fontinfo/LXGWWenKai-Light.plist sources/build/LXGWWenKai-Light.ufo/fontinfo.plist
cp sources/fontinfo/LXGWWenKai-Regular.plist sources/build/LXGWWenKai-Regular.ufo/fontinfo.plist
cp sources/fontinfo/LXGWWenKai-Medium.plist sources/build/LXGWWenKai-Medium.ufo/fontinfo.plist
cp sources/fontinfo/LXGWWenKaiMono-Light.plist sources/build/LXGWWenKaiMono-Light.ufo/fontinfo.plist
cp sources/fontinfo/LXGWWenKaiMono-Regular.plist sources/build/LXGWWenKaiMono-Regular.ufo/fontinfo.plist
cp sources/fontinfo/LXGWWenKaiMono-Medium.plist sources/build/LXGWWenKaiMono-Medium.ufo/fontinfo.plist
# feature override
cp sources/shared/lite/features.fea sources/build/LXGWWenKai-Light.ufo/features.fea
cp sources/shared/lite/features.fea sources/build/LXGWWenKai-Regular.ufo/features.fea
cp sources/shared/lite/features.fea sources/build/LXGWWenKai-Medium.ufo/features.fea
cp sources/shared/lite/features.fea sources/build/LXGWWenKaiMono-Light.ufo/features.fea
cp sources/shared/lite/features.fea sources/build/LXGWWenKaiMono-Regular.ufo/features.fea
cp sources/shared/lite/features.fea sources/build/LXGWWenKaiMono-Medium.ufo/features.fea