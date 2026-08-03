import streamlit as st
import random

st.set_page_config(page_title="MBTI 티니핑 찾기", page_icon="💖", layout="centered")

# ---------- 귀여운 스타일 ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FFE6F2 0%, #E6F2FF 100%);
}
.title-box {
    text-align: center;
    padding: 20px;
}
.result-card {
    background-color: white;
    border-radius: 25px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(255, 150, 200, 0.4);
    border: 3px solid #FFB6D9;
    margin-top: 20px;
}
.ping-name {
    font-size: 40px;
    font-weight: 900;
    color: #FF69B4;
}
.ping-desc {
    font-size: 18px;
    color: #555;
    margin-top: 10px;
    line-height: 1.6;
}
.ping-emoji {
    font-size: 70px;
}
</style>
""", unsafe_allow_html=True)

# ---------- MBTI별 티니핑 매칭 데이터 ----------
mbti_data = {
    "ISTJ": {"name": "차칸핑", "emoji": "📘", "desc": "성실하고 규칙을 잘 지키는 당신! 무엇이든 계획대로 착착 해내는 든든한 친구예요."},
    "ISFJ": {"name": "다정핑", "emoji": "🌷", "desc": "주변 사람들을 세심하게 챙기는 따뜻한 마음의 소유자! 늘 곁에서 힘이 되어줘요."},
    "INFJ": {"name": "마음핑", "emoji": "🌙", "desc": "깊은 생각과 따뜻한 공감 능력을 가진 신비로운 친구! 진심을 알아주는 사이예요."},
    "INTJ": {"name": "지혜핑", "emoji": "🔮", "desc": "똑똑하고 계획적인 전략가! 항상 한 발 앞서 생각하는 멋진 친구예요."},
    "ISTP": {"name": "손재주핑", "emoji": "🔧", "desc": "손끝이 야무지고 문제 해결을 좋아하는 실속파! 뭐든 척척 만들어내요."},
    "ISFP": {"name": "몽글핑", "emoji": "🎨", "desc": "감성 충만! 예쁜 것과 조용한 시간을 사랑하는 예술가 기질의 친구예요."},
    "INFP": {"name": "몽상핑", "emoji": "✨", "desc": "상상력이 풍부하고 순수한 마음을 가진 몽환적인 친구! 세상을 아름답게 봐요."},
    "INTP": {"name": "궁금핑", "emoji": "🧩", "desc": "호기심 대장! 궁금한 건 끝까지 파고드는 똑똑한 탐구자예요."},
    "ESTP": {"name": "신나핑", "emoji": "⚡", "desc": "에너지 넘치고 모험을 즐기는 액티비티 최강자! 함께 있으면 심심할 틈이 없어요."},
    "ESFP": {"name": "반짝핑", "emoji": "🌟", "desc": "무대 체질! 밝은 에너지로 주변을 환하게 만드는 인기쟁이 친구예요."},
    "ENFP": {"name": "두근핑", "emoji": "💗", "desc": "열정 가득! 새로운 사람과 아이디어에 항상 설레는 자유로운 영혼이에요."},
    "ENTP": {"name": "아이디어핑", "emoji": "💡", "desc": "재치 넘치고 새로운 걸 시도하는 걸 좋아하는 발명가 스타일 친구예요."},
    "ESTJ": {"name": "야무핑", "emoji": "📋", "desc": "리더십 만점! 조직적이고 책임감 있게 무엇이든 이끌어가는 친구예요."},
    "ESFJ": {"name": "사랑핑", "emoji": "💕", "desc": "따뜻하고 사교적인 인기만점 친구! 모두를 챙기는 다정한 분위기 메이커예요."},
    "ENFJ": {"name": "나눔핑", "emoji": "🤝", "desc": "사람들을 이끌고 격려하는 따뜻한 카리스마! 모두의 힘이 되어주는 친구예요."},
    "ENTJ": {"name": "당당핑", "emoji": "👑", "desc": "타고난 리더! 목표를 향해 자신감 있게 나아가는 강력한 카리스마의 소유자예요."},
}

# ---------- 메인 화면 ----------
st.markdown("<div class='title-box'><h1>💖 나에게 맞는 티니핑은? 💖</h1><p>MBTI를 선택하면 나와 찰떡궁합인 티니핑을 알려드려요!</p></div>", unsafe_allow_html=True)

mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요 👇", mbti_list)

if st.button("✨ 나의 티니핑 찾기 ✨", use_container_width=True):
    result = mbti_data[selected_mbti]
    st.markdown(f"""
    <div class='result-card'>
        <div class='ping-emoji'>{result['emoji']}</div>
        <div class='ping-name'>{result['name']}</div>
        <div class='ping-desc'><b>{selected_mbti}</b> 유형인 당신과 어울리는 티니핑이에요!<br><br>{result['desc']}</div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

st.markdown("<br><p style='text-align:center; color:#999; font-size:12px;'>Made with 💖 by Streamlit</p>", unsafe_allow_html=True)
