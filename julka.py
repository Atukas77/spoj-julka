def main():
    answers = []
    for i in range(10):
        total = int(input())
        m = int(input())
        y = (total - m) // 2
        x = total - y
        answers.append(x)
        answers.append(y)

    for i in range(0, 20, 2):
        print(answers[i])
        print(answers[i+1])

main()