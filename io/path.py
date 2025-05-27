# 3.4 버전이상부터 추천되는 Modern 한 Path 
# 관련 조작용 라이브러리 
from pathlib import Path

# 현재 스크립트가 실행되는 디렉터리
# (부모 디렉터리가 아님)
# 예로 cmd 로 cd C:\Users\LeeYunSeon> 로
# 현재 디렉터리가 저기이고 
# python -m A/B/script.py 로 실행했다하면
# 여기서 cwd 는 여전히 C:\Users\LeeYunSeon> 임 
# 여기가 *현재 디렉터리* 임 
current_dir = Path.cwd()
print(current_dir)

# 현재 실행되고 있는 스크립트의 디렉터리
current_dir_file = Path(__file__).parent
print(current_dir_file)

# pathlib 에서 지원하는 / 를 이용한 경로 구성
# 운영체제 dependent 함. 유연성있음 . 사용 권장됨 
data_folder = "dataFolder"
data_filePath = "data.txt"
file_path = current_dir / data_folder / data_filePath

print(file_path)