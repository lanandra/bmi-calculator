# lanandra BMI Calculator
Calculator for Body Mass Index  

## Prerequisites  
Currently supported and tested on Linux and Windows environment.  
Also supported to run on Docker Container.  

Before use this application, please make sure you have been installed these prerequisites:
- python 3.7+. You also can create virtual environment first before running this application  
- Docker Container Runtime installed (If you want to run this application as container)

## How to Use  

### Local file  
1. Clone this repository to your local  
2. Install requirements  

    On Linux:  

        python3 -r requirements.txt  

    On Windows:  

        python -r requirements.txt  

3. Run main.py. This command will execute and run application as web server  

    On Linux:  

        python3 main.py  
    
    On Windows:  

        python main.py  

4. From your web browser access the application. Default port is 5000.  

    Example: localhost:5000  

### Run on Docker container  

1. Pull image from Docker Hub  

        docker pull lanandra/bmi-calculator  

2. Run container  

   Example: You can run this container on detached mode and run on default port 5000

        docker run -d -p 5000:5000 --name bmi-calculator lanandra/bmi-calculator:latest  

### For CLI Junkie  

1. You can run bmi.py to run application on Command Line Interface  

    On Linux  

        python3 bmi.py  

    On Windows  

        python bmi.py