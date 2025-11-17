dar = []
with open('student_data.csv', 'r', encoding='UTF-8') as f1:
    next(f1)
    data = f1.read()
    # data = [("").join(line for line in data)]
    data = [line.strip.split('\n') line for line in data]
    print(data)
    x = data.split('\n')

# with open('student_names', 'w', encoding='UTF-8') as f2:
#f1.seek > (0)
# next(f1) skip header

print(data)