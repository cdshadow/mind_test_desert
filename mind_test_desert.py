import streamlit as st

# 기본값으로 선택할 수 있는 옵션 추가
option = st.radio(
    '당신은 지금 5마리의 동물과 사막을 걷고있습니다. 그런데 가다보니, 너무 지치고 힘들어서 5마리 중 한마리 버려야 한다면, 어떤 동물을 제일 먼저 버리겠습니까?',
    ['선택하세요', '사자', '말', '소', '양', '원숭이']
)

# 각 옵션에 대한 설명
descriptions = {
    '사자': '당신이 가장 힘들때는 일단 자존심을 포기합니다',
    '말': '당신이 가장 힘들때, 당신은 가족을 포기합니다',
    '소': '당신이 가장 힘들때, 당신은 직업을 포기합니다',
    '양': '당신이 가장 힘들때, 당신은 사랑을 포기합니다',
    '원숭이': '당신은 가장 힘들때, 친구를 포기합니다'
}

# 사용자가 '선택하세요'를 제외한 옵션을 선택했을 때만 답안 표시
if option and option != '선택하세요':
    st.text(f'당신은 {descriptions[option]}.')

