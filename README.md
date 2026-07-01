# Terraform을 이용한 AWS 인프라 자동화

웹 콘솔을 통한 반복적인 수동 설정의 휴먼 에러를 방지하고 인프라의 재사용성 확보를 위한 전체 아키텍처 코드화

---

## 🏗 Architecture
[ GitHub Repository ]
│
▼
[ HCP Terraform ]
│
▼
[ AWS Provider ]
/       
[ VPC ]   [ ALB ]
│         │
[ EC2 ]   [ Auto Scaling ]
│
[ RDS (MariaDB) ]

---

## 🛠 Tech Stack

`Terraform` `HCP Terraform` `GitHub` `AWS CLI` `Nginx` `Amazon RDS (MariaDB)`

---

## 📌 주요 구현 내용

### 1. 선언적 인프라 자동화
- AWS 핵심 리소스 전체를 Terraform 코드로 정의
- Public/Private 서브넷 구조 기반 VPC, ALB, Auto Scaling, RDS 코드화

### 2. CI/CD 파이프라인 구성
- HCP Terraform과 GitHub 연동으로 코드 변경 시 자동 배포
- 수동 콘솔 작업 없이 CLI 프로비저닝으로 배포 자동화

### 3. 재사용성 확보
- 동일 아키텍처를 반복 재현 가능한 구조 확립
- 수동 콘솔 대비 배포 시간 단축 및 휴먼 에러 방지

---

## 👤 담당 역할

| 구분 | 내용 |
|---|---|
| 팀 프로젝트 | Terraform 코드 리뷰 및 검증 담당. 팀원들이 작성한 코드의 오류 여부 확인 및 배포 전 사전 검토 수행 |
| 독립 재구현 | VPC, ALB, Auto Scaling, RDS를 포함한 AWS 전체 인프라 리소스를 Terraform으로 혼자 처음부터 단독 설계 및 작성 |

---

## 🔧 주요 코드 구조
.
├── main.tf          # 메인 리소스 정의
├── variables.tf     # 변수 선언
├── outputs.tf       # 출력값 정의
├── vpc.tf           # VPC 및 서브넷 구성
├── ec2.tf           # EC2 인스턴스 구성
├── alb.tf           # ALB 구성
├── rds.tf           # RDS 구성
└── autoscaling.tf   # Auto Scaling 구성

## Python 스크립팅

`plan_summary.py`는 `terraform plan` 결과를 파싱해서 생성/변경/교체/삭제될 리소스를 종류별로 요약해서 보여주는 스크립트입니다. 리소스가 많아지면 plan 원본 출력이 길어져 한눈에 파악하기 어려워지는 문제를 보완하기 위해 작성했습니다.

\`\`\`
python3 plan_summary.py
\`\`\`

## 📄 발표 자료
[프로젝트 발표 자료 보기](./aws-infra-automation-terraform.pdf)
