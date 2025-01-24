# 古韵流芳非遗文化探秘--遗风寻根

<!-- PROJECT LOGO -->
<p align="center">
   <a href="https://github.com/z0312z/Intangible-Cultural-Heritage/">
   </a>
</p>

## 🔆介绍：
项目为书生浦语大模型实战训练营项目，学习于书生浦语大模型实战营。

## 📌概述：
在喧嚣的现代生活中，你是否曾渴望触摸那些古老而美丽的非遗文化，却苦于无处寻觅其踪迹？是否曾幻想过，能够亲身走进那些充满历史底蕴的技艺世界，感受那份沉淀千年的匠心独运？来“古韵流芳非遗文化探秘——遗风寻根”吧！

这是一个致力于让每一份非遗美丽更加美丽的讲解大模型项目。我们精心打造了一个全方位、沉浸式的非遗文化体验空间，带你穿越时空，领略那些濒临失传的传统技艺与民俗的独特魅力。在这里，你将亲身感受非遗文化的深厚底蕴，品味其中蕴含的历史韵味，成为非遗文化的传承者与守护者，让这份美丽在你的手中焕发出新的光彩。

本项目基于InternLM2.5系列大模型，通过xtuner进行指令微调，结合LMDeploy加速推理技术，打造出高效的非遗讲解大模型。该模型支持ASR语音转文本功能，用户可通过语音轻松提问，即刻获取非遗相关的详尽解答。同时，🗣TTS文本秒转语音技术让非遗传奇故事通过清新悦耳的声音生动再现。我们还提供🎥定制数字人讲解视频服务，📜详尽的非遗说明书深度解读每一项文化遗产的独特魅力，让用户对非遗有更深入的了解。

## ✨主要功能亮点
- 🎙 语音秒转文本，轻松通过语音提问探索非遗奥秘。
- 🗣 文本秒转语音技术，非遗传奇声声入耳，如在眼前。
- 🎥 定制数字人讲解视频，一键生成，非遗知识生动演绎。
- 📜 详尽非遗说明书，深度解读非遗，了解非遗的历史背景与文化内涵。
- 🌈 简洁直观界面，陈列了各类非遗作品，如翻阅古籍般流畅，非遗之美一目了然。
- 🎨 一键生成，无论是语音转文字的便捷，还是视觉呈现的精致，都让你的非遗探索之旅如行云流水，尽在掌握。

## 🏷️架构图
![架构图](./Information/架构图2.png)

## 📌 目录

- [古韵流芳非遗文化探秘--遗风寻根](#古韵流芳非遗文化探秘--遗风寻根)
  - [📢 简介](#介绍)
  - [📌 目录](#-目录)
  - [🖼 演示](#%EF%B8%8F-演示视频)
  - [🛠 环境搭建](#-环境搭建)
  - [📜 微调数据](#-微调数据)
    - [讲解员信息](#讲解员信息)
    - [非遗信息](#非遗信息)
    - [用户可能提问](#用户可能提问)
    - [数据集生成 Prompt](#数据集生成-prompt)
    - [启动生成](#启动生成)
  - [📚 RAG 说明书数据生成](#-rag-说明书数据生成)
  - [🎨 XTuner 微调 InternLM2](#xtuner-微调-internlm2)
  - [🦸 数字人](#数字人)
  - [🔊 TTS \& 🎙️ ASR](#tts--️-asr)
  - [🚀 量化](#量化)
  - [🛰 部署](#部署)
  - [结语](#结语)

## 🎞️ 🎭演示视频
[点击观看](https://www.bilibili.com/video/BV1DikTYDEaN/?share_source=copy_web&vd_source=60a9d4803dceda5b0d29cfab7058dff0)

## 🛠 环境搭建

```bash
git https://github.com/z0312z/Intangible_Cultural_Heritage.git
cd Intangible_Cultural_Heritage
conda env create -f environment.yml
conda activate Intangible_Cultural_Heritage
pip install -r requirements.txt
```
直接部署启动：
```
streamlit run app.py --server.address=0.0.0.0 --server.port 7860
```

## 📜 微调数据

数据集生成有关的配置都在 [configs/conversation_cfg.yaml](https://github.com/z0312z/Intangible_Cultural_Heritage/blob/main/configs/conversation_cfg.yaml) 中。

<p align="center">
  <img src="https://github.com/z0312z/Intangible_Cultural_Heritage/blob/main/Information/%E6%9E%B6%E6%9E%84%E5%9B%BE%E6%95%B0%E6%8D%AE%E9%83%A8%E5%88%86.png" alt="gen_data" width="45%">
</p>

从架构图中可以看出我们将数据集分成了非遗和主播两个部分。其中非遗部分含有其特点和图片，主播部分包括主播的基本信息及特点。
数据部分还包括了：

- 用户可能问到的问题
- 数据格式化成微调 json 以及自我认知

### 讲解员信息

为讲解员设置基本信息和特点使其更贴近需求:

```yaml
# 角色及其性格
role_type:
  菲菲: # 萝莉
    - 知识渊博
    - 讲解生动
    - 熟练运用非遗相关的历史与文化典故
    - 称呼观众为[亲爱的朋友们]
```

### 非遗信息

非遗列表的雏形是由两个prompt通过大模型生成的：

> 第一个 prompt: 帮我列举10种常见的非遗种类，并每种举例5个其子类
>
> 每个类 prompt: 你可以帮我举例每个非遗的6个亮点或特点，, 然后用python dict形式输出：{类名：[特点1, 特点2] ...} ，去掉特点12的字样，除python字典外的其他都不要输出，不要有任何的警告信息。 [xxx]

详见：[configs/conversation_cfg.yaml L82-L400](https://github.com/z0312z/Intangible_Cultural_Heritage/blob/main/configs/conversation_cfg.yaml#L82-L400)

```yaml
product_list:
    神话:
      盘古开天辟地: [创世主题, 英雄主义, 象征意义, 宇宙观, 自然崇拜, 口耳相传]
      女娲补天: [拯救世界, 母性光辉, 象征意义, 宇宙秩序, 自然灾害, 人类起源]
      精卫填海: [坚持不懈, 复仇与抗争, 象征意义, 自然力量, 悲剧色彩, 民族精神]
      夸父逐日: [追求光明, 英雄主义, 象征意义, 自然崇拜, 悲剧结局, 探索精神]
      后羿射日: [英雄救世, 勇敢无畏, 象征意义, 自然灾害的克服, 射箭技艺, 神话色彩]
    民间传说:
      孟姜女哭长城: [爱情悲剧, 忠诚与牺牲, 社会批判, 文化符号, 女性形象, 民间情感]
      牛郎织女: [爱情忠贞, 家庭团圆, 星象传说, 七夕节日, 封建礼教批判, 文化传承]
      梁祝传说: [爱情悲剧, 家庭阻力, 性别角色, 文化传承, 民间信仰, 美好愿景]
      白蛇传: [人妖之恋, 爱情考验, 法海阻挠, 忠贞不渝, 文化象征, 世代传承]
      西湖龙井的传说: [茶文化, 善良与抗争, 地方特色, 民间故事, 茶树象征, 文化传承]
    民间故事:
      杜康酿酒: [偶然发现, 酿酒技艺, 人物传奇, 历史背景, 文化寓意, 智慧启示]
      阿凡提的故事: [智慧与幽默, 社会批判, 人物形象, 正义与邪恶, 讽刺艺术, 民间智慧]
      三个和尚: [团结合作, 互相推诿, 教训寓意, 寺庙生活, 传统寓言, 道德启示]
      田螺姑娘: [爱情故事, 善良勤劳, 美好愿望, 人物形象, 幸福生活, 民间奇谈]
      长发妹: [勇敢抗争, 泉水发现, 山妖威胁, 村民福祉, 英雄形象, 乡土传奇]

      ....
```

### 用户可能提问

在讲解员输出了自己的文案之后，客户肯定会产生新的问题需要继续解答，所以我举例了 10 个用户可能问到的问题的方向，生成的这些问题的 prompt 也在这里标注了

```yaml
# prompt: 了解非遗的时候，客户常会问题的问题，举例10个, 只列举大类就行
customer_question_type:
  - 历史背景与文化渊源
  - 制作工艺与技艺特点
  - 材质选择与处理
  - 传承人与传承情况
  - 展览信息与参观流程
  - 保护措施与现状
  - 作品欣赏与解读
  - 文化价值与意义
  - 互动体验与参与方式
  - 后续发展与推广计划
```

### 数据集生成 Prompt

配置文件最核心的部分就是如何生成 prompt 给到商用大模型的，这里配置了每个对话的条目，以及生成数据集的细节：

详见：[configs/conversation_cfg.yaml L1-L46](https://github.com/z0312z/Intangible_Cultural_Heritage/blob/main/configs/conversation_cfg.yaml#L1-L46)

```yaml
# 对话设置
conversation_setting:

  system: "现在你是一位金牌非遗讲解员，你的名字叫{role_type}，你的说话方式是{character}。你能够根据非遗信息讲解非遗并且结合非遗信息解答用户提出的疑问。"
  first_input: "我的{product_info}，你需要根据我给出的非遗信息撰写一段非遗讲解文案。你需要突出非遗项目的独特魅力和文化价值，激发听众的兴趣和尊重。"

# 数据集生成设置
data_generation_setting:

  # 每个产品生成 ${each_product_gen} 个 conversion 数据，conversion 中包含【文案 + QA】，
  each_product_gen: 3

  # 每个 conversion 中的的对话数，文案为 1 个，其余会生成 ${each_conversation_qa} - 1 个 QA 
  each_conversation_qa: 5

  # 每个文案生成随机抽取 ${each_pick_hightlight} 个亮点
  each_pick_hightlight: 3

  # 每个文案生成后随机抽取 ${each_pick_hightlight} 个问题生成用户的提问
  each_pick_question: 3

  # 数据集生成 prompt
  dataset_gen_prompt: 现在你是一位金牌非遗讲解员，你的名字叫{role_type}，你的说话方式是{character}。
                      我的{product_info}，你需要根据我给出的非遗产品信息撰写一段至少600字的直播讲解文案。你需要深入挖掘并放大产品的非遗文化价值，激发观众的兴趣，同时传递对非遗文化的尊重与热爱。
                      输出文案后，结合非遗产品信息站在观众的角度根据[{customer_question}]提出{each_conversation_qa}个问题并解答。
                      全部输出的信息使用我期望的 json 格式进行输出：{dataset_json_format}。注意 json 一定要合法。
 
  # 数据生成 json 格式
  dataset_json_format: 
    '{
      "conversation": [
        {
          "output": 非遗讲解文案，格式化一行输出，不要换行。
        },
        {
          "input": 观众的问题,
          "output": 讲解员回答
        },
        {
          "input": 观众的问题,
          "output": 讲解员回答
        },
        ... 直到问题结束
      ]
    }'


```



## 🧩开发进度
- 项目启动与需求整理
- 架构设计阶段
- 数据训练
- ASR与TTS模块开发阶段
- 数字人模块开发阶段
- 前端开发阶段

## 🚩后续规划
- 内容拓展与更新
- 模型微调与性能提升

## 特别鸣谢
感谢书生浦语大模型实战营和Streamer-Sales销冠——卖货主播大模型项目的支持
- 书生浦语大模型实战营：[https://github.com/InternLM/Tutorial](https://github.com/InternLM/Tutorial)
- Streamer-Sales销冠——卖货主播大模型：[https://github.com/PeterH0323/Streamer-Sales](https://github.com/PeterH0323/Streamer-Sales)
