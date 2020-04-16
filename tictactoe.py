from graphics import *

#the main board
class Board:
	def __init__(self):
		self.board = []
		for i in range(3):
			self.board.append([0, 0, 0])

	def resetBoard(self):
		for i in range(3):
			for j in range(3):
				self.board[i][j] = 0
	
	#must previously check if space is occupied
	#1 means circle, 2 means X
	def move(self, i, j, player):
			self.board[i][j] = player
	
	#Checks if space is occupied
	def isOccupied(self, i, j):
		if self.board[i][j] == 0:
			return False
		else:
			return True
	
	def checkVerticalWin(self, col, player):
		for i in range(3):
			if self.board[col][i] != player:
				return False
		return True
		
	def checkHorizontalWin(self, row, player):
		for i in range(3):
			if self.board[i][row] != player:
				return False
		return True
	
	def isTie(self):
		for i in range(3):
			for j in range(3):
				if self.board[i][j] != 0:
					return False
		return True
	
	#returns 0 if no one has won, 1 if p1 wins, 2 if p2 wins, 3 if tie
	def checkVictory(self):
		for i in range(3):
			if self.checkVerticalWin(i, 1):
				return 1
			if self.checkHorizontalWin(i, 1):
				return 1
			if self.checkVerticalWin(i, 2):
				return 2
			if self.checkHorizontalWin(i, 2):
				return 2
		if self.isTie():
			return 3
		else:
			return 0
			

def drawShape(x, y, typ, win):
    if typ==1:
        p = Point(x, y)
        m = Circle(p, 50)
        m.setFill(color_rgb(0, 0, 0))
        m.draw(win)
    else:
        p1 = Point(x+30, y+30)
        p2 = Point(x-30, y-30)
        ln = Line(p1, p2)
        ln.setOutline(color_rgb(0, 0, 0))
        ln.setWidth(5)
        ln.draw(win)
        p3 = Point(x-30, y+30)
        p4 = Point(x+30, y-30)
        ln2 = Line(p3, p4)
        ln2.setOutline(color_rgb(0, 0, 0))
        ln2.setWidth(5)
        ln2.draw(win)

#1 denotes circle, 2 denotes X
#squares are denoted in order
def addShape(square, typ, win):
    if square==1:
        drawShape(125, 100, typ, win)
    elif square==2:
        drawShape(250, 100, typ, win)
    elif square==3:
        drawShape(375, 100, typ, win)
    elif square==4:
        drawShape(125, 225, typ, win)
    elif square==5:
        drawShape(250, 225, typ, win)
    elif square==6:
        drawShape(375, 225, typ, win)
    elif square==7:
        drawShape(125, 350, typ, win)
    elif square==8:
        drawShape(250, 350, typ, win)
    else:
        drawShape(375, 350, typ, win)

#Update graphics
def updateBoard(board, win):
	for i in range(3):
		for j in range(3):
			if board.board[i][j] != 0:
				addShape(i + 3*j + 1, board.board[i][j], win)

def drawBoardLine(x1, y1, x2, y2, win):
	p1 = Point(x1, y1)
	p2 = Point(x2, y2)
	ln = Line(p1, p2)
	ln.setOutline(color_rgb(0, 0, 0))
	ln.setWidth(3)
	ln.draw(win)

def drawBoard(win):
	drawBoardLine(187, 40, 187, 410, win)
	drawBoardLine(312, 40, 312, 410, win)
	drawBoardLine(65, 162, 435, 162, win)
	drawBoardLine(65, 287, 435, 287, win)

def clearWin(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def getBoardPosition(x, y):
	if(x<187):
		a = 0
	elif(x<312):
		a = 1
	else:
		a = 2
	if(y<162):
		b = 0
	elif(y<312):
		b = 1
	else:
		b = 2
	return [a, b]

#Main function
def main():
    board = Board()
    win = GraphWin("Tic Tac Toe", 500, 500, autoflush=False)
    while(True):
        clearWin(win)
        drawBoard(win)
        board.resetBoard()
        playerMove = 1
        while(True):
            while(True):
                position = win.getMouse()
                pos = getBoardPosition(position.x, position.y)
                if not(board.isOccupied(pos[0], pos[1])):
                    break
                print("Occupied Square")
            board.move(pos[0], pos[1], playerMove)
            clearWin(win)
            drawBoard(win)
            updateBoard(board, win)
            winner = board.checkVictory()
            if winner != 0:
                break
            if playerMove == 1:
                playerMove = 2
            else:
                playerMove = 1
        win.getMouse()
             

main()
	


