# Reading-Textfile
## Problem Statement
Write a program to parse this data and generate a report with the following information:

1. How many orders did the site receive? </br>
2. What was the total amount of the orders? </br>
3. List the names of the customers who ordered once and did not order again. </br>
4. Get a distribution of customers who ordered exactly once, exactly twice and so on up to 4 orders and group the rest as 5 orders and above. </br>

Orders | Count of customers
-------|-------------------
1      |
2      |
3      |
4      |
5+     |

5. Optional: Generate this report as a simple HTML page with a table. </br>
6. Optional: Add a bar graph for the information in question 4 in your HTML report. </br>

## Solution 
## File Details and Output generated:-
### 1. readtextfile.js file:-
In this file, I have created a Node.js to read text file and return the response in JSON. Code will then read the request URL and based on it, the response will be sent back. 
Steps of Execution:-
1. on the command prompt:- 
    <br> Node readtextfile.js </br>
    
2. Open any browser and enter the following URL
                     <br> http://localhost:5050 </br> 

 ![readingtextusingjavascript](https://user-images.githubusercontent.com/42746311/51076892-b48c3780-16c4-11e9-8e23-c2ac9f029aea.png)

###  2.	Generating Report: - 
I have written the python file that generates the report.
<br> Output:-</br>

![report](https://user-images.githubusercontent.com/42746311/51076849-6a0abb00-16c4-11e9-8729-efd21f1b71b9.png)

After generating the data, I have created HTML files with Python scripts, and use Python to automatically open an HTML file (“report.html”) in browser using webbrowser.
I have used plotly library to show graph in browser.



![customerdataUsingplotly](https://user-images.githubusercontent.com/42746311/51076830-2617b600-16c4-11e9-973c-5817c2ff5873.png)
