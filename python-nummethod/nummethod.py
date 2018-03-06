import matplotlib.pyplot as plt
from numpy import arange,sin,cos
x = arange(0.0,6.2,0.2)
plt.plot(x,sin(x),'o-',x,cos(x),'s-')
# Plot with specified
# line and marker style
# Add label to x-axis
# Add legend in loc. 3
# Add coordinate grid
plt.xlabel('x')
plt.legend(('sine','cosine'),loc = 0)
plt.grid(True)
plt.savefig('testplot.png',format='png') # Save plot in png
                                         # format for future use
plt.show()                               # Show plot on screen
input("\nPress return to exit")
