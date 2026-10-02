import mysql.connector


class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="indigo",
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL database")

        except Exception as e:
            print("Error connecting to MySQL database:", e)
            exit()

    def fetch_city_name(self):
        self.cursor.execute("""
            SELECT DISTINCT(Destination) FROM flights
            UNION
            SELECT DISTINCT(Source) FROM flights
        """)
        data = self.cursor.fetchall()

        city = []
        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self, source, destination):
        self.cursor.execute(
            """
            SELECT Airline, Route, Dep_Time, Duration, Price
            FROM flights
            WHERE Source = %s AND Destination = %s
            """,
            (source, destination),
        )
        data = self.cursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []

        self.cursor.execute("""
            SELECT Airline, COUNT(*) FROM flights
            GROUP BY Airline
        """)

        data = self.cursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        city = []
        frequency1 = []

        self.cursor.execute("""
            select source,count(*) from (select source from flights 
            union all 
            select destination from flights) as t
            group by t.source
            order by count(*) 
        """)

        data = self.cursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency1.append(item[1])

        return city, frequency1

    def daily_frequency(self):
        date = []
        frequency2 = []

        self.cursor.execute("""
            select Date_of_Journey,count(*) from flights
            group by Date_of_Journey;
        """)

        data = self.cursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency2.append(item[1])

        return date, frequency2
