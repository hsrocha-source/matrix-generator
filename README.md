# matrix-generator

The code generates matrices that abide by the following pattern:

Input 1:

00 00 00

00 01 00

Input 2:

00 00 00 00 00

00 00 01 00 00

00 01 02 01 00

Input 3:

00 00 00 00 00 00 00

00 00 00 01 00 00 00

00 00 01 02 01 00 00

00 01 02 03 02 01 00

Input 4:

00 00 00 00 00 00 00 00 00 

00 01 01 01 01 01 01 01 00 

00 01 02 02 02 02 02 01 00 

00 01 02 03 03 03 02 01 00 

00 01 02 03 04 03 02 01 00

Input n:

00 ... 00 ... 00
00 ... 01 ... 00
.             .
.             .
.             .
00 ... n ... 00

The input numbers are always two digit numbers.
The matrix has 2n+1 columns and n+1 rows.
