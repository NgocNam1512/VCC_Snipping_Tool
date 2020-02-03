from PIL import Image

LEFT_MARGIN = 80
TOP_MARGIN = 130
RIGHT_MARGIN = 30
BOTTOM_MARGIN = 130

def VCCCrop(input):
    img = Image.open(input)
    name = input.split(".")
    # Remove top, bottom, left and right margin
    width, height = img.size
    box = (LEFT_MARGIN, TOP_MARGIN, width-RIGHT_MARGIN, height-BOTTOM_MARGIN)
    all_boards = img.crop(box)
    # all_boards.save("result2.png")
    board_width = all_boards.size[0]/3
    board_height = all_boards.size[1]/4

    # Cut to small boards
    for col in range(1, 4):
        for row in range(1, 5):
            small_box = (board_width*(col-1), board_height*(row-1), 
                board_width*col, board_height*row)
            board = all_boards.crop(small_box)
            board.save(name[0] + str((row-1)*3+col) + ".png")

if __name__ == "__main__":
    VCCCrop("test2.png")