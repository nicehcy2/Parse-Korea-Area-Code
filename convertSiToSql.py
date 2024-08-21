input_filename = "법정동코드 광역시.txt"
output_filename = "법정동코드 광역시 SQL.txt"
current_date = '2024-08-21'
sidoId = 0
sigunguId = 0
region_full_name = ''

with open(input_filename, "r") as input, \
        open(output_filename, "w") as outfile:

    for line in input:

        data = line.strip().split()
        region_code = data[0]

        if len(data) >= 5:
            data[3] = data[3] + data[4]
            del data[4]

        if (len(data) >= 4):
            region_full_name = data[1] + " " + data[2] + " " + data[3]

         # 파싱된 데이터가 하나인 경우
        if len(data) == 2:
            sql = f"INSERT INTO SidoRegion VALUES ({region_code}, '{current_date}', '{current_date}', {region_code}, '{data[1]}');"
            sidoId = data[0]

        # 파싱된 데이터가 두 개인 경우
        elif len(data) == 3:
            sql = f"INSERT INTO SigunguRegion VALUES ({region_code}, '{current_date}', '{current_date}', {region_code}, '{data[2]}', {sidoId});"
            sigunguId = data[0]

        # 파싱된 데이터가 세 개인 경우
        elif len(data) == 4:
            sql = f"INSERT INTO EupmyeondongRegion VALUES ({region_code}, '{current_date}', '{current_date}', {region_code}, '{region_full_name}', '{data[3]}', {sidoId}, {sigunguId});"

        outfile.write(sql + "\n")
