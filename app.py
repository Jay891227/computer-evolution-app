# app.py
import streamlit as st
from streamlit_sortables import sort_items
from streamlit_drawable_canvas import st_canvas
from streamlit_lottie import st_lottie
from streamlit_chat import message
import requests, time, random

# --- Helper to load Lottie animations ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return {}
    return r.json()

# --- Page and Theme Config ---
st.set_page_config(
    page_title="追尋智械之光：電腦發展史闖關",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Sidebar
st.sidebar.image("https://i.imgur.com/your_school_logo.png", width=120)
st.sidebar.markdown("# 智械探險隊")

# Lottie for header
lottie_clock = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_p8bfn5to.json")
st_lottie(lottie_clock, height=150, key="header")

st.title("🌌 追尋智械之光：電腦發展史闖關遊戲")
st.markdown("> 幫助先驅者收集五大「智慧之核」，重建被遺忘的電腦神殿！")

# Initialize session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "tubes" not in st.session_state:
    st.session_state.tubes = [True]*6
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tabs for stages
tabs = st.tabs([
    "序幕：牛車引言",
    "關卡1：齒輪核心",
    "關卡2：資料之眼",
    "關卡3：能量之心",
    "關卡4：微縮之力",
    "關卡5：組裝之魂",
    "關卡6：智能之眼"
])

# --- 序幕：牛車引言 ---
with tabs[0]:
    st.header("序幕：牛車載電腦")
    st.image("https://i.imgur.com/3xOkeS3.jpg", use_column_width=True, caption="1962 IBM 650 牛車運抵交大")
    choice = st.radio("為何要用牛車運送？", [
        "真空管過於脆弱，怕震動",
        "那是當時最先進的物流方式",
        "為了展示傳統與現代結合"
    ], index=0)
    if st.button("提交說明"):
        if choice == "真空管過於脆弱，怕震動":
            st.success("👍 正確！真空管又重又怕震，需要穩定慢運。")
        else:
            st.error("❌ 再想想真空管本身的特性。")

# --- 關卡1：機械計算器（齒輪核心） ---
with tabs[1]:
    st.header("關卡1：機械計算器—齒輪核心")
    st.write("請拖拉小齒輪到「3」和「5」的位置，並計時完成。")
    # Canvas for draggable gears (simplified)
    gear_canvas = st_canvas(
        fill_color="rgba(0,0,0,0)",  # transparent
        stroke_width=2,
        stroke_color="#555",
        background_image=None,
        update_streamlit=True,
        height=200, width=400,
        drawing_mode="transform"  # allow drag
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("開始計時"):
            st.session_state.start_time = time.time()
    with col2:
        if st.button("完成"):
            if st.session_state.start_time:
                elapsed = time.time() - st.session_state.start_time
                st.balloons()
                st.metric("用時", f"{elapsed:.2f} 秒")
            else:
                st.warning("請先按「開始計時」。")

    st.info("**說明**：Pascal 的機械加法器由齒輪啮合實現加減，但體積大且易卡死。")

# --- 關卡2：打孔卡片（資料之眼） ---
with tabs[2]:
    st.header("關卡2：打孔卡片—資料之眼")
    st.write("條件：身高>160且年齡15-16，請在4×4卡片上打孔（選擇編號）。")
    holes = list(range(1,17))
    selected = st.multiselect("請點擊要打孔的位置編號", holes, default=[])
    if st.button("篩選結果"):
        answer = {2,5,7,12}
        if set(selected)==answer:
            st.success("✅ 正確！已篩選出所有符合條件的資料。")
        else:
            st.error(f"❌ 錯誤。正確是 {sorted(answer)}，你選 {selected}。")
    st.info("**1860** Hollerith 發明打孔卡，自動化數據處理由此開始。")

# --- 關卡3：真空管模擬（能量之心） ---
with tabs[3]:
    st.header("關卡3：真空管模擬—能量之心")
    st.write("勾選代表「通電(1)」；按「燒毀一隻」模擬真空管故障。")
    cols = st.columns(6)
    for i in range(6):
        with cols[i]:
            icon = "💡" if st.session_state.tubes[i] else "💥"
            if st.button(icon, key=f"tube_{i}"):
                st.session_state.tubes[i] = not st.session_state.tubes[i]
    if st.button("燒毀一隻"):
        idx = random.randint(0,5)
        st.session_state.tubes[idx] = False
        st.error(f"管子{idx+1}已燒壞！")
    st.write("目前狀態：", ["通" if x else "斷" for x in st.session_state.tubes])
    st.info("**1940s** ENIAC 用真空管運算，但耗能高、易故障。")

# --- 關卡4：電晶體 & IC（微縮之力） ---
with tabs[4]:
    st.header("關卡4：電晶體與IC—微縮之力")
    st.write("在右圖上點擊 3 處缺陷，用紅點標記。")
    st.image("https://i.imgur.com/1aK5nQK.png", width=400, caption="積體電路示意圖")
    canvas_result = st_canvas(
        fill_color="rgba(255,0,0,0.3)",
        stroke_width=10,
        stroke_color="red",
        background_image=None,
        update_streamlit=True,
        height=300, width=400,
        drawing_mode="point"
    )
    if st.button("檢查標記"):
        objs = canvas_result.json_data["objects"]
        if len(objs)>=3:
            st.success("✅ 偵測到你標記了至少3處缺陷！")
        else:
            st.error("❌ 請標記至少3處缺陷。")
    st.info("**1958** Kilby & Noyce 發明IC，大幅縮小元件。")

# --- 關卡5：PC組裝（組裝之魂） ---
with tabs[5]:
    st.header("關卡5：微處理器與PC—組裝之魂")
    parts = ["CPU","RAM","主機板","儲存裝置","電源","I/O"]
    order = sort_items("請將零件拖曳到此處，完成PC組裝", parts)
    if st.button("檢查組裝"):
        if order==parts:
            st.success("🎉 PC 組裝成功！")
        else:
            st.error(f"❌ 順序錯誤：{order}")
    st.info("**1971** Intel 4004 首顆微處理器帶來個人電腦革命。")

# --- 関卡6：AI Chatbot（智能之眼） ---
with tabs[6]:
    st.header("關卡6：AI時代—智能之眼")
    user_input = st.text_input("問AI一個問題", "")
    if user_input:
        st.session_state.chat_history.append({"user": user_input})
        # 簡易回覆
        reply = {
            "什麼是馮紐曼架構": "馮紐曼架構包含輸入、記憶、控制、運算、輸出五大模組。",
            "電晶體": "電晶體是一種半導體元件，可控制電流開/關。",
        }.get(user_input, "這是一個有趣的問題，我會繼續學習！")
        st.session_state.chat_history.append({"bot": reply})
    for chat in st.session_state.chat_history:
        if "user" in chat:
            message(chat["user"], is_user=True)
        else:
            message(chat["bot"])
    if st.button("清除對話"):
        st.session_state.chat_history = []
    st.info("**2010s** 深度學習與Transformer引領生成式AI風潮。")

# --- Footer ---
st.markdown("---")
st.markdown("📖 **版權**：此教學互動由[你的學校]提供，並以 MIT 授權。")
