import streamlit as st
import pandas as pd

st.set_page_config(page_title="한국 MBTI 비율", page_icon="🇰🇷", layout="centered")

st.title("🇰🇷 우리나라 MBTI 비율")
st.markdown(
    "대한민국의 MBTI 정식 보급기관인 **어세스타(Assesta)** 가 공개한 "
    "한국인 MBTI 유형 분포 자료를 그래프로 살펴봐요! 📊"
)
st.caption("출처: 어세스타(Assesta) 공개 자료, 2023년 기준 · 재미로 참고해주세요 😉")

st.divider()

# ------------------------------------------------------------
# 데이터 (어세스타 공개 자료 기준, 합계 약 100%)
# ------------------------------------------------------------
data = {
    "MBTI": [
        "ISTJ", "ESTJ", "ENFP", "ISFJ", "ESFJ", "ESFP", "INFP", "ISFP",
        "ESTP", "ISTP", "ENTP", "ENTJ", "ENFJ", "INTJ", "INTP", "INFJ",
    ],
    "비율(%)": [
        12.8, 12.4, 9.7, 8.3, 8.2, 7.2, 6.7, 6.5,
        4.2, 4.1, 3.6, 3.5, 3.3, 3.3, 3.2, 2.9,
    ],
    "이모지": [
        "📋", "🏢", "🚀", "🛡️", "🤝", "🎤", "🌈", "🎨",
        "⚡", "🔧", "💡", "👑", "🌟", "♟️", "🧪", "🔮",
    ],
}
df = pd.DataFrame(data)
df["유형"] = df["이모지"] + " " + df["MBTI"]

# ------------------------------------------------------------
# 하이라이트 카드
# ------------------------------------------------------------
top = df.iloc[0]
bottom = df.iloc[-1]
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🥇 가장 흔한 유형", value=f"{top['이모지']} {top['MBTI']}", delta=f"{top['비율(%)']}%")
with col2:
    st.metric(label="🦄 가장 희귀한 유형", value=f"{bottom['이모지']} {bottom['MBTI']}", delta=f"{bottom['비율(%)']}%")

st.divider()

# ------------------------------------------------------------
# 그래프
# ------------------------------------------------------------
st.markdown("### 📊 전체 유형별 비율")
chart_df = df.set_index("유형")[["비율(%)"]]
st.bar_chart(chart_df, horizontal=True, color="#FF6F61")

st.divider()

with st.expander("🧐 이 그래프 어떻게 볼까요?"):
    st.markdown(
        "- 한국에서는 **ISTJ, ESTJ** 같은 계획적이고 현실적인 유형이 상대적으로 많아요. 📋🏢\n"
        "- 반대로 **INFJ, INTP** 처럼 내면 탐구형 유형은 비교적 드문 편이에요. 🔮🧪\n"
        "- MBTI 비율은 조사기관·시기에 따라 달라질 수 있어요. 참고 자료로만 활용해주세요! 🙂\n"
        "- 내 MBTI가 희귀하든 흔하든, **나만의 강점**은 따로 있다는 걸 잊지 마세요! ✨"
    )

st.page_link("app.py", label="🏠 메인으로 돌아가기", icon="🔙")
