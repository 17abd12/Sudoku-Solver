import tkinter as tk
    

def display_sudoku(matrix1,matrix2,text,color):




    root = tk.Tk()
    root.title("Soduku")
    canvas = tk.Canvas(root, width=380, height=500)
    canvas.pack()
    canvas.create_text(180,40,text=text,font=('Arial',15),fill = color)
    cell_width = 40  # Adjust this value to control the cell width
    cell_height = 40  # Adjust this value to control the cell height

    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            x1 = j * cell_width +10
            y1 = i * cell_height + 70
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            if matrix1[i][j] == matrix2[i][j]:
                canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(matrix1[i][j]), font=("Arial", 15),fill = 'RED')
            else:
                canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(matrix1[i][j]), font=("Arial", 15),fill = 'GREEN')

    root.mainloop()