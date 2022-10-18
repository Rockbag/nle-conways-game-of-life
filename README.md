# Conway's Game Of Life

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively).
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or
diagonally adjacent. At each step in time, the following transitions occur:

## Rules
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Notes

This is a very naive implementation of Conway's Game of Life that you can use as the blueprint for practicing your craft.

I'd suggest to first read through the code then try it out yourself. Once you get a hang of it, try and write it yourself. Feel free to use this code as reference if you are stuck.

Start from scratch every day and set a timer for 30 minutes. Do this until you get a working solution within the allotted time.

Once you get there, try and improve the code. Or do it in another language.

## Usage

`python main.py -g 100`

You can tweak the `-g` value to run the code for different generations.

## Thank You

If you are here, it's probably because you've seen my post `Practice makes perfect` on [Next Level Engineer](https://newsletter.nextlevel.engineer). I just wanted to say thank you for
being an awesome member of the community!