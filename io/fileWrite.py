from pathlib import Path

# 현재 실행되는 스크립트 파일의 디렉터리
directory = Path(__file__).parent

data_folder = "dataFolder"
data_filePath = "data.txt"

# Path 클래스의 / 연산자로 path 를 결합 
fileDir = directory / data_folder
filePath = fileDir / data_filePath

print(f'filePath : {filePath}')

# filePath 가 존재하지 않으면 생성 
if not Path.exists(fileDir):
    Path.mkdir(fileDir)

# 파일 없으면 생성 
fPath = Path(filePath)
fPath.touch(exist_ok=True)

# 텍스트까지 쓰기 
fPath.write_text("홀리홀리 ~~")
