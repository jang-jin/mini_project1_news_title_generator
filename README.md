# Mini Project : 뉴스 기사 헤드라인 생성 모델 구축



# 1. 데이터 수집

세계일보

KBS NEWS

The Science Times

디지털 타임스

뉴스 기사를 **IT/과학** 분야만 스크래핑

약 2010년 ~ 2020년 뉴스 제목, 본문 **27322**개 수집 



# 2. 모델 구축


## 1) LSTM with Attention + split

![attention파라미터수정X](https://user-images.githubusercontent.com/65910678/91725528-d6a83580-ebd9-11ea-8841-bcc024a0fe6c.PNG)

### 예측 결과

감염 경로 못 찾은 확진자 30%… 文 "일부 교회 몰상식·적반하장" -> 미래부 탐사 탐사 본격 추진

IT서비스 개발현장, 코로나 '시한폭탄' -> 국내 연구진 개발 5g 시대 본격 추진


## 2) LSTM with Attention + KoNLPy(Okt)

![attention형태소분석파라미터수정X](https://user-images.githubusercontent.com/65910678/91725613-f3dd0400-ebd9-11ea-808f-9fe1c4447564.PNG)

### 예측 결과

감염 경로 못 찾은 확진자 30%… 文 "일부 교회 몰상식·적반하장" -> 국내 연 구진 치매 원인 규명

IT서비스 개발현장, 코로나 '시한폭탄' -> 스마트폰 으로 코로나 19 치료 제 개발


## 3) LSTM with Attention + KoNLPy(Okt) 명사만

![attention명사만파라미터수정X](https://user-images.githubusercontent.com/65910678/91725677-0b1bf180-ebda-11ea-883f-685f644d05b7.PNG)

### 예측 결과

감염 경로 못 찾은 확진자 30%… 文 "일부 교회 몰상식·적반하장" -> 코로나 백신 개발

IT서비스 개발현장, 코로나 '시한폭탄' -> 미래부 코로나 보안 반도체 강화


## 4) LSTM with Attention + KoNLPy(Okt) 조사만 제외

![attention형태소분석조사빼고](https://user-images.githubusercontent.com/65910678/91725756-22f37580-ebda-11ea-88fc-9ae56c2b0b59.PNG)

### 예측 결과

감염 경로 못 찾은 확진자 30%… 文 "일부 교회 몰상식·적반하장" -> 바이러스 감염 원인 밝히다

IT서비스 개발현장, 코로나 '시한폭탄' -> 코로나 19 치료 제 2 배 높이다


## 5) BiLSTM with Attention + KoNLPy(Okt)

![attention+bilstm](https://user-images.githubusercontent.com/65910678/91725808-343c8200-ebda-11ea-93f4-124b6aaca87c.PNG)

### 예측 결과

감염 경로 못 찾은 확진자 30%… 文 "일부 교회 몰상식·적반하장" -> 교통 선진국 교통 선진국 교통 선진국 교통 선진국 교통 선진국

IT서비스 개발현장, 코로나 '시한폭탄' -> 감염병 위장 감염병 위장 감염병 위장 감염병 위장 감염병 위장 감염병 위장 


## 6) BiLSTM with Attention + KoNLPy(Okt) 수정

![attention+bilstm수정](https://user-images.githubusercontent.com/65910678/91725864-44ecf800-ebda-11ea-9860-8dfa05874618.PNG)

### 예측 결과

감염 경로 못 찾은 확진자 30%… 文 "일부 교회 몰상식·적반하장" -> 코로나 19 미세먼지 막다 정부 정부 건 의 3 배 높이다

IT서비스 개발현장, 코로나 '시한폭탄' -> 코로나 19 치료 제 개발 에 올해 의 혁신



# 3.결론

## 1) 데이터 부족.. / 시간과 컴퓨터 성능의 문제는..
## 2) 한국어 모델의 미래는..?
## 3) KoBERT ??, KoGPT2 ??
