from tkinter import *
from kruskal import kruskal
from graph import *
import networkx as nx
import sys

root = Tk()

G = nx.empty_graph()

graph_example = {}


# label widget
def myClick():
    Label(root, text="xd").grid(row=0)


def save():
    file = open('xdd.txt', 'w')
    file.write('no hej')
    file.close()


# Funkcja wczytuje graf z pliku i zapisuje go do zmiennej globalnej graph_example.
# Przyjmuję konwencje według której graf w pliku jest zapisany w postaci m linii, a w każdej
# linii 3 liczby a, b, v oddzielone spacją. m oznacza liczbę krawędzi, a i b wierzchołki, a v
# to waga krawędzi między nimi.
# Można ewentualnie dopisać sprawdzenie poprawności formatu danych wejściowych.
def load_graph_from_file():
    D = {}  # To będzie graf który wczytamy.
    file = "Examples/example_in.txt"

    with open(file) as f:
        for line in f.readlines():
            a = line[0]
            b = line[2]
            v = line[4]
            if a not in D:
                D[a] = {}
            D[a][b] = v

    global graph_example
    graph_example = D

    return


# Bierze graf ze zmiennej globalnej graph_example, wywołuje na nim kruskala, a wynik zapisuje do pliku.
# Format zapisanych danyh taki sam jak w pliku wejściowym.
def save_kruskal_graph_to_file():
    file = "Examples/example_out.txt"
    my_graph = kruskal(graph(graph_example))
    vertices = my_graph.items()

    f = open(file, "w")  # "w" oznacza, że jeśli plik nie istniał to go stworzy, a jeśli istniał to go nadpisze.
    for v in vertices:
        edges = v[1].items()
        for e in edges:
            line = ' '.join([v[0], e[0], e[1]])
            f.write(line)
            f.write("\n")

    f.close()

    return


def end_app():
    sys.exit()


myButton1 = Button(root, text="Wczytaj graf z pliku", padx=50, pady=50, font=50, command=load_graph_from_file)
myButton2 = Button(root, text="Zapisz wynik kruskala do pliku", padx=50, pady=50, font=50,
                   command=save_kruskal_graph_to_file)
myButton3 = Button(root, text="Zakończ", padx=50, pady=50, font=50, command=end_app)
myButton1.grid(row=1)
myButton2.grid(row=2)
myButton3.grid(row=3)

# def wyswietl():
#     tajp=nx.empty_graph()
#     global G
#     if (type(G)==type(tajp)):
#         nx.draw(G)
#         plt.show()
#
#     return


# myButton3 = Button(root,text="Wyswietl",padx=p,pady=p,font=50,command=wyswietl)
# myButton3.grid(row=3)

root.mainloop()
