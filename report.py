import webbrowser
from plotly.offline import plot, get_plotlyjs
import plotly.graph_objs as go

fname_list=[]
lname_list=[]
name=[]

## Opens Customerdata file in read only mode
customerdata=open("customerdata.txt","r")

##Read a text file into a list
l=customerdata.read().split()
l=list(l)

##Removing the header(first row)
for i in range(0,4):
    l.pop(0)


##Split list into 5 sized chunks
new_list=[l[i:i+5] for i in range(0,len(l),5)]

##How many orders did the site receive?
def orders():
   print("\n")
   print("Total number of orders received: ",end=" ")
   print(len(new_list))


## Total amount of the orders
def totalAmount():
    total_amount=0
    for i in range(0,len(new_list)):
        total_amount = total_amount + int(new_list[i][4])
    print("Total amount of all the orders: ", end=" ")
    print(total_amount)

##Names of the customers who ordered once and did not order again
def orderedOnce():
    print("List of customers who ordered once and did not order again:")
    for i in range(0,len(new_list)):
        fname_list.append(new_list[i][2])
    for i in range(0,len(new_list)):
        lname_list.append(new_list[i][3])
    for i in range(0,len(fname_list)):
        #logic to combine first and last name.
        name.append(fname_list[i]+ ' ' +lname_list[i])
        name[i]=name[i].replace(',', '')
    oneTimeOrder=0
    twoTimeOrder=0
    threeTimeOrder=0
    fourTimeOrder=0
    fiveTimeOrder=0
    for i in range(0,len(name)):
        if name.count(name[i])==1:
            oneTimeOrder+=1
            print(name[i])

    for i in range(0,len(name)):
        if name.count(name[i])==2:
            twoTimeOrder+=1

    for i in range(0,len(name)):
        if name.count(name[i])==3:
            threeTimeOrder+=1

    for i in range(0,len(name)):
        if name.count(name[i])==4:
            fourTimeOrder+=1

    for i in range(0,len(name)):
        if name.count(name[i])>=5:
            fiveTimeOrder+=1

##Plotting the graph using Plotly
    data = [
        go.Bar(
            x=[1, 2, 3, 4, 5],
            y=[oneTimeOrder,twoTimeOrder,threeTimeOrder,fourTimeOrder,fiveTimeOrder]
        )
    ]
    layout = go.Layout(
        autosize=False,
        width=500,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        xaxis=dict(
            title='Orders',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Count of customers',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        title="<b>Distribution of Customers</b>",
       # paper_bgcolor='#7f7f7f',
        #plot_bgcolor='#c7c7c7'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = plot(fig,output_type='div',include_plotlyjs=False,show_link=False)
    html_start = """
    <html>
      <head>
         <style type="text/css">
             .plotly-graph-div { width: 50%; float: left; }
             .floatRight {width: 50%;position: absolute;top: 100px;left: 600px;}
             .container { overflow: hidden; }
         </style>
         <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
      </head>
    <body>"""
    html_end = """
       <div class="container">
             {plot_url}
           <div class="floatRight">
               <h3>Distribution of Customers</h3>
               <table border=1 cellspacing="1px">
                        <tr>
                            <th>Orders</th>
                            <th>Count of customers</th>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>{One}</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>{Two}</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>{Three}</td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>{Four}</td>
                        </tr>
                        <tr>
                            <td>5+</td>
                            <td>{FivePlus}</td>
                        </tr>
        
                </table>
            </div>
       </div>
    </body>
    </html>""".format(plotlyjs=get_plotlyjs(),plot_url=plot_url,One=oneTimeOrder,Two=twoTimeOrder,Three=threeTimeOrder,Four=fourTimeOrder,FivePlus=fiveTimeOrder)
    fileData = html_start +html_end
    writeFile = open("report.html", "w")
    writeFile.write(fileData)
    writeFile.close()

webbrowser.open("report.html")

if __name__ == '__main__':
    orders()
    totalAmount()
    orderedOnce()

customerdata.close()