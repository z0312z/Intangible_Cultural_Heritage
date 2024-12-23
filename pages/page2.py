import random
from datetime import datetime
from pathlib import Path
import streamlit as st
from utils.web_configs import WEB_CONFIGS
from audiorecorder import audiorecorder
from utils.asr.asr_worker import process_asr
from utils.digital_human.digital_human_worker import show_video
from utils.infer.lmdeploy_infer import get_turbomind_response
from utils.model_loader import ASR_HANDLER, LLM_MODEL, RAG_RETRIEVER
from utils.tools import resize_image


# 设置页面配置，包括标题、图标、布局和菜单项
st.set_page_config(
    page_title="非遗讲解平台",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# 非遗讲解平台",
    },
)


def on_btn_click(*args, **kwargs):
    """
    处理按钮点击事件的函数。
    """
    if kwargs["info"] == "清除对话历史":
        st.session_state.messages = []
    elif kwargs["info"] == "返回非遗项目展示页":
        st.session_state.page_switch = "app.py"
    else:
        st.session_state.button_msg = kwargs["info"]


def init_sidebar():
    """
    初始化侧边栏界面，展示非遗信息，并提供操作按钮。
    """
    asr_text = ""
    with st.sidebar:
        # 标题
        st.markdown("## 非遗讲解员  ——  菲菲")
        st.subheader("目前讲解")
        with st.container(height=400, border=True):
            st.subheader(st.session_state.product_name)

            image = resize_image(st.session_state.image_path, max_height=100)
            st.image(image, channels="bgr")

            st.subheader("非遗特点", divider="grey")
            st.markdown(st.session_state.hightlight)

            want_to_buy_list = [
                "我对这个非遗项目非常感兴趣。",
                "我想了解更多关于这个非遗项目的细节。",
                "我打算收藏这个非遗项目。",
                "我准备分享这个非遗项目到我的社交网络。",
                "我希望参加这个非遗项目的体验活动。",
                "我想知道如何支持这个非遗项目的传承。",
                "我对这个非遗项目的传统技艺感到好奇。",
                "我有兴趣参与保护这个非遗项目。",
            ]
            buy_flag = st.button("了解更多 📖", on_click=on_btn_click, kwargs={"info": random.choice(want_to_buy_list)})


        # 是否生成 TTS
        if WEB_CONFIGS.ENABLE_TTS:
            st.subheader("TTS 配置", divider="grey")
            st.session_state.gen_tts_checkbox = st.toggle("生成语音", value=st.session_state.gen_tts_checkbox)

        if WEB_CONFIGS.ENABLE_DIGITAL_HUMAN:
            # 是否生成 数字人
            st.subheader(f"数字人 配置", divider="grey")
            st.session_state.gen_digital_human_checkbox = st.toggle(
                "生成数字人视频", value=st.session_state.gen_digital_human_checkbox
            )

        st.subheader("页面切换", divider="grey")
        st.button("返回非遗项目展示页", on_click=on_btn_click, kwargs={"info": "返回非遗项目展示页"})

        st.subheader("对话设置", divider="grey")
        st.button("清除对话历史", on_click=on_btn_click, kwargs={"info": "清除对话历史"})

        # 模型配置
        # st.markdown("## 模型配置")
        # max_length = st.slider("Max Length", min_value=8, max_value=32768, value=32768)
        # top_p = st.slider("Top P", 0.0, 1.0, 0.8, step=0.01)
        # temperature = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.01)

    return asr_text


def init_message_block(meta_instruction, user_avator, robot_avator):

    # 在应用重新运行时显示聊天历史消息
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])

            if message.get("wav") is not None:
                # 展示语音
                print(f"Load wav {message['wav']}")
                with open(message["wav"], "rb") as f_wav:
                    audio_bytes = f_wav.read()
                st.audio(audio_bytes, format="audio/wav")

    # 如果聊天历史为空，则显示产品介绍
    if len(st.session_state.messages) == 0:
        # 直接产品介绍
        get_turbomind_response(
            st.session_state.first_input,
            meta_instruction,
            user_avator,
            robot_avator,
            LLM_MODEL,
            session_messages=st.session_state.messages,
            add_session_msg=False,
            first_input_str="",
            enable_agent=False,
        )

    # 初始化按钮消息状态
    if "button_msg" not in st.session_state:
        st.session_state.button_msg = "x-x"


def process_message(user_avator, prompt, meta_instruction, robot_avator):
    # Display user message in chat message container
    with st.chat_message("user", avatar=user_avator):
        st.markdown(prompt)

    get_turbomind_response(
        prompt,
        meta_instruction,
        user_avator,
        robot_avator,
        LLM_MODEL,
        session_messages=st.session_state.messages,
        add_session_msg=True,
        first_input_str=st.session_state.first_input,
        rag_retriever=RAG_RETRIEVER,
        product_name=st.session_state.product_name,
        enable_agent=st.session_state.enable_agent_checkbox,
    )


def main(meta_instruction):

    # 检查页面切换状态并进行切换
    if st.session_state.page_switch != st.session_state.current_page:
        st.switch_page(st.session_state.page_switch)

    # 页面标题
    st.title("古韵流芳非遗文化探秘")

    # 说明
    st.info(
        "本项目是基于人工智能的文字、语音、视频生成领域搭建的非遗讲解大模型。用户被授予使用此工具创建文字、语音、视频的自由，但用户在使用过程中应该遵守当地法律，并负责任地使用。开发人员不对用户可能的不当使用承担任何责任。",
        icon="❗",
    )

    # 初始化侧边栏
    asr_text = init_sidebar()

    # 初始化聊天历史记录
    if "messages" not in st.session_state:
        st.session_state.messages = []

    message_col = None
    if st.session_state.gen_digital_human_checkbox and WEB_CONFIGS.ENABLE_DIGITAL_HUMAN:

        with st.container():
            message_col, video_col = st.columns([0.6, 0.4])

            with video_col:
                # 创建 empty 控件
                st.session_state.video_placeholder = st.empty()
                with st.session_state.video_placeholder.container():
                    show_video(st.session_state.digital_human_video_path, autoplay=True, loop=True, muted=True)

            with message_col:
                init_message_block(meta_instruction, WEB_CONFIGS.USER_AVATOR, WEB_CONFIGS.ROBOT_AVATOR)
    else:
        init_message_block(meta_instruction, WEB_CONFIGS.USER_AVATOR, WEB_CONFIGS.ROBOT_AVATOR)

    # 输入框显示提示信息
    hint_msg = "你好，可以问我任何关于非遗项目的问题"
    if st.session_state.button_msg != "x-x":
        prompt = st.session_state.button_msg
        st.session_state.button_msg = "x-x"
        st.chat_input(hint_msg)
    elif asr_text != "" and st.session_state.asr_text_cache != asr_text:
        prompt = asr_text
        st.chat_input(hint_msg)
        st.session_state.asr_text_cache = asr_text
    else:
        prompt = st.chat_input(hint_msg)

    # 接收用户输入
    if prompt:

        if message_col is None:
            process_message(WEB_CONFIGS.USER_AVATOR, prompt, meta_instruction, WEB_CONFIGS.ROBOT_AVATOR)
        else:
            # 数字人启动，页面会分块，放入信息块中
            with message_col:
                process_message(WEB_CONFIGS.USER_AVATOR, prompt, meta_instruction, WEB_CONFIGS.ROBOT_AVATOR)


print("into sales page")
st.session_state.current_page = "pages/page2.py"

if "sales_info" not in st.session_state or st.session_state.sales_info == "":
    st.session_state.page_switch = "app.py"
    st.switch_page("app.py")

main((st.session_state.sales_info))
