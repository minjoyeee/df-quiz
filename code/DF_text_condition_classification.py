import pandas as pd
import re
from config import DATA_DIR, PATTERNS

# ✨ 처리 대상 설정 (쉽게 확장 가능)
target_column = 'Dungeon'  # 처리 대상: 'Dungeon', 'Character', 'Equipment' 등

# 입출력 파일 설정 (포맷팅으로 자동 생성, 영어만 사용)
input_path = DATA_DIR / f'{target_column}_raw.xlsx'
output_path = DATA_DIR / f'{target_column}_classified.xlsx'

# 엑셀 파일 읽기
df = pd.read_excel(input_path)

# 패턴은 config.py에서 가져옴
hanja_pattern = PATTERNS['hanja']
special_pattern = PATTERNS['special']

# 케이스 분류 함수
def classify_case(name):
    has_hanja = bool(re.search(hanja_pattern, name))
    has_special = bool(re.search(special_pattern, name))
    
    if has_hanja and has_special:
        return 'cond3'  # 한자와 특수문자가 모두 있는 경우
    elif has_hanja:
        return 'cond1'  # 한자만 있는 경우
    elif has_special:
        return 'cond2'  # 특수문자만 있는 경우
    else:
        return 'cond4'  # 한자와 특수문자가 모두 없는 경우

# 새 컬럼 추가
df['Condition'] = df[target_column].apply(classify_case)

# 결과 확인
print("=" * 60)
print(f"케이스별 분류 결과 ({target_column})")
print("=" * 60)
print(df['Condition'].value_counts().sort_index())
print()

# 각 케이스별 샘플 출력
for case in ['cond1', 'cond2', 'cond3', 'cond4']:
    sample = df[df['Condition'] == case][target_column].head(3)
    if len(sample) > 0:
        print(f"\n{case} 샘플:")
        print(sample.values)

# 엑셀 파일로 저장
df.to_excel(output_path, index=False, sheet_name='Data')

print(f"\n✅ 파일 저장 완료: {output_path}")
print(f"전체 행 수: {len(df)}")