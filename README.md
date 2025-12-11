# df-quiz

던파(Dungeon Fighter Universe) 게임 인물 이름 초성 퀴즈 데이터셋 및 게임 개발 프로젝트

## 🎯 목적

던파 IP의 게임 인물들을 대상으로 초성 퀴즈 데이터를 수집, 정제, 분석하여 퀴즈 게임 엔진 개발

## 📊 주요 기능

- **웹 크롤링**: Playwright를 활용한 DFU 포털 데이터 수집
- **데이터 정제**: 한자, 특수문자 처리 및 조건별 분류
- **한글 NLP**: 초성 추출 (hangul_utils 활용)
- **데이터 관리**: pandas를 통한 Excel 기반 데이터 처리

## 📁 프로젝트 구조
```
df-quiz/
│   .gitignore
│   README.md
│
├───📁code
│       DF_DFU_Character.py # Playwright 크롤링
│       DF_text_condition_classification.py # 데이터 정제 및 분류
│       DF_init_consonants.py # 초성 추가
│
└───📁data
        DF_DFU_Character.xlsx
        DF_DFU_Character_classified.xlsx
        DF_DFU_Character_classified_init_consonants.xlsx ✅

        DF_DFU_Dungeon.xlsx
        DF_DFU_Dungeon_classified.xlsx
        DF_DFU_Dungeon_classified_init_consonants.xlsx ✅


## 🛠 기술 스택

- **Python 3.12
- **Playwright**: 웹 크롤링 (JavaScript 렌더링 대응)
- **pandas**: 데이터 처리
- **openpyxl**: Excel 파일 조작
- **hangul_utils**: 한글 초성 추출

## 📈 데이터 현황

- 총 996명 인물 데이터, 276개 던전명 데이터터
- 조건별 분류:
  - cond1: 한자만 포함
  - cond2: 특수문자만 포함
  - cond3: 한자 + 특수문자
  - cond4: 깨끗한 데이터

## 🚀 사용 방법
* 순서대로 사용용
1. DF_DFU_Character.py
2. DF_text_condition_classification.py
3. DF_init_consonants.py


## 📝 개발 계획
```markdown
- [ ] 퀴즈 주제 추가
~~ - [ ] 점수 시스템 및 랭킹 ~~
```

## 🔍 주의사항

- 띄어쓰기가 초성에 반영됨
- 한자는 원본 그대로 유지됨
- 데이터는 웹 크롤링으로 수집되므로 주기적 업데이트 필요

## 📄 라이선스

MIT