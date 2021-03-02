# CentralityApp

### Python Tkinter application to generate network centrality measures of institutional investors.


This application imports institutional holdings data and creates investor level network centrality measurements. 
When two investors hold a financial interest in the same firm, the aligned financial interests could connect both investors,
creating a network. Network centrality measures are often used as a proxy for agent superiority, therefore, an investor level
centrality measure could be useful within the domain of empirical finance literature. By default, the appliation exports both 
an adjacency matrix, and an edge list from the imported holdings data.


First import the data with the button labeled "Import". The input file must be in CSV format. 
Then the necessary column names must be defined. Write the column name that represents the investor indentifier, the firm
identifier, and lastly, the amount invested. Finally, check the respective box for each desired centrality measurement and
click "Run". The exporting process could take a couple minutes, so it is best not to manipulate the window until it is finished
with the files. The output files will be created in the same directory as the application file (CentralityApp.py).


This application relies heavily on the NetworkX python library. Details on the calculation of each centrality measurement can
be found within the NetworkX documentation at https://networkx.org/.


CentralityApp.py is the main application file.
GraphGenerator.py handles making the edge lists and converts them into NetworkX graph objects.
Centrality.py contains the functions that return arrays of the centrality measures.
