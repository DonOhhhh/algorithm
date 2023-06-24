#!/bin/bash

# 변수 초기값 설정
start=1
end=1
js_file=""

# 명령 줄 인자로 '-s'로 시작 번호, '-e'로 끝 번호, '-f'로 js 파일 경로를 받습니다.
while getopts s:e:f: option; do
  case "${option}" in
  s) start=${OPTARG} ;;
  e) end=${OPTARG} ;;
  f) js_file=${OPTARG} ;;
  esac
done

# 시작 번호부터 끝 번호까지 숫자를 반복합니다.
for i in $(seq $start $end); do
  # 각 명령어의 출력을 비교하고 출력 결과를 temp_output에 저장합니다.
  diff <(cat inputs/$i | node ${js_file}) <(cat inputs/$i.a) >temp_output

  # 출력 결과를 확인하고 output 파일에 저장할 내용을 준비합니다.
  result="숫자 $i: "
  if [ -s temp_output ]; then
    result+="차이가 있습니다"
  else
    result+="동일합니다"
  fi

  # 결과를 출력합니다.
  echo "$result"
done

# 임시 파일을 제거합니다.
rm temp_output
