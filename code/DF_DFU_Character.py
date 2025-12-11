from playwright.sync_api import sync_playwright
import time
import pandas as pd

target_column = 'dungeon' # 'dungeon' or 'character' or 'etc'

character_list = []
df = pd.DataFrame()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto('https://www.dnf-universe.com/stories')
    time.sleep(2)  # 초기 로딩 대기
    
    # 특정 섹션의 더보기 버튼만 클릭
    # nth-child(11) = 인물, nth-chile(9) = 던전
    more_button_selector = '#dfu-app > div > div.list > div:nth-child(2) > div.list_content > div:nth-child(9) > div.content_more'
    
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
    
    # 해당 섹션의 모든 캐릭터 데이터 수집
    print("데이터 수집 시작...")
    time.sleep(2)  # 최종 로딩 완료 대기
    
    # 해당 섹션의 캐릭터 찾기
    # nth-child(11) = 인물, nth-chile(9) = 던전
    base_selector = '#dfu-app > div > div.list > div:nth-child(2) > div.list_content > div:nth-child(9) > div.content_list > div'
    
    # 모든 캐릭터 요소 찾기
    character_elements = page.query_selector_all(f'{base_selector} > a > span')
    
    for element in character_elements:
        text = element.text_content()
        if text:
            character_list.append(text.strip())
    
    print(f"총 {len(character_list)}개의 데이터 수집됨")
    
    time.sleep(1)
    browser.close()
    
# 결과 저장
df = pd.DataFrame({target_column: character_list})
df.to_excel(f'C:\\Users\\TWOHLINE\\Desktop\\Coupang_study\\df-quiz\\data\\DF_DFU_{target_column}.xlsx', index=False, sheet_name='Data')
print(df)