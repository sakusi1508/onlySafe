import streamlit as st

st.set_page_config(page_title="安全対策費計算", layout="centered")

# タイトル（法定福利費の文言を削除）
st.title("本体金額計(円)から安全対策費を計算するツール")

# 説明テキスト（法定福利費の項目を削除）
st.markdown("""


計算式は以下の通りです

- 作業名、品名 × 0.08 = 安全対策費
- 本体金額計(円) = 作業名、品名 + 安全対策費
""")

# 注意書き
with st.expander("📌 使用上の注意"):
    st.warning("""
- 本体金額計の値は半角数字で入力してください。
- カンマ（,）や全角数字は使わないでください。
- 小数（例：123.45）も入力可能です。
    """)

# 入力フィールド
st.markdown('<span style="color:red;">本体金額計(円)の値を入力してください（例：123）</span>', unsafe_allow_html=True)

# 入力欄（ラベルなし）
d_input = st.text_input("", value="")

# 計算処理
if st.button("計算する"):
    try:
        d = float(d_input)
        

        a = d / 1.08
        b = a * 0.08
        
       

        st.success("✅ 計算結果")
        st.write(f"品名 = {a:.2f}")
        st.write(f"安全対策費 = {b:.2f}")
        # 法定福利費の表示を削除しました
        
    except ValueError:
        st.error("数値を正しく入力してください（例：123.45）")

# フッター
st.markdown("---")
st.caption("© 2025 ABC Calculator")