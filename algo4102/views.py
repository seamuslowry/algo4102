from django.shortcuts import render
from .models import Board
from copy import copy, deepcopy


# 2D array to represent a blank board
blank_board = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
               [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
               [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# 2D array used to keep track of which cell can or cannot be changed
blank_sure_board = [[ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, True , True , True , True , True , True ],
               [ True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, True , True , True , True , True , True ],
               [ True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, True , True , True , True , True , True ],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False]]

# for rendering in webpage; know which tiles not to show
xnotiles1 = (9,10,11)
ynotiles1 = (0,1,2,3,4,5,15,16,17,18,19,20)
xnotiles2 = ynotiles1
ynotiles2 = xnotiles1

# numeric representations for each individual grid
TOP_LEFT = 0
TOP_RIGHT = 1
MIDDLE = 2
BOT_LEFT = 3
BOT_RIGHT = 4
NONE = -1

# what size square to go through; only valid numbers are 9 and 21
ENDVAL=21

# show the blank board
def index(request):
    context = {('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
    return render(request, 'index.html',context)

# solve and display solution
def solve(request):
    if request.method != "POST":
        return "You shouldn't be here yet"
    # copy above boards b/c python will not allow constants
    given = deepcopy(blank_board)
    sure = deepcopy(blank_sure_board)

    # parse input fields; do not take irrelvant POST fields
    for i in request.POST:
        if not i[0]=='c' and not i[0]=='i':
            rc = i.split('-')
            r = int(rc[0])
            c = int(rc[1])
            if (request.POST[i]):
                given[r][c]=int(request.POST[i])
                if (given[r][c]!=0):
                    sure[r][c]=True
            else:
                given[r][c]=0


    # solution algorithm using backtracking
    nr=0   # current row
    nc=0   # current column

    prog = True    #True is should progress; False if backtracking
    while nr < ENDVAL and nc < ENDVAL:
        # if we backtrack past the start, there is no solution
        if nr < 0 or nc < 0:
            return "No solution"
        val = given[nr][nc]

        # if the grid we are on is one of the constraints
        # simply pass it
        # go forward if we are progressing
        # go backwards if we are regressing

        if sure[nr][nc]:
            if prog:
                #PROGRESS
                tog = progress(nr,nc)
                nr = tog[0]
                nc = tog[1]
            else:
                # REGRESS
                tog = regress(nr,nc)
                nr = tog[0]
                nc = tog[1]

        # if the grid is not one of the constraints

        else:
            something_found = False # True if grid is validly filled
            # empty values are represented as 0s
            # begin at val+1 and check through 9 for a valid value
            for i in range(val+1,10):

                # if we find a valid move
                # then we set the algorithm to progress
                # DO the valid move
                # record that something was found
                # stop searching

                if valid_move(given,nr,nc,i):
                    prog = True
                    given[nr][nc]=i
                    something_found=True
                    break

            # if a valid move was completed
            # progress
            # otherwise
            # regress/backtrack

            if something_found:
                #PROGRESS
                tog = progress(nr,nc)
                nr = tog[0]
                nc = tog[1]
            else:
                prog = False
                given[nr][nc]=0
                #REGRESS
                tog = regress(nr,nc)
                nr = tog[0]
                nc = tog[1]

    # due to contraints of django, the answer is passed as a string and later parsed    
    ansstr = two_d_list_to_string(given)
    context = {('ansstr',ansstr),('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
    return render(request, 'solved.html',context)

#compute nr and nc for a progression; return the tuple of the new (nr,nc)
def progress(nr,nc):
    nr=nr+(nc+1)//ENDVAL
    nc=(nc+1)%ENDVAL
    return (nr,nc)

# compute nr and nc for a regression; return the tuple of the new (nr,nc)
def regress(nr,nc):
    if (nc == 0):
        nr = nr - 1
        nc = ENDVAL-1
    else:
        nc = nc - 1
    return(nr,nc)

# print a 2d array in a 'prettier' way; used for testing
def print_2d_array(board):
    for r in board:
        for c in r:
            print c,
        print " "

# convert the 2D array to a 'pretty' string to place in a log for testing
def str_2d_array(board):
    ret = ""
    for r in board:
        for c in r:
            if len(str(c)) == 1:
                ret =  ret + "  " + str(c)
            else:
                ret = ret + " " + str(c)
        ret = ret + "\n"
    ret = ret +"\n\n\n\n\n"
    return ret

# convert the 2D array to a string that can be parsed in the template
def two_d_list_to_string(list):
    ansstr = "test"    # need this as a buffer to account for truncate method in django filter
    for row in list:
        for col in row:
            if col >= 0:
                ansstr = ansstr + str(col)
            elif col == 0:
                ansstr = ansstr + "z"
            else:
                ansstr = ansstr + "x"
    ansstr = ansstr + "three" # need this as a buffer to account for truncate method in django filter
    return ansstr

# determine if the tile is valid (tile, not move)
def is_valid(r,c):
    return not (c in xnotiles1 and r in ynotiles1 or c in xnotiles2 and r in ynotiles2)

# determine if the move is valid on the board; this is the larger board
def valid_move(board,r,c,val):
    # first, detemrine which board(s) the tile is on
    bi_s = determine_boards_or_invalid(r,c)
    # ensure the value falls within the accepted range
    final_validity = val <= 9 and val >=1
    # return false if the move goes to an invalid tile
    if -1 in bi_s:
        return False
    #for every board the tile is in
    for bi in bi_s:
        # get the smaller 9x9 board
        b = get_board(board, bi)
        # get the normalized (0-9) indices for the new board
        newr = convert_r_for_board(bi,r)
        newc = convert_c_for_board(bi,c)
        # determine if the move is valid for that board
        # logical AND all the validities together; move must be valid for all
        final_validity = final_validity and reg_val(b,newr,newc,val)
    return final_validity

# determine normalized row for each board
def convert_r_for_board(board_index,r):
    r_offset = {
        TOP_LEFT:0,
        TOP_RIGHT:0,
        MIDDLE:6,
        BOT_LEFT:12,
        BOT_RIGHT:12,
    }
    return r-r_offset.get(board_index,0)

#determine normalized column for each board
def convert_c_for_board(board_index,c):
    c_offset = {
        TOP_LEFT:0,
        TOP_RIGHT:12,
        MIDDLE:6,
        BOT_LEFT:0,
        BOT_RIGHT:12,
    }
    return c - c_offset.get(board_index,0)

# validate for a 9x9 board
# row, column, and block must all be valid
def reg_val(board,r,c,val):
    return reg_row_val(board,r,val) and reg_col_val(board,c,val) and reg_blk_val(board,r,c,val)

# return true if move is valid within the row
def reg_row_val(board,r,val):
    return val not in board[r]

# return true if move is valid within the column
def reg_col_val(board,c,val):
    for r in range(9):
        if board[r][c]==val:
            return False;
    return True

# return true if move is valid with the block
def reg_blk_val(board,r,c,val):
    base_r = r//3*3
    base_c = c//3*3
    for test_r in range(base_r,base_r+3):
        for test_c in range(base_c,base_c+3):
            if board[test_r][test_c]==val:
                return False
    return True

# find the correct board(s) given the row and column
def determine_boards_or_invalid(r,c):
    if not is_valid(r,c):
        return [NONE]
    ret = []
    if c < 9 and r < 9:
        ret.append(TOP_LEFT)
    if c > 11 and r < 9:
        ret.append(TOP_RIGHT)
    if c > 11 and r > 11:
        ret.append(BOT_RIGHT)
    if c < 9 and r > 11:
        ret.append(BOT_LEFT) 
    if c > 5 and c < 15 and r > 5 and r < 15:
        ret.append(MIDDLE)
    return ret

# get the smaller 9x9 board (denotes from b_index) from the larger board
def get_board(board,b_index):
    if b_index==TOP_LEFT:
        return get_top_left(board)
    elif b_index==TOP_RIGHT:
        return get_top_right(board)
    elif b_index==BOT_LEFT:
        return get_bot_left(board)
    elif b_index==BOT_RIGHT:
        return get_bot_right(board)
    elif b_index==MIDDLE:
        return get_middle(board)
    else:
        return null;

# get the TOP_LEFT board from the given bigger board
def get_top_left(board): 
    ret = [[c for c in r[:9]] for r in board[:9]]
    return ret

# get the TOP_RIGHT board from the given bigger board
def get_top_right(board): 
    ret = [[c for c in r[12:]] for r in board[:9]]
    return ret

# get the BOT_RIGHT board from the given bigger board
def get_bot_right(board): 
    ret = [[c for c in r[12:]] for r in board[12:]]
    return ret

# get the BOT_LEFT board from the given bigger board
def get_bot_left(board): 
    ret = [[c for c in r[:9]] for r in board[12:]]
    return ret

# get the MIDDLE board from the given bigger board
def get_middle(board):
    ret = [[c for c in r[6:15]] for r in board[6:15]]
    return ret