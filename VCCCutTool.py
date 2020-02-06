from PIL import Image
import os

LEFT_MARGIN = 80
TOP_MARGIN = 130
RIGHT_MARGIN = 30
BOTTOM_MARGIN = 130
ROW = 4
COLUMN = 3

def VCCCropBorder(input, left=LEFT_MARGIN, right=RIGHT_MARGIN, top=TOP_MARGIN, bottom=BOTTOM_MARGIN):
    img = Image.open(input)
    # Remove top, bottom, left and right margin
    width, height = img.size
    box = (left, top, width-right, height-bottom)
    all_boards = img.crop(box)
    all_boards.show(all_boards)


def VCCCropSmallBoard(input, row=ROW, column=COLUMN, 
                    left=LEFT_MARGIN, right=RIGHT_MARGIN, top=TOP_MARGIN, bottom=BOTTOM_MARGIN):
    img = Image.open(input)
    # Remove top, bottom, left and right margin
    width, height = img.size
    box = (left, top, width-right, height-bottom)
    all_boards = img.crop(box)
    
    board_width = all_boards.size[0]/column
    board_height = all_boards.size[1]/row

    # Cut to small boards
    name = input.split(".")[0]
    if not os.path.exists(name):
        os.makedirs(name)
    for col in range(1, column+1):
        for ro in range(1, row+1):
            small_box = (board_width*(col-1), board_height*(ro-1), 
                board_width*col, board_height*ro)
            board = all_boards.crop(small_box)
            board.save(name + "/" + name + str((ro-1)*row+col) + ".png")

if __name__ == "__main__":
    VCCCropBorder("test-1.png")
    # VCCCropSmallBoard("test-1.png", row=3, column=1)