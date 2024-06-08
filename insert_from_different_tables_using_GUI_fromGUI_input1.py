import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0987654321",
    database="world"
)
mycursor = mydb.cursor()

def get_city_details():
    city_name = entry.get()
    q = f"""
        SELECT city.CountryCode, city.Population, country.Name, country.Continent
        FROM city
        INNER JOIN country ON city.CountryCode = country.Code
        WHERE city.Name = '{city_name}'
    """
    mycursor.execute(q)
    myresult = mycursor.fetchall()

    if mycursor.rowcount == 0:
        theLabel.config(text="Invalid city name")
    else:
        theLabel.config(text=myresult)

# Create the main Tkinter window
root = tk.Tk()
root.title("City Details")

# Entry widget for city name
entry = tk.Entry(root)
entry.pack()

# Button to get city details
get_details_button = tk.Button(root, text="Get Details", command=get_city_details)
get_details_button.pack()

# Label to display city details
theLabel = tk.Label(root, text="")
theLabel.pack()

# Start the Tkinter event loop
root.mainloop()
