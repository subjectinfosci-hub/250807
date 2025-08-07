import streamlit as st

# MBTI 데이터 (예시)
mbti_data = {
    "INTJ": {
        "직업": ["전략기획가", "데이터 과학자", "시스템 분석가"],
        "취미": ["체스", "독서", "코딩"]
    },
    "INFP": {
        "직업": ["작가", "심리상담사", "예술가"],
        "취미": ["글쓰기", "명상", "그림 그리기"]
    },
    "ENTP": {
        "직업": ["창업가", "마케팅 전략가", "변호사"],
        "취미": ["토론", "즉흥 연설", "보드게임"]
    },
    "ISFJ": {
        "직업": ["간호사", "교사", "사회복지사"],
        "취미": ["요리", "사진 정리", "가족과 시간 보내기"]
    },
    # 더 많은 유형 추가 가능
}

# 스트림릿 앱 구성
st.title("MBTI 기반 직업 및 취미 추천기")
st.write("자신의 MBTI 유형을 선택하면, 그에 맞는 직업과 취미를 추천해드려요!")

mbti_types = list(mbti_data.keys())
selected_mbti = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

if selected_mbti:
    st.subheader(f"🧠 {selected_mbti} 유형 추천")
    st.markdown("### 💼 추천 직업")
    for job in mbti_data[selected_mbti]["직업"]:
        st.write(f"- {job}")

    st.markdown("### 🎯 추천 취미")
    for hobby in mbti_data[selected_mbti]["취미"]:
        st.write(f"- {hobby}")
