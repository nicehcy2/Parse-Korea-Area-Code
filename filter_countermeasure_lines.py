import pandas as pd

input_filename = "응급대처.xlsx"
output_filename = "응급대처 정리.txt"

# Excel 파일 읽기
df = pd.read_excel(input_filename)

for index, row in df.iterrows():
    # 첫 번째와 세 번째 열에 접근
    selected_columns = df.iloc[:, [2, 3]]

    # 데이터 출력
    print(selected_columns)
