from hangul_utils import divide_hangul
import pandas as pd


df = pd.read_excel('C:\\Users\\TWOHLINE\\Desktop\\Coupang_study\\DF_DFU_Dungeon_classified.xlsx', 
                   sheet_name='Data')

def get_cho(text):
    result = []
    for char in text:
        divided = divide_hangul(char)
        if divided:
            result.append(divided[0])  # 초성만 추출
    return ''.join(result)

df['Initial_Consonants'] = df['dungeon'].apply(get_cho)

print(df['Initial_Consonants'].head(3).values)  # ㅎㄱ

df.to_excel('C:\\Users\\TWOHLINE\\Desktop\\Coupang_study\\DF_DFU_Dungeon_classified_init_consonants.xlsx', 
            index=False, 
            sheet_name='init_consonants')
