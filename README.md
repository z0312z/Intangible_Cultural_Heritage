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
  - [📌 目录](#目录)
  - [🖼 演示](#%EF%B8%8F-演示视频)
  - [🛠 环境搭建](#环境搭建)
  - [📜 微调数据](#微调数据)
    - [主播性格](#主播性格)
    - [产品信息](#产品信息)
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
studio-conda -t streamer-sales -o pytorch-2.1.2
conda activate Intangible_Cultural_Heritage
pip install -r requirements.txt
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
