from playwright.sync_api import sync_playwright
import time
import pandas as pd
from config import DATA_DIR, DFU_URL

# ✨ 수집 대상 설정 (쉽게 확장 가능)
target_column = 'Dungeon'  # 수집 대상: 'Dungeon', 'Character', 'Equipment' 등
nth_child = 9  # 던전: 9, 인물: 11, 새로운 항목: ?? (개발자가 수동으로 확인해서 입력)

character_list = []
df = pd.DataFrame()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto(DFU_URL)
    time.sleep(2)  # 초기 로딩 대기
    
    # 특정 섹션의 더보기 버튼만 클릭
    more_button_selector = f'#dfu-app > div > div.list > div:nth-child(2) > div.list_content > div:nth-child({nth_child}) > div.content_more'
    
    while True:
        try:
            # 해당 selector의 더보기 버튼 확인
            more_button = page.query_selector(more_button_selector)
            
            if more_button and more_button.is_visible():
                more_button.click()
                time.sleep(1.5)  # 클릭 후 로딩 대기
                print("더보기 버튼 클릭됨")
            else:
                print("더보기 버튼이 더 이상 보이지 않음")
                break
        except Exception as e:
            print(f"더보기 버튼 없음 또는 오류: {e}")
            break
    
    # 해당 섹션의 모든 데이터 수집
    print(f"데이터 수집 시작... ({target_column})")
    time.sleep(2)  # 최종 로딩 완료 대기
    
    # 해당 섹션 찾기
    base_selector = f'#dfu-app > div > div.list > div:nth-child(2) > div.list_content > div:nth-child({nth_child}) > div.content_list > div'
    # 모든 요소 찾기
    character_elements = page.query_selector_all(f'{base_selector} > a > span')
    
    for element in character_elements:
        text = element.text_content()
        if text:
            character_list.append(text.strip())
    
    print(f"총 {len(character_list)}개의 데이터 수집됨")
    
    time.sleep(1)
    browser.close()
    
# 결과 저장
# ✨ 포맷팅으로 파일명 자동 생성 (영어만 사용)
df = pd.DataFrame({target_column: character_list})
output_path = DATA_DIR / f'{target_column}_raw.xlsx'
df.to_excel(output_path, index=False)
print(f"✅ 파일 저장 완료: {output_path}")
print(df.head())