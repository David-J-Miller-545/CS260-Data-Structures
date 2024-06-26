# This line makes the output go to a png file instead of to the screen
set terminal png
set output "plot.png"

# This line does the plotting
plot "data.out" using 1:2, "data.out" using 1:3

# If you are working interactively, you can now say "replot" if you
# change the data file and it will re-plot the data
