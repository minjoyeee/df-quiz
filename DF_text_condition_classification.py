import pandas as pd
import re

# 엑셀 파일 읽기
df = pd.read_excel('C:\\Users\\TWOHLINE\\Desktop\\Coupang_study\\DF_DFU_Dungeon.xlsx')

# 한자 패턴 정의
hanja_pattern = r'[\(\(][\u4E00-\u9FFF]+[\)\)]'
special_pattern = r'[,:]'

# 케이스 분류 함수
def classify_case(name):
    has_hanja = bool(re.search(hanja_pattern, name))
    has_special = bool(re.search(special_pattern, name))
    
    if has_hanja and has_special:
        return 'cond3' # 한자와 특수문자가 모두 있는 경우
    elif has_hanja:
        return 'cond1' # 한자만 있는 경우
    elif has_special:
        return 'cond2' # 특수문자만 있는 경우
    else:
        return 'cond4' # 한자와 특수문자가 모두 없는 경우

# 새 컬럼 추가
df['Condition'] = df['dungeon'].apply(classify_case)

# 결과 확인
print("=" * 60)
print("케이스별 분류 결과")
print("=" * 60)
print(df['Condition'].value_counts().sort_index())
print()

# 각 케이스별 샘플 출력
for case in ['cond1', 'cond2', 'cond3', 'cond4']:
    print(f"\n{case} 샘플:")
    print(df[df['Condition'] == case]['dungeon'].head(3).values)

# 엑셀 파일로 저장
output_path = 'C:\\Users\\TWOHLINE\\Desktop\\Coupang_study\\DF_DFU_Dungeon_classified.xlsx'
df.to_excel(output_path, index=False, sheet_name='Data')

print(f"\n✅ 파일 저장 완료: {output_path}")
print(f"전체 행 수: {len(df)}")