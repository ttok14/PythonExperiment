colors = ['red', 'green', 'red', 'blue', 'red', 'blue']

first_blue = next((c for c in colors if c == 'blue'), None)


# 'red' 인 요소 전부 찾기
found = [c for c in colors if c == 'red']
print(f'Red Count {len(found)} in {colors}')

firstRedFound = next((c for c in colors if c == 'red'), None)

print(firstRedFound)
