#!/usr/bin/env python3
"""
terraform plan 결과를 요약해서 보여주는 스크립트.
리소스가 많아지면 plan 원본 출력이 길어져서 한눈에 파악하기 어렵기 때문에,
생성/변경/교체/삭제될 리소스 개수와 이름을 간단히 정리해서 보여준다.
"""

import subprocess
import re
import sys


def run_plan():
    result = subprocess.run(
        ["terraform", "plan", "-no-color"],
        capture_output=True, text=True
    )
    if result.returncode not in (0, 1, 2):
        print("terraform plan 실행 중 오류가 발생했습니다:")
        print(result.stderr)
        sys.exit(1)
    return result.stdout


def parse_plan(output):
    create = re.findall(r'# (\S+) will be created', output)
    destroy = re.findall(r'# (\S+) will be destroyed', output)
    update = re.findall(r'# (\S+) will be updated in-place', output)
    replace = re.findall(r'# (\S+) must be replaced', output)
    return create, update, destroy, replace


def main():
    print("terraform plan 실행 중...\n")
    output = run_plan()
    create, update, destroy, replace = parse_plan(output)

    print("=" * 50)
    print("Terraform Plan 요약")
    print("=" * 50)

    print(f"생성될 리소스: {len(create)}개")
    for r in create:
        print(f"  + {r}")

    print(f"\n변경될 리소스: {len(update)}개")
    for r in update:
        print(f"  ~ {r}")

    print(f"\n교체될 리소스: {len(replace)}개")
    for r in replace:
        print(f"  ! {r}")

    print(f"\n삭제될 리소스: {len(destroy)}개")
    for r in destroy:
        print(f"  - {r}")

    print("=" * 50)

    summary = re.search(r'Plan: .*', output) or re.search(r'No changes\..*', output)
    if summary:
        print(summary.group())


if __name__ == "__main__":
    main()
