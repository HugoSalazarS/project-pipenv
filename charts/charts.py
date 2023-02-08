import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C", "D", "E", "F"]
    values = [1, 24, 45, 100, 100, 3]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("Pie.png")
    plt.close()