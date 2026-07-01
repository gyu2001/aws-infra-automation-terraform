# Terraform을 이용한 AWS 인프라 자동화

개인 실습으로 AWS 인프라 전체(VPC, ALB, Auto Scaling, RDS)를 Terraform 코드로 먼저 구축했고, 이후 4인 팀 프로젝트에서는 Terraform 코드 리뷰와 배포 전 검증을 담당했습니다.

---

## Architecture

    [ GitHub Repository ]
             │
             ▼
      [ AWS Provider ]
             │
    ┌────────┼────────┐
    │                 │
  [ VPC ]          [ ALB ]
    │                 │
  [ EC2 ]      [ Auto Scaling ]
                       │
                  [ RDS (MariaDB) ]

---

## Tech Stack

`Terraform` `AWS CLI` `Nginx` `Amazon RDS (MariaDB)` `Python`

---

## 담당 역할

4인 팀 프로젝트에서는 Terraform 코드 리뷰와 배포 전 검증을 담당해, 팀원들이 작성한 코드의 오류를 사전에 걸러냈습니다.

---

## 구현 내용 (개인 실습)

### 1. 선언적 인프라 자동화
- AWS 핵심 리소스 전체를 Terraform 코드로 정의
- Public/Private 서브넷 구조 기반 VPC, ALB, Auto Scaling, RDS 코드화

### 2. 재사용성 확보
- `terraform apply` 한 번으로 전체 인프라를 9분 42초 내 배포하는 것까지 실제로 검증
- 동일 아키텍처를 반복 재현 가능한 구조로 구성

### 3. 배포 전 검증 자동화
- RDS 비밀번호가 평문으로 하드코딩된 것을 발견해 변수로 분리
- `terraform plan` 출력을 리소스별로 요약해주는 Python 스크립트(`plan_summary.py`) 작성

---

## 코드 구조

    .
    ├── 1. Terraform Provider.tf
    ├── 2. VPC.tf
    ├── 3. Subnet.tf
    ├── 4. IGW.tf
    ├── 5. NGW.tf
    ├── 6. RT.tf
    ├── 7. Security Group.tf
    ├── 8. Key Pair.tf
    ├── 9. EC2.tf
    ├── 10. RDS.tf
    ├── 11. S3.tf
    ├── 12. acm.tf
    ├── 13. route53.tf
    ├── 14. ALB.tf
    ├── 15. AutoScaling.tf
    ├── variables.tf
    └── plan_summary.py

---

## Python 스크립팅

`plan_summary.py`는 `terraform plan` 결과를 파싱해서 생성/변경/교체/삭제될 리소스를 종류별로 요약해서 보여주는 스크립트입니다. 리소스가 많아지면 plan 원본 출력이 길어져 한눈에 파악하기 어려워지는 문제를 보완하기 위해 작성했습니다.

    python3 plan_summary.py
