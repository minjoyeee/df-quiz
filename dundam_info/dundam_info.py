# dundam_info

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# 시크릿 모드 설정
chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://dundam.xyz/")
time.sleep(2)

try:
    # 광고팝업 닫기
    try:
        close_button = driver.find_element(By.CLASS_NAME, "puadd-fontdown")
        close_button.click()
        time.sleep(0.3)
        print("광고팝업 닫음")
    except:
        print("광고팝업이 없거나 이미 닫혔습니다")
    
    # 검색창에 캐릭터명 입력
    search_input = driver.find_element(By.CLASS_NAME, "form-control")
    search_input.clear()
    search_input.send_keys("회사")
    
    # 서버 선택
    from selenium.webdriver.support.ui import Select
    server_select = Select(driver.find_element(By.ID, "server"))
    server_select.select_by_value("cain")
    
    # 검색 버튼 클릭
    search_button = driver.find_element(By.CLASS_NAME, "searchbutton")
    search_button.find_element(By.TAG_NAME, "button").click()
    
    time.sleep(0.3)
    print("검색 완료!")
    
    # BeautifulSoup으로 결과 파싱 (첫 번째 scon만)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    scon = soup.find('div', class_='scon')
    
    if scon:
        # 아바타 이미지 URL
        avatar_url = scon.find('div', class_='seh_abata').find('img')['src']
        
        # 게임 서버
        game_server = scon.find('div', class_='seh_sever').find('li', class_='sev').get_text(strip=True)
        
        # 직업
        job = scon.find('div', class_='seh_job').find('li', class_='sev').get_text(strip=True)
        
        # 캐릭터명 + 계정명(서버)
        seh_name = scon.find('div', class_='seh_name')
        char_name = seh_name.find('span', class_='name').get_text(strip=True)
        account_server = seh_name.find('span', class_='introd server').get_text(strip=True)
        
        # 캐릭터명과 모험단명 분리
        seh_name = scon.find('div', class_='seh_name')
        name_span = seh_name.find('span', class_='name')
        char_name = name_span.contents[0].strip()
        guild_name = seh_name.find('span', class_='introd server').get_text(strip=True)
        
        # 명성
        fame = seh_name.find('span', class_='val').get_text(strip=True)
        
        # 크리티컬 확률
        critical = scon.find('span', class_='saint-critical').get_text(strip=True)
        
        # 랭킹 (seh_stat에서)
        seh_stat = scon.find('div', class_='seh_stat')
        ranking = ""
        if seh_stat:
            stat_a = seh_stat.find('ul', class_='stat_a')
            if stat_a:
                ranking_elem = stat_a.find('span', class_='val')
                if ranking_elem:
                    ranking = ranking_elem.get_text(strip=True)
        
        # DataFrame으로 정리
        data = {
            '서버': [game_server],
            '직업': [job],
            '모험단명': [guild_name],
            '캐릭터명': [char_name],
            '명성': [fame],
            '던담딜': [ranking],
            '크리티컬': [critical],
            '아바타URL': [avatar_url],
        }
        
        df = pd.DataFrame(data)
        print("\n=== 캐릭터 정보 ===")
        print(df)
        
        # xlsx 파일로 저장
        df.to_excel('dundam_character.xlsx', index=False)
        print("\n파일 저장 완료: dundam_character.xlsx")
    else:
        print("검색 결과가 없습니다")
    
except Exception as e:
    print(f"에러: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()