# 원본 파일에서 각 줄의 뒤에서 2칸의 문자열이 "폐지"가 아닌 줄만 새로운 파일에 저장
input_filename = "법정동코드 전체자료.txt"
output_filename = "법정동코드 전체자료_미존재 제거 버전.txt"

# 파일 입출력
with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
    for line in infile:
        # 각 줄의 공백을 제거하고 마지막 3글자 확인
        if not line.strip()[-2:] == "폐지":
            # 마지막 두 글자를 제거하고, 문자열의 양쪽 공백을 제거
            stripped_line = line.strip()
            new_line = stripped_line[:-2].strip()
            
            # 각 단어 사이의 간격을 하나의 공백으로 맞추기
            formatted_line = ' '.join(new_line.split())

            # 포맷팅된 줄을 출력 파일에 쓰기
            outfile.write(formatted_line + "\n")
