import streamlit as st
import pandas as pd

st.set_page_config(page_title="나라별 MBTI 분포", page_icon="🌍", layout="centered")

st.title("🌍 나라별 MBTI 분포 비교")
st.markdown("MBTI 비율은 나라마다 조금씩 다르게 나타나요. 우리나라와 다른 나라를 비교해볼까요? 🌐")
st.caption(
    "출처: 🇰🇷 어세스타(Assesta, 2023) · 🇺🇸 Myers-Briggs Foundation 공개 자료 · "
    "조사 방식이 달라 직접 비교엔 한계가 있어요, 참고용으로 봐주세요 😊"
)

st.divider()

# ------------------------------------------------------------
# 국가별 상위 5개 유형 데이터
# ------------------------------------------------------------
korea = pd.DataFrame({
    "MBTI": ["📋 ISTJ", "🏢 ESTJ", "🚀 ENFP", "🛡️ ISFJ", "🤝 ESFJ"],
    "비율(%)": [12.8, 12.4, 9.7, 8.3, 8.2],
})
usa = pd.DataFrame({
    "MBTI": ["🛡️ ISFJ", "🤝 ESFJ", "📋 ISTJ", "🎨 ISFP", "🏢 ESTJ"],
    "비율(%)": [13.8, 12.3, 11.6, 8.8, 8.7],
})

st.markdown("### 🇰🇷 한국 vs 🇺🇸 미국 · 상위 5개 유형")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**🇰🇷 대한민국**")
    st.bar_chart(korea.set_index("MBTI"), color="#4C6EF5")
with col2:
    st.markdown("**🇺🇸 미국**")
    st.bar_chart(usa.set_index("MBTI"), color="#F76707")

st.info(
    "🇰🇷 한국은 계획적인 **ISTJ·ESTJ**가 상위권인 반면, "
    "🇺🇸 미국은 배려심 많은 **ISFJ·ESFJ**가 상위권이에요. "
    "문화와 사회 분위기가 성격 유형 분포에도 영향을 줄 수 있답니다! 🌏"
)

st.divider()

# ------------------------------------------------------------
# 재미있는 사실: 온라인 자가검사 데이터의 함정
# ------------------------------------------------------------
st.markdown("### 🤔 그런데 잠깐, 이런 사실도 있어요!")
st.warning(
    "온라인 무료 성격검사 사이트(16Personalities 등)에서는 흥미롭게도 "
    "**INFP 유형이 거의 모든 나라에서 1위**로 나타나요! 🌈\n\n"
    "왜 그럴까요? 성격 검사 자체에 관심이 많은 사람일수록 검사를 더 많이 하는 경향이 있는데, "
    "그런 성향이 INFP와 잘 맞기 때문이라고 해요. "
    "즉, **검사에 참여한 사람들의 특성**이 결과에 영향을 줄 수 있다는 뜻이죠. 🕵️"
)

with st.expander("📚 통계를 볼 때 기억하면 좋은 점"):
    st.markdown(
        "- MBTI 통계는 **조사 기관·표본·시기**에 따라 결과가 크게 달라질 수 있어요. 🔄\n"
        "- 공식 검사(Form M 등) 데이터와 온라인 자가검사 데이터는 성격이 달라요. 🧩\n"
        "- '내 나라에 이 유형이 많다/적다'는 건 참고 정보일 뿐, "
        "여러분 개인의 강점과는 별개예요! 💪"
    )

st.page_link("app.py", label="🏠 메인으로 돌아가기", icon="🔙")
