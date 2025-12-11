# df-quiz

던파(Dungeon Fighter Universe) 게임 인물 이름 초성 퀴즈 데이터셋 만들기기

## 🎯 목적

던파 IP의 게임 데이터들을 대상으로 초성 퀴즈 데이터로 변환(수집, 정제, 저장)

## 📊 주요 기능

- **웹 크롤링**: Playwright를 활용한 [🌐DFU 포털 데이터🌐](https://www.dnf-universe.com/stories "DFU 사이트") 수집 
- **데이터 정제**: 한자, 특수문자 처리 및 조건별 분류
- **한글 NLP**: 초성 추출 (hangul_utils 활용)
- **데이터 관리**: pandas를 통한 Excel 기반 데이터 처리

## 📁 프로젝트 구조
```
df-quiz/
│   .gitignore
│   config.py
│   README.md
│
├───📁code
│       DF_DFU_Character.py # Playwright 크롤링
│       DF_text_condition_classification.py # 데이터 정제 및 분류
│       DF_init_consonants.py # 초성 추가
│
└───📁data
        DF_DFU_Character_Raw.xlsx
        DF_DFU_Character_classified.xlsx
        DF_DFU_Character_classified_init_consonants.xlsx ✅

        DF_DFU_Dungeon_Raw.xlsx
        DF_DFU_Dungeon_classified.xlsx
        DF_DFU_Dungeon_classified_init_consonants.xlsx ✅
```

## 🛠 기술 스택

- **Python 3.12**
- **Playwright**: 웹 크롤링 (JavaScript 렌더링 대응)
- **pandas**: 데이터 처리
- **openpyxl**: Excel 파일 조작
- **hangul_utils**: 한글 초성 추출

## 📈 데이터 현황

- 총 996명 인물 데이터, 276개 던전명 데이터
- 조건별 분류:
  - cond1: 한자만 포함
  - cond2: 특수문자만 포함
  - cond3: 한자 + 특수문자
  - cond4: 깨끗한 데이터

## 🚀 사용 방법

<details>
<summary><b>📋 순서대로 사용하기 (클릭하여 펼치기)</b></summary>

### 1단계: 저장소 클론
```bash
git clone https://github.com/minjoyeee/df-quiz.git
cd df-quiz
```

### 2단계: 가상 환경 생성 및 활성화(선택)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3단계: 패키지 설치
```bash
pip install -r requirements.txt
# 또는
pip install pandas openpyxl playwright hangul-utils
playwright install
```

### 4단계: 순서대로 코드 실행
```bash
# 1. 데이터 크롤링
python code/DF_DFU_Character.py

# 2. 데이터 정제 및 분류
python code/DF_text_condition_classification.py

# 3. 초성 추출
python code/DF_init_consonants.py
```

### 5단계: 결과 확인
`data/` 폴더에서 최종 파일 확인:
- ✅ `DF_DFU_Character_classified_init_consonants.xlsx`
- ✅ `DF_DFU_Dungeon_classified_init_consonants.xlsx`

</details>

<details>
<summary><b>⚙️ 경로 설정 (config.py 사용)</b></summary>

이 프로젝트는 **config.py**로 모든 경로를 자동 관리합니다. 따라서 누가 받든 경로 수정 없이 바로 실행 가능합니다.

### config.py의 역할

```python
# config.py에서 자동으로 설정됨
PROJECT_ROOT = Path(__file__).parent.absolute()  # 프로젝트 경로 자동 계산
DATA_DIR = PROJECT_ROOT / 'data'                 # data 폴더 경로
```

### 파일명은 코드에서 동적으로 생성

```python
# target_column 변수에 따라 파일명 자동 생성
target_column = 'dungeon'  # 또는 'character', 'equipment' 등

# 1단계: 크롤링
output_path = DATA_DIR / f'{target_column}_raw.xlsx'

# 2단계: 정제
input_path = DATA_DIR / f'{target_column}_raw.xlsx'
output_path = DATA_DIR / f'{target_column}_classified.xlsx'

# 3단계: 초성 추출
input_path = DATA_DIR / f'{target_column}_classified.xlsx'
output_path = DATA_DIR / f'{target_column}_classified_init_consonants.xlsx'
```

### 각 코드에서 사용 방법

```python
# ❌ 이전 (절대경로 - 불편)
df = pd.read_excel('C:\\Users\\Yourname\\Desktop\\...\\dungeon_raw.xlsx')

# ✅ 이후 (config.py 사용 - 자동)
from config import DATA_DIR
output_path = DATA_DIR / f'{target_column}_raw.xlsx'
df.to_excel(output_path, index=False)
```

**장점:**
- GitHub에서 받은 사람도 바로 실행 가능
- `target_column` 변수만 바꾸면 자동으로 파일명 변경
- 새로운 항목 추가 시 코드 수정 최소화
- 전문적인 프로젝트 구조

</details>


## 📝 개발 계획

- [ ] 퀴즈 주제 추가
- [ ] 장비 사전 엔드포인트 추가
- [ ] ~~점수 시스템 및 랭킹~~

## 🔍 주의사항

- 띄어쓰기가 초성에 반영됨
- 한자는 원본 그대로 유지됨
- 데이터는 웹 크롤링으로 수집되므로 주기적 업데이트 필요

## 📄 라이선스

minjoyeee