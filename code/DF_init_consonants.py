from hangul_utils import divide_hangul
import pandas as pd
from config import DATA_DIR

# ✨ 처리 대상 설정 (쉽게 확장 가능)
target_column = 'Dungeon'  # 처리 대상: 'Dungeon', 'Character', 'Equipment' 등

# 입출력 파일 설정 (포맷팅으로 자동 생성)
input_path = DATA_DIR / f'DF_DFU_{target_column}_classified.xlsx'
output_path = DATA_DIR / f'DF_DFU_{target_column}_classified_init_consonants.xlsx'

# 파일 읽기
df = pd.read_excel(input_path, sheet_name='Data')

def get_cho(text):
    """각 문자의 초성 추출"""
    result = []
    for char in text:
        divided = divide_hangul(char)
        if divided:
            result.append(divided[0])  # 초성만 추출
    return ''.join(result)

# 초성 추출
df['Initial_Consonants'] = df[target_column].apply(get_cho)

print(f"✨ 초성 추출 샘플:")
print(df['Initial_Consonants'].head(5).values)

# 파일 저장
df.to_excel(output_path, 
            index=False, 
            sheet_name='init_consonants')

print(f"\n✅ 파일 저장 완료: {output_path}")
print(f"전체 행 수: {len(df)}")