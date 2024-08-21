# 원본 파일에서 각 줄의 뒤에서 2칸의 문자열이 "폐지"가 아닌 줄만 새로운 파일에 저장
input_filename = "법정동코드 전체자료.txt"
output_filename = "법정동코드 전체자료_미존재 제거 버전.txt"

# 파일 입출력
with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
    for line in infile:
        # 각 줄의 공백을 제거하고 마지막 3글자 확인
        if not line.strip()[-2:] == "폐지":
            # 조건에 맞는 줄을 새로운 파일에 작성
            outfile.write(line)
