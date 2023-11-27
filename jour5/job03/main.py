print('Veuillez rentrer la hauteur du triangle')
height = int(input())

def draw_triangle(height):
    for i in range(height):
        espace=" " *(height - i - 1)
        if  i == 0 :
            print(espace + '/' '\\')
        elif i !=height-1:
            print(espace + "/" + " " * (i*2) + "\\" )
        else:
            print(espace + "/" + "-" * (i*2) + "\\")

draw_triangle(height)