# NonogramDestroyer
This program scrapes nonograms from https://www.nonograms.org/ and solves them

SCRAPING:
1. Puzzle dimensions Row width, column height (<div class="content"> <table><tbody><tr><td>Size: 35x40</td></table></div>)
2. Column numbers
   <div class="content"><table class="nonogram_table" id="nonogram_table"><tr><td class="nmtt"><table><tbody><tr>
       tr id "nmtt" is for COLUMN numbers
       if there is a value in a <td> then it will have id="nmv0_0" or something like that. 
           First number is count from left to right so max is Row width - 1.
           Second number is count how many numbers are in column starting from 0.
           <div> inside the <tr> has the text value of the number
   </table></tbody></tr></td></tr></table></div>
3. Row numbers
   <div class="content"><table class="nonogram_table" id="nonogram_table"><tr><td class="nmtL"><table><tbody><tr>
       tr id "nmtL" is for ROW numbers
       if there is a value in a <td> then it will have id="nmh0_0" or something like that.
            First number is count how many numbers are in row starting from 0.
            Second number is count from top to bottom so max is Row width - 1.
            <div> inside the <tr> has the text value of the number
   </table></tbody></tr></td></tr></table></div>

MUST HAVE:
1. Matrix to store which columns and rows are solved
SOLVING:
1. Where columns have 1 number solve columns where number = column height of puzzle.
2. Where rows have 1 number solve rows where number = row width of puzzle.
3. Where columns have 1 number and column height / number <2 then column height - number = amount of "unknown" squares from top and bottom of the column. (Superposition of extreme positions)
4. Where rows have 1 number and row width / number <2 then row width - number = amount of "unknown" squares from left and right of the row. (Superposition of extreme positions)
5. Sum of numbers for column or row + spaces in between = column height or row width, then paint the pattern according the numbers from top to bottom or left to right.
6. Pushing off from the walls. (If in the line there is a painted square, distance from which to the left border of the crossword is less than the meaning of the first figure – than you can paint several squares on the right. For this we shall count the meaning of the first figure from the left border of the crossword – all the squares to the right from the deciphered one can be painted. The same method works for the last figure and the right border of the crossword – you can paint squares on the left from the deciphered one.)
7. Inaccessibility. (If in the line there are painted squares, which can be definitely referred to particular figures, there is an opportunity to put crosses in the squares “inaccessible” for any figures. Most often this method is used when you notice a square (or several squares) whish can refer to the first or to the last figure only.)
8. Doesn’t fit in. (There are situations when in the line there appear areas, marked by crosses, in which none of the shown figures can fit. Thus, such areas are filled with crosses. We can act the same way when this area appears at the beginning/ end of the line and the first/ last figure doesn’t fit in.)
9. Division. (In situations when there are some unpainted squares divided by an empty square it is necessary to check if it may contain a painted square – in case it contradicts figures shown in the line, the square must have a cross.)
10. Double positioning. (Sometimes there are situations when a painted square in the line can refer to two variants of positioning groups of squares only. Squares which in both variants of positioning remain empty are marked by crosses.)

Row width, column height (5x3)

    (1, 3, 1, 1, 1)
(1) (0, 1, 0, 0, 0)
(5) (1, 1, 1, 1, 1)
(1) (0, 1, 0, 0, 0)
