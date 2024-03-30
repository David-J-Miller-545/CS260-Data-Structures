# This line makes the output go to a png file instead of to the screen
set terminal png
set output "1.png"

plot "1.out" using 1:2

set output "2.png"

plot "2.out" using 1:2
