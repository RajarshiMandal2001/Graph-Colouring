def make_graph(colour_assigned,connection_matrix):
    import networkx as n
    from matplotlib import pyplot as plt
    g = n.Graph()
    #[1000,1001,1002,100,1003]   1000 and 100 are same colour similarly 1003 = 103

    #changing the colours value since graph plot will not allow same values .so making rest of color 1000 to 1000.1,1000.2 ....so on
    for i in range(len(colour_assigned)):
        for j in range(i+1,len(colour_assigned)):
            if colour_assigned[j] == colour_assigned[i]:
                colour_assigned[j]+=0.1
    x,y=1,1
    f=0
    for colour in colour_assigned:
        if y==3:
            x+=1
            f=1
        g.add_node(colour,pos=(x,y))
        if f:
            y=1
            x+=1
            f=0
            continue
        y+=1

    for i in range(len(colour_assigned)):
        for j in range(i+1,len(colour_assigned)):
            if connection_matrix[i][j] == 1:
                g.add_edge(colour_assigned[i],colour_assigned[j])

    pos=n.get_node_attributes(g,"pos")
    n.draw_networkx(g,pos) 
    plt.show()




def assign_a_colour(j):
    global s
    global chromatic_no
    c = 0
    colours_assigned[j] = colour
    while c < len(colours_assigned):
        print("colour_assigned_matrix=",colours_assigned)
        if colours_assigned[j] == colours_assigned[c] and c != j:  # if matching colour already assigned to any node
            print("matching colour (",colours_assigned[c],") found at position ",c,"which is of node ",c)
            if connection_matrix[c][j] == 1 or connection_matrix[j][c] == 1: # check that if the two nodes has connection or not
                print("since connection exists between ",c,"and ",j)
                new_colour = colours_assigned[j] + 1
                colours_assigned[j] = new_colour
                print("new minimum colour assigned for node ",j,"= ",colours_assigned[j],"and made c=0")
                c = 0
                continue
        c += 1
        print("c=",c)
    s = set(colours_assigned)
    chromatic_no = len(s)
    if -1 in s:
        chromatic_no-=1
    print("till now chromatic no. of graph=",chromatic_no)
    
# NUMBERING OF GRAPH MAY EFFECT THE CHROMATIC NUMBER !!!!! 
chromatic_no = 0
s = {}
colour = 1000
colours = [1000] #keeps track of how many colours have been used till now
colours_assigned = [1000]
n = int(input("Enter the number of vertices:"))
for _ in range(n-1):
    colours_assigned.append(-1)
connection_matrix = [[0 for j in range(n)] for i in range(n)]
edges = int(input("Enter how many edges(3->4 and 4->3 counts a single edge):"))
for _ in range(edges):
    e = int(input("Enter edge(hint: 34 or 43):"))
    row = e//10
    col = e%10
    connection_matrix[row][col] = 1
    connection_matrix[col][row] = 1

for i in range(n):
    print(connection_matrix[i])
    print("\n")
# connection_matrix = [[0,1,1,0,0],
#                         [1,0,1,1,0],
#                         [1,1,0,0,1],
#                         [0,1,0,0,1],
#                         [0,1,1,1,0]]
                    # [[0,1,0,1,1,0,0,0],
                    # [1,0,1,0,0,1,0,0],
                    # [0,1,0,1,0,0,1,0],
                    # [1,0,1,0,0,0,0,1],
                    # [1,0,0,0,0,1,1,0],
                    # [0,1,0,0,1,0,0,0],
                    # [0,0,1,0,1,0,0,1],
                    # [0,0,0,1,0,0,1,0]]    
                    


for i in range(n-1):
    for j in range(i+1,n):
        if connection_matrix[i][j] == 1 and colours_assigned[j] == -1:
            print("currrent node=",i," j=",j)
            assign_a_colour(j)
print("program terminated. chromatic no.=",chromatic_no)
make_graph(colours_assigned,connection_matrix)