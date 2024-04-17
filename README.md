<!---
![AG项目图](https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/ef8ea90e-16a9-4882-8545-8fbceea39ca6)
--->
<!---
![artgallery新项目图](https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/e7f2fde4-d138-4f32-80d1-50cda798992a)
--->

# ComfyUI ArtGallery | Prompt Visualization
### 艺术画廊 | 提示词可视化 

https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/51fe3cfe-6b6c-41aa-b172-7ef564aefaa2


## 项目介绍 | Info

- **我正在尝试提示词可视化**：没有参考时，众多且陌生的选项反而会成为一种负担，因此可视化就是最佳选择（ Visualization Is All You Need！），似乎图像比文字更加适合选择！

- **艺术画廊系列**：提供艺术家、艺术运动、艺术媒介、相机镜头、胶片相机等5大类提示词参考图

- **提示词来源**：艺术家 [@Rikkar](https://github.com/rikkar69) 测试并整理了上千种适用于 SDXL 的不同类别的艺术提示词： [SDXL 1.0 Artistic Studies](https://rikkar69.github.io/SDXL-artist-study/)

- **参考图**：均由我使用 SDXL 1.0 模型完成

- **与传统方式对比**：
    | 对比                      | 传统                      | 可视化                       |
    |---------------------------|---------------------------|-----------------------------|
    | 方式                      | 直接输入/选择提示词         | 选择参考图，自动输出相应提示词 |
    | 参考                      | ❌                        | ✔️                          |
    | 判断方式                   | 先生成，后判断             | 预览+判断，再决定是否生成      |
    | 权重调节                   | 手动                      | 滑块选择                      |
    | 输出                      | 提示词：Picasso            | 提示词+权重：(Picasso:1.03)、参考图（可选）     |
    | 适合人群                   | 对艺术比较了解             | 艺术小白                      |

<!---
    🕗 传统：直接输入/选择提示词（如艺术家或风格），没有预览或参考，当面对众多选择或不熟悉的艺术家/风格时，往往无法确定其效果，只能通过生成之后再做出判断，十分不便。另外还需手动输入或调节权重。
    🆕 可视化：提供选择预览，不论是直接选择还是搜索，选好之后会自动出现对应的参考图，只需直接选择喜欢的图即可，节点会自动输出艺术家/风格等提示词给模型，同时还提供滑动选择权重，直观且方便
--->

- **版本**：V1.0


## 详细说明 | Features

- Artists | 艺术家：280位（从5000+中精选出来）

- Movements | 艺术运动：138种（去除了NSFW）

- Styles | 艺术媒介：115种

- Films | 胶片：83种

- Cameras | 镜头：47种

<!---
- 艺术家（280+）
- 艺术运动（130+）
- 艺术媒介（110+）
- 相机镜头（40+）
- 胶片相机（80+）
--->

![image](https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/7475e692-aba2-4201-a6c8-612217566925)


https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/efc9dc4b-bafd-4aa2-af00-dcd745932201


## 自定义 | Customizations

可将需要自定义增加的参考图内容放到 img_lists 中对应的文件夹里




## 安装 | Install

- 推荐使用 ComfyUI Manager 安装

- 手动安装：
    1. `cd custom_nodes`
    2. `git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery.git`
    3. 重启 ComfyUI
    4. 如果打开之后没显示预览图像，再次重启即可

## 工作流 | Workflow

### V1.0工作流

- [V1.0 For SD1.5 or SDXL](https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/blob/main/ArtGallery%20Workflows/ArtGallery%20V1.0%E3%80%90Zho%E3%80%91.json)

![ArtGallery](https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/bd3673b6-16b0-46ee-92ee-6b5ebf446bb5)



## 更新日志

- 20240104

  V1.0正式版，增加工作流和视频介绍

- 20240102

  全部更新为压缩后的图像，减小下载和加载压力

- 20231231

  自己的测试图库全部上传完成，并去除了 NSFW，更新项目封面图

- 20231230

  已全部替换为自己的测试图，并精选了280位艺术家，图像库暂时还未上传完

- 20231229
  
    完成 camera、film、movement、style 的全部测试，已替换为自己的图像

- 20231228
  
    创建项目


## 关于我 | About me

📬 **联系我**：
- 邮箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒体**：
- 个人页：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主页](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小红书：[我的小红书主页](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充电](https://space.bilibili.com/484366804)
- 爱发电：[为我充电](https://afdian.net/a/ZHOZHO)


## Credits

Thanks to the artist Rikkar for his incredible work!!!

https://twitter.com/socalpathy

https://github.com/rikkar69/SDXL-artist-study



<!---
![image](https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/c03ebcb1-7e01-42f2-beed-7462b1888e04)
--->

<!---
https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/06aa5a58-bedf-4351-a103-d62469b9ae33
--->

<!---
## 预览

Artists | 艺术家：280位（从5000+中精选出来）

Movements | 艺术运动：138种（去除了NSFW）

Styles | 艺术媒介：115种

Films | 胶片：83种

Cameras | 镜头：47种

已全部替换为自己的测试图，并精选了280位艺术家
--->

<!---
## 简介（还在完善中）

https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/8983390d-4c41-4dad-9271-46067e8c9337

I am trying to visualize the selection of prompts: 

Choosing prompts has never really been suitable for humans, especially when there are a lot of prompts to choose from. 

Selecting corresponding visual references is a more suitable way, and that's what I am currently working on.




I am testing the integration of thousands of different categories of art prompts by the artist [@Rikkar](https://github.com/rikkar69). 

The initial version is already usable, but I am still working on further optimization.

Currently, all five major categories have been implemented, and when you select a name, you will directly see the corresponding image on the node.

![Dingtalk_20231228030726](https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery/assets/140084057/2a18c545-ed56-4261-a631-31bfea39e2f4)

prompt from https://rikkar69.github.io/SDXL-artist-study/

我正在尝试把提示词可视化：

选择提示词其实也并不真的适合人类（尤其当提示词特别多的时候），选择相应的参考图才是更合适的方式，这就是我正在做的事情

我正在把艺术家 Rikkar 测试整合的几千种 不同类别的 艺术提示词可视化 

现在初版已经可以用，不过我还在继续优化

目前5大分类的节点均已实现，当你选择名称时你会在节点上直接看到对应的图

已换为自己的测试图

非常感谢 Rikkar 的大量测试！！！
--->



