# bloguide
코딩잔향: 블로가이드 (bloguie) 프로젝트
- 네이버 블로그 게시글을 마크다운으로 추출하는 내용을 포함해 마크다운 텍스트를 분석하는 분석기 API 프로젝트입니다.
- Elasticsearch를 활용한 마크다운 텍스트 분석 내용을 포함합니다.
- 텍스트 데이터에서 인사이트를 얻을 수 있도록 ES 검색/통계, 연관 분석 내용을 포함합니다.
- 블로그 운영 및 외부 사용자에게 유용한 도구를 제공합니다.
- 일부 외부 공개용 API를 제공합니다.

## 주요 기능
- 네이버 게시글 -> 마크다운 포팅
- ES 분석기 마크다운 블로그 게시글 적용
- LLM 기반 게시글 분석
- 이메일 알림
- Third Party tools
- API 관리 기능

## 개발 환경
- Linux Ubuntu 22.04 (선택 사항, 테스트 DB 구성용)
    - VirutalBox 6.1
    - Docker & Docker Compose

- Python 3.10.6
    - FastAPI (ver. 0.110.2)
    - uvicorn==0.30.1

## 기능 명세
<to-do>

## 환경 구성
### VM 설정
1. virtualbox install
2. vagrant install
3. vagrant up

### Elasticsearch
- .env (common)
<pre>
# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=

# Version of Elastic products
STACK_VERSION=8.11.1

# Set the cluster name
CLUSTER_NAME=docker-cluster

# Set to 'basic' or 'trial' to automatically start the 30-day trial
LICENSE=basic

# Port to expose Elasticsearch HTTP API to the host
ES_PORT=9200

# Port to expose Kibana to the host
KIBANA_PORT=5601

# Increase or decrease based on the available host memory (in bytes)
MEM_LIMIT=1073741824

# Project namespace (defaults to the current folder name if not set)
# COMPOSE_PROJECT_NAME=myproject
</pre>

- DB만
<pre>
docker-compose -f docker-compose-db.yml up -d --build
docker-compose -f docker-compose-db.yml down
</pre>

- 서비스 시작
<pre>
docker-compose -f docker-compose-dev|prod.yml up -d --build
docker-compose -f docker-compose-dev|prod.yml down
</pre>
