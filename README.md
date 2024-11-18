# CPU-Simulator

### Tools Used: 
* Python
* .NET

## About
For my CS3502 Operating Systems class, there are two phases. 

For Phase 1, I have tested 2 different algorithms, Round Robin and FCFS, to compare performance of speed for average CPU Waiting and Arrival Times. Using Python, I wrote scripts for each algorithm to have a look at performance and trade-offs with different sets of data. I connected these scripts to the Program.cs file that the .NET framework generates for execution, and ran the program. 


For Phase 2, I implemented a deadlock fix using a resource allocation graph for both algorithms. This logic is inside resource_allocation_graph.py, with both python scripts of the algorithms utilizing it.



[See Report Here](https://docs.google.com/document/d/1c2l6cxlio8eQtGSiJacVQWZvMLLnArs5ruE5ClLSuFI/edit?usp=sharing)



## Usage
To run this program, perform the following:

1) Clone this project into your IDE (Vs Code, IntelliJ, etc).

2) Make sure you have the [.NET Core SDK](https://dotnet.microsoft.com/en-us/download) downloaded.

3) Once this is downloaded, navigate into the /Program folder of the project using your IDE terminal.

4) Run the dotnet build command. This should generate all the .NET files needed.
  
5) Now run the dotnet run command. This will execute the Program.cs file, and you'll be able to see the output of the Python Scripts in your IDE.


