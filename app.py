import streamlit as st

# 設定頁面
st.set_page_config(page_title="從牛車到AI：電腦演進教學互動", layout="wide")

# 標題與引言
st.title("從牛車到AI：電腦演進與基礎原理")
st.markdown(
    """
    **引言**：1962年，一台巨大而脆弱的 IBM 650 真空管電腦，憑藉牛車從基隆港
    緩緩運抵國立陽明交通大學。這段情景，是台灣資訊史的關鍵一刻，也象徵了人類
    如何一步步跨越技術困境，創造現代電腦架構。讓我們從牛車雕像出發，體驗電腦
    五代演進、馮紐曼架構與二進位運算的核心邏輯！
    """
)

# 第一部分：電腦世代排序
st.header("1. 電腦世代排序挑戰")
gen_options = [
    "第一代：真空管電腦",
    "第二代：電晶體電腦",
    "第三代：積體電路電腦",
    "第四代：超大型積體電路／個人電腦",
    "第五代：AI 與量子計算機"
]
st.write("請依照時代先後順序，為下列世代編號：")
selections = []
for i in range(1, 6):
    selections.append(st.selectbox(f"第 {i} 位", gen_options, key=f"order_{i}"))

if st.button("檢查排序"):
    if len(set(selections)) < 5:
        st.warning("請確保每個世代都只選一次。")
    else:
        if selections == gen_options:
            st.success("🎉 排序正確！恭喜闖關成功！")
        else:
            st.error("排序錯誤，再試一次！")

# 第二部分：馮紐曼架構說明
st.header("2. 馮紐曼架構角色說明")
roles = {
    "輸入裝置": "將使用者輸入的資料轉換成電腦可以處理的形式（如鍵盤）。",
    "記憶體": "短暫儲存程式與資料，以供運算器讀寫。",
    "控制器": "解讀並執行指令，協調其他模組的執行流程。",
    "運算器 (ALU)": "執行算術與邏輯運算。",
    "輸出裝置": "將運算結果轉換成人類可理解的輸出（如螢幕、印表機）。"
}
selected_role = st.selectbox("選擇要了解的模組", list(roles.keys()))
st.info(f"**{selected_role}**：{roles[selected_role]}")

# 第三部分：二進位加法練習
st.header("3. 二進位加法練習")
col1, col2 = st.columns(2)
with col1:
    b1 = st.text_input("輸入二進位數 A", value="101")
with col2:
    b2 = st.text_input("輸入二進位數 B", value="011")

if st.button("計算二進位和"):
    try:
        result = bin(int(b1, 2) + int(b2, 2))[2:]
        st.success(f"結果：{result} (二進位)")
    except ValueError:
        st.error("請輸入有效的 0/1 組成的二進位數字。")

# 頁尾
st.markdown("---")
st.markdown("此互動原型於3小時內完成，用於教學示範。安裝 Streamlit 並執行：`streamlit run app.py`即可啟動。")
