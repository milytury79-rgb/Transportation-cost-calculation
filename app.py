
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="스마트 교통비 계산기",
    page_icon="🚌",
    layout="centered"
)

# 디자인 설정
st.markdown("""
<style>
    .main {
        background-color: #F5F8FC;
    }

    .title {
        text-align: center;
        color: #246BCE;
        font-size: 35px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 16px;
    }

    .result-box {
        background-color: #EAF3FF;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 10px;
    }

    .result-price {
        color: #246BCE;
        font-size: 32px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# 제목
st.markdown(
    '<div class="title">🚌 스마트 교통비 계산기</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">나의 한 달 교통비를 쉽고 간편하게 계산해 보세요!</div>',
    unsafe_allow_html=True
)

st.divider()

# 안내 문구
st.info("교통수단과 이용 정보를 입력하면 예상 교통비를 자동으로 계산해 줍니다.")

# 교통수단 선택
st.subheader("🚍 1. 교통수단 선택")

transport = st.selectbox(
    "이용하는 교통수단을 선택하세요.",
    ["버스", "지하철", "기타 교통수단"]
)

# 기본 요금 설정
default_fares = {
    "버스": 1500,
    "지하철": 1550,
    "기타 교통수단": 2000
}

st.caption(f"선택한 교통수단의 예시 기본 요금: {default_fares[transport]:,}원")

# 요금 입력
st.subheader("💰 2. 이용 요금 입력")

fare = st.number_input(
    "1회 이용 요금 (원)",
    min_value=0,
    value=default_fares[transport],
    step=100
)

# 이용 횟수 입력
st.subheader("📅 3. 이용 횟수 및 날짜 입력")

daily_count = st.number_input(
    "하루 이용 횟수",
    min_value=1,
    value=2,
    step=1
)

days = st.number_input(
    "한 달 동안 이용하는 일수",
    min_value=1,
    max_value=31,
    value=20,
    step=1
)

# 할인 적용
st.subheader("🎁 4. 할인 적용")

discount_check = st.checkbox("할인을 적용하겠습니다.")

discount_rate = 0

if discount_check:
    discount_rate = st.slider(
        "할인율을 선택하세요 (%)",
        min_value=0,
        max_value=100,
        value=10,
        step=5
    )

st.divider()

# 계산 버튼
if st.button("🧮 교통비 계산하기", use_container_width=True):

    # 입력값 검사
    if fare <= 0:
        st.error("1회 이용 요금은 0원보다 커야 합니다.")

    elif daily_count <= 0 or days <= 0:
        st.error("이용 횟수와 이용 일수를 확인해 주세요.")

    else:
        # 교통비 계산
        total_count = daily_count * days

        original_cost = fare * total_count

        discount_cost = original_cost * discount_rate / 100

        final_cost = original_cost - discount_cost

        daily_cost = final_cost / days

        # 결과 출력
        st.success("교통비 계산이 완료되었습니다!")

        st.subheader("📊 5. 교통비 계산 결과")

        st.write(f"**선택한 교통수단:** {transport}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "총 이용 횟수",
                f"{total_count:,}회"
            )

        with col2:
            st.metric(
                "하루 평균 교통비",
                f"{daily_cost:,.0f}원"
            )

        st.divider()

        st.write("### 💳 할인 전후 교통비 비교")

        st.metric(
            "할인 전 교통비",
            f"{original_cost:,.0f}원"
        )

        st.metric(
            "할인 금액",
            f"{discount_cost:,.0f}원",
            delta=f"-{discount_cost:,.0f}원",
            delta_color="inverse"
        )

        st.markdown(
            f"""
            <div class="result-box">
                <p>할인 후 최종 교통비</p>
                <div class="result-price">
                    {final_cost:,.0f}원
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # 한 달 예상 교통비
        st.subheader("📆 6. 한 달 예상 교통비")

        st.write(
            f"하루 {daily_count}회, 한 달 {days}일 이용할 경우"
        )

        st.success(
            f"한 달 예상 교통비는 {final_cost:,.0f}원입니다."
        )

        st.caption(
            "※ 입력한 요금과 할인율을 기준으로 계산한 예상 금액입니다."
        )

        # 계산 다시 하기
        st.divider()

        if st.button("🔄 다시 계산하기"):
            st.rerun()


# 하단 안내
st.divider()

st.caption(
    "© 스마트 교통비 계산 프로그램 | 학생들의 합리적인 용돈 관리를 위한 서비스"
)
