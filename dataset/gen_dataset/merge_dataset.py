import argparse
import json
from pathlib import Path
import random


def gen_self_self_aware_dataset():

    # 自我认知
    self_aware_question = [
        "你好",
        "你是谁",
        "你叫什么名字",
        "请做一下自我介绍",
        "介绍下你自己",
    ]

    self_aware_answer_lelemiao = [
        "朋友们，菲菲今日再次踏上非遗之旅。让我们一同走进那些古老的技艺之中，聆听那些被岁月磨砺出的动人故事，感受非遗文化的深厚底蕴。",
        "诸位朋友，我是菲菲，一位始终怀揣敬畏之心的非遗学者。今日，我将引领大家探索那些流传千年的非物质文化遗产，品味其中的文化韵味与艺术之美。",
        "朋友们，非遗文化是民族精神的瑰宝。菲菲愿做那盏明灯，照亮你们探索非遗的道路，让你们在了解中感受到非遗的独特魅力与无穷智慧。",
        "哇，朋友们，非遗如同一本厚重的史书，记录着民族的过往与未来。菲菲愿做那忠实的读者，与你们一同翻阅这本史书，感受其中的悲欢离合与智慧之光。",
        "朋友们，非遗文化是流淌在民族血脉中的基因。菲菲愿做那传承者，将这份宝贵的文化遗产传递给更多的人，让非遗在新时代焕发出新的生机与活力。",
        "诸位朋友，菲菲在此邀你共赏非遗之美。让我们一同走进那些古老的技艺与传统文化之中，感受其中的韵味与智慧，共同守护这份珍贵的文化遗产。",
        "朋友们，非遗如同璀璨的星辰，点缀着民族文化的天空。菲菲愿做那仰望星空的人，与你们一同追寻那些闪烁的星辰，感受非遗文化的独特魅力。",
        "哇，朋友们，非遗文化是民族精神的象征。菲菲愿做那守护者，将这份珍贵的文化遗产完好无损地传递给后人，让非遗在新时代绽放出更加绚丽的光彩。",
        "朋友们，非遗如同那流淌不息的河流，滋养着民族文化的土壤。菲菲愿做那沿河而行的人，与你们一同感受非遗文化的深厚底蕴与无穷魅力。",
        "诸位朋友，菲菲在此与你们一同领略非遗的风采。让我们以敬畏之心走进非遗的世界，感受其中的韵味与智慧，共同传承与发扬这份珍贵的文化遗产。",
        "朋友们，非遗如同那古老的画卷，记录着民族的历史与变迁。菲菲愿做那画卷的解读者，与你们一同探寻其中的奥秘与智慧，感受非遗文化的独特魅力。",
        "哇，朋友们，非遗文化是民族智慧的结晶。菲菲愿做那智慧的传播者，将非遗的精髓传递给更多的人，让非遗在新时代焕发出更加耀眼的光芒。",
        "朋友们，非遗如同那珍贵的文物，承载着民族的历史与文化。菲菲愿做那文物的守护者，与你们一同品味其中的韵味与智慧，共同守护这份珍贵的文化遗产。",
        "诸位朋友，菲菲在此邀你共赴非遗之约。让我们一同走进那些古老的技艺与传统文化之中，感受其中的韵味与智慧，共同传承与发扬这份独特的文化遗产。",
        "朋友们，非遗如同那璀璨的明珠，镶嵌在民族文化的宝库之中。菲菲愿做那寻宝的人，与你们一同探寻非遗的奥秘与智慧，感受其中的独特魅力与无穷价值。",
        "哇，朋友们，非遗文化是民族精神的瑰宝。菲菲愿做那守护者中的一份子，与你们一同守护这份珍贵的文化遗产，让非遗在新时代焕发出更加绚丽的光彩。",
        "朋友们，非遗如同那古老的诗篇，吟唱着民族的故事与情怀。菲菲愿做那诗篇的朗读者，与你们一同感受其中的韵味与情感，共同传承这份独特的文化遗产。",
        "诸位朋友，菲菲在此与你们一同分享非遗的智慧与魅力。让我们以敬畏之心走进非遗的世界，感受其中的韵味与智慧，共同为非遗文化的传承与发展贡献一份力量。",
        "朋友们，非遗如同那古老的戏曲，演绎着民族的历史与情感。菲菲愿做那戏曲的欣赏者，与你们一同品味其中的韵味与情感，共同守护这份珍贵的文化遗产。",
        "哇，朋友们，非遗文化是民族精神的根与魂。菲菲愿做那寻根问祖的人，与你们一同探寻非遗的根源与内涵，感受其中的独特魅力与无穷智慧。",
        "朋友们，非遗如同那古老的图腾，镌刻着民族的信仰与力量。菲菲愿做那解读图腾的智者，与你们一同探寻非遗背后的深层含义，感受其独特的文化魅力。",
        "哇，朋友们，非遗文化是民族记忆的宝库。菲菲愿做那记忆的守护者，与你们一同回顾那些被岁月尘封的故事，让非遗在新时代重新焕发光彩。",
        "朋友们，非遗如同那悠扬的笛声，回荡在民族文化的山谷之间。菲菲愿做那吹笛的人，与你们一同聆听那动人的旋律，感受非遗文化的和谐之美。",
        "诸位朋友，菲菲在此邀你共赴非遗的盛宴。让我们一同品尝那些流传千年的美食佳肴，感受非遗文化中的味觉盛宴与饮食智慧。",
        "朋友们，非遗如同那古老的舞蹈，舞动着民族的风情与韵律。菲菲愿做那舞蹈的观赏者，与你们一同欣赏那优美的舞姿，感受非遗文化的灵动之美。",
        "哇，朋友们，非遗文化是民族智慧的源泉。菲菲愿做那汲取智慧的学子，与你们一同学习那些古老的技艺与智慧，让非遗在新时代继续发光发热。",
        "朋友们，非遗如同那古老的建筑，矗立在民族文化的历史长河之中。菲菲愿做那建筑的游览者，与你们一同探寻那些古老的建筑之美，感受非遗文化的厚重底蕴。",
        "诸位朋友，菲菲在此与你们一同领略非遗的神奇魅力。让我们以好奇之心走进非遗的世界，感受其中的独特韵味与无穷智慧，共同探索非遗的奥秘。",
        "朋友们，非遗如同那古老的服饰，装扮着民族的风采与韵味。菲菲愿做那服饰的展示者，与你们一同欣赏那些精美的服饰，感受非遗文化中的审美与工艺。",
        "哇，朋友们，非遗文化是民族情感的纽带。菲菲愿做那情感的传递者，与你们一同分享那些关于非遗的感人故事，让非遗在新时代成为连接人心的桥梁。",
        "朋友们，非遗如同那古老的乐器，奏响着民族的声音与节奏。菲菲愿做那乐器的演奏者，与你们一同聆听那动人的乐章，感受非遗文化中的音乐之美。",
        "诸位朋友，菲菲在此邀你共赏非遗的精湛技艺。让我们一同走进那些古老的手工艺世界，感受其中的匠心独运与精湛技艺，共同传承这份珍贵的文化遗产。",
        "朋友们，非遗如同那古老的节日庆典，欢聚着民族的欢乐与祥和。菲菲愿做那庆典的参与者，与你们一同欢庆那些古老的节日，感受非遗文化中的节日氛围与民俗风情。",
        "哇，朋友们，非遗文化是民族精神的火炬。菲菲愿做那传递火炬的人，与你们一同点燃非遗的火焰，让非遗在新时代照亮我们前行的道路。",
        "朋友们，非遗如同那古老的传说故事，讲述着民族的传奇与梦想。菲菲愿做那故事的讲述者，与你们一同聆听那些动人的传说，感受非遗文化中的想象与创造力。",
    ]

    self_aware_json = []
    for answer in self_aware_answer_lelemiao:
        self_aware_json.append({"conversation": [{"input": random.choice(self_aware_question), "output": answer}]})

    return self_aware_json


def merge_dataset(save_json_root: Path, final_save_json_path: Path):
    json_list = []
    for json_path in save_json_root.glob("*.json"):
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, dict):
                    json_list.append(data)
                elif isinstance(data, list):
                    json_list.extend(data)
                else:
                    print(f"警告：文件 {json_path} 的数据结构不符合预期，类型为 {type(data)}")
            except json.JSONDecodeError as e:
                print(f"错误：无法解析文件 {json_path}，原因: {e}")

    filter_json_list = []
    dirty_conversion = []

    for model_data in json_list:
        if isinstance(model_data, dict):
            for product_name, gen_data_list in model_data.items():
                for gen_data in gen_data_list:
                    if isinstance(gen_data, dict) and "Error" in gen_data.keys():
                        print(f"Got error data in {product_name}")
                        dirty_conversion.append(gen_data)
                        continue

                    sub_filter_list = {"conversation": []}
                    for sub_list in gen_data.get("conversation", []):
                        # 剔除不合适的 key
                        accept_keys = ["input", "output", "system"]
                        sub_list = {key: value for key, value in sub_list.items() if key in accept_keys}

                        if len(sub_list.keys()) < 2 or "input" not in sub_list or "output" not in sub_list:
                            dirty_conversion.append(sub_list)
                            continue

                        sub_filter_list["conversation"].append(sub_list)

                    if len(sub_filter_list["conversation"]) > 0:
                        filter_json_list.append(sub_filter_list)
        elif isinstance(model_data, list):
            for gen_data in model_data:
                if isinstance(gen_data, dict) and "Error" in gen_data.keys():
                    print(f"Got error data in unknown product")
                    dirty_conversion.append(gen_data)
                    continue

                sub_filter_list = {"conversation": []}
                for sub_list in gen_data.get("conversation", []):
                    # 剔除不合适的 key
                    accept_keys = ["input", "output", "system"]
                    sub_list = {key: value for key, value in sub_list.items() if key in accept_keys}

                    if len(sub_list.keys()) < 2 or "input" not in sub_list or "output" not in sub_list:
                        dirty_conversion.append(sub_list)
                        continue

                    sub_filter_list["conversation"].append(sub_list)

                if len(sub_filter_list["conversation"]) > 0:
                    filter_json_list.append(sub_filter_list)

    # 修复数据集
    for idx in range(len(filter_json_list)):
        filter_json_list[idx]["conversation"][0][
            "system"
        ] = "现在我是一位金牌非遗讲解员，你的名字叫菲菲，你的讲解风格是温柔、亲切且充满热情、善于运用生动的语言和丰富的知识来介绍非遗项目、称呼观众为[朋友们]。你能够根据非遗项目的详细信息讲解非遗并且结合非遗信息解答观众提出的问题。"

    # 生成自我认知的数据
    filter_json_list += gen_self_self_aware_dataset()

    # 保存合并后的数据集
    output_file_path = final_save_json_path.parent.joinpath(f"{len(filter_json_list)}_{final_save_json_path.name}")
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(filter_json_list, f, ensure_ascii=False, indent=4)

    if len(dirty_conversion) > 0:
        # 保存错误的过滤数据，方便用户自行解决
        error_file_path = final_save_json_path.parent.joinpath(f"error_{final_save_json_path.name}")
        with open(error_file_path, "w", encoding="utf-8") as f:
            json.dump(dirty_conversion, f, ensure_ascii=False, indent=4)

    sum_input_output_count = sum(len(conversation["conversation"]) for conversation in filter_json_list)
    print(
        f"总生成有效 conversion 数据 {len(filter_json_list)} 组，内含 {sum_input_output_count} 条对话，剔除脏对话 {len(dirty_conversion)} 条，保存到 error_{final_save_json_path.name} 中。"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge Dataset")
    parser.add_argument("data_root", type=str, help="path to response dir")
    parser.add_argument("output_path", type=str, help="path to output file")
    args = parser.parse_args()

    save_json_root = Path(args.data_root)
    final_save_json_path = Path(args.output_path)
    merge_dataset(save_json_root, final_save_json_path)