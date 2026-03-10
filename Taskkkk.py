names = []
scores = []

with open("students.txt") as f:
    for line in f:
        name, score = line.split()
        names.append(name)
        scores.append(int(score))

average = sum(scores) / len(scores)

with open("average.txt", "w") as f:
    f.write(f"Qrupun ortalama bali: {average}")

with open("kesilenler.txt", "w") as f:
    for i in range(len(scores)):
        if scores[i] < 50:
            f.write(names[i] + "\n")
