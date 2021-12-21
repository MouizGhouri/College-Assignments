class Matrix () :
    
    def __init__(self, rows, columns, matrixElements = []) :
        self.rows = rows
        self.columns = columns
        self.elements = matrixElements
    
    def getRow (self, row) :
        return [self.elements [i] for i in range (row * self.columns, (row * self.columns) + self.columns)]
    
    def getColumn (self, column) :
        return [self.elements [i] for i in range (column, len (self.elements), self.columns)]
    
    def getDimensions (self) :
        return self.rows, self.columns
    
    def getElement (self, row, column) :
        return self.elements [(self.columns * row) + (column)]
    
    def elementCount (self) :
        return self.rows * self.columns
    
    def draw (self, padding = 2) :
        
        output = ""
        symbols = []
        padding = (" " * padding)
        
        for i in range (self.rows) :
            output += "┃"
            for j in range (self.columns) :
                currentElement = str (self.getElement (i, j))
                spaces = " " * (max ([len (str (i)) for i in self.getColumn (j)]) - len (currentElement))
                newline = padding + currentElement + padding + spaces + "┃"
                output += newline
            output += "\n"
            
        symbolIndices = [n for n, i in enumerate (output.splitlines () [0]) if i == '┃' and n != 0 and n != len (output.splitlines () [0]) - 1]
        line = ('━' * (len (output.splitlines () [0]) - 2 - (self.columns - 1)))
        
        topLine = list (('┏' + line + "┓") + '\n')
        bottomLine = list ('\n' + ('┗' + line + "┛"))
        middleLines = list ("\n┣" + line + "┫\n")
        
        for i in symbolIndices :
            topLine.insert (i, '┳')
            bottomLine.insert (i + 1, '┻')
            middleLines.insert (i + 1, "╋")
            
        middleLines = (''.join (middleLines)).join (output.splitlines ())
        topLine, bottomLine = ''.join (topLine), ''.join (bottomLine)
        output = topLine + middleLines + bottomLine
        
        print (output)
        
    def __dotProduct (self, x, y) :
        return sum ([i[0] * i[1] for i in zip (x, y)])
        
    def __mul__(self, other) :
        
        resultantElements = []
        resultantMatrix = Matrix (self.rows, other.columns)

        for i in range (self.rows) :
            for j in range (other.columns) :
                resultantElements.append (self.__dotProduct (self.getRow (i), other.getColumn (j)))

        resultantMatrix.elements = resultantElements
        return resultantMatrix

matrices = []

while len (matrices) < 2 :
    
    dimensions = []
    
    while len (dimensions) < 2 :
        try :
            dimensions.append (int (input (">> %s of Matrix %d : " % (["Rows", "Columns"][len (dimensions)], (len (matrices) + 1)))))
        except:
            print ("ERROR: Enter a valid integral value.")
            continue
            
    if len (matrices) >= 1 :
        if matrices [0].columns != dimensions [0] :
            print ("\nERROR: The columns of first matrix must be equal to rows of the second matrix.\n\
                    \rDimensions of the first matrix : %d x %d\n" % (matrices [0].getDimensions ()))
            continue
    if 0 in dimensions :
        print ("\nERROR: 0 is not a valid dimension for a matrix.\n")
        continue
    
    matrices.append (Matrix (*dimensions))

print ("\n")
print ("> Matrices :")
print ("- Matrix 1 : %d x %d" % (matrices [0].getDimensions ()))
print ("- Matrix 2 : %d x %d" % (matrices [1].getDimensions ()))
    
for i in range (2) :
    matrixElements = []
    print ("\n\n>> Elements for Matrix %d" % (i + 1))
    for j in range (matrices [i].elementCount ()) :
        while True :
            try :
                matrixElements.append (int (input ("- Enter element %d (%d x %d) : " % (len (matrixElements) + 1, (len (matrixElements) // matrices [i].rows), (len (matrixElements) % matrices [i].columns)))))
                break
            except :
                print ("ERROR: Enter a valid integral value.")
                
    matrices [i].elements = matrixElements
    
print ("\n")
print ("> Matrices :\n")

print ("Matrix 1 (%d x %d)" % (matrices [0].getDimensions ()))
matrices [0].draw ()
print ()

print ("Matrix 2 (%d x %d)" % (matrices [1].getDimensions ()))
matrices [1].draw ()
print ()
    
print ("\n")

resultantMatrix = matrices [0] * matrices [1]

print ("> Product Matrix : ")

resultantMatrix.draw ()
