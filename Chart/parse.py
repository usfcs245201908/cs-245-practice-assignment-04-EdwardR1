import matplotlib.pyplot as plt
def parse(fileName):
    values={"Insertion": [], "Bubble": [], "Selection": [], "Size": []}
    r = open(fileName, "r")
    for line in r:
        (insertion, bubble, selection, size) = line.split(",")
        if(parseInt(insertion) != -1):
            values["Insertion"].append(parseInt(insertion))
        if(parseInt(bubble) != -1):
            values["Bubble"].append(parseInt(bubble))
        if(parseInt(selection) != -1):
            values["Selection"].append(parseInt(selection))
        if(parseInt(size) != -1):
            values["Size"].append(parseInt(size))
    return values
        
def parseInt(string):
    try:
        return int(string)
    except ValueError:
        return -1

def graph():
    values = parse("data.csv")
    x = values["Size"]

    y1 = values["Insertion"]

    y2 = values["Bubble"]

    y3 = values["Selection"]

    plt.plot(x, y1, label="Insertion Sort")
    plt.plot(x, y2, label="Bubble Sort")
    plt.plot(x, y3, label="Selection Sort")

    plt.xlabel("Array Size")
    plt.ylabel("Time (ms)")
    plt.xlim(50000, 500000)
    plt.ylim(0, 350000)
    plt.xticks([100000, 200000, 300000, 400000, 500000])
    plt.grid(linestyle="-", linewidth=0.5)

    plt.title("Running time of each sorting algorithm")

    plt.legend()

    plt.show()


def main():
    graph()

main()