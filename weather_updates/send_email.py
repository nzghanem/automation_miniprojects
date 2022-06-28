from get_data import WeatherData
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import make_msgid
import os
import re
import pathlib


class send_email():
    def __init__(self, receiver_email, msn_link, city):
        self.sender_email = "p.nezar.ghanem@gmail.com"
        self.password = "wjkeukdtdnramzxs"
        self.msn_link = msn_link
        self.dataCity = list(WeatherData(self.msn_link))
        self.receiver_email = receiver_email
        self.city = city
        self.sendto()

    def get_path(self, text):
        # to change directory to where your python files are located as when it runs auto it doesn't run from this directory
        os.chdir('/Users/nezaraboghanem/Documents/Programming/main_programming_languages/Python/projects_2022/weather_updates')
        conditions = 'conditions'  # name of the folder
        files = os.listdir(conditions)  # list of the items in the folder
        weather_condition = ""
        for condition in files:
            condition = condition.replace(".jpg", "")
            if re.search(f"({condition[0]}|{condition[0].upper()})({condition[1:]})", text):
                weather_condition = os.path.join(
                    pathlib.Path().absolute(),
                    conditions,
                    condition
                )
        return weather_condition

    def looplis(self, index, starting):
        string = ""
        for i in range(len(self.dataCity[0][index])-starting):
            if re.search("[a-z]", self.dataCity[0][index][i+starting]):
                string += "\n" + self.dataCity[0][index][i+starting] + " - "
            else:
                string += f" {self.dataCity[0][index][i+starting]}"
        return string

    def ten_day_weather(self):
        string = self.looplis(0, 5) + self.looplis(1, 3)
        data = string.split("\n")
        data = list(filter(None, data))
        return data

    def get_realfeel(self):
        return self.dataCity[1].split("\n")[1]

    def sendto(self):
        message = EmailMessage()
        message["To"] = self.receiver_email
        message["From"] = self.sender_email
        message["Subject"] = f"Today is {self.dataCity[0][0][2]} in {self.city}"
        data = self.ten_day_weather()
        attachment_cid1 = make_msgid()
        attachment_cid2 = make_msgid()
        attachment_cid3 = make_msgid()
        attachment_cid4 = make_msgid()
        attachment_cid5 = make_msgid()
        attachment_cid6 = make_msgid()
        attachment_cid7 = make_msgid()
        attachment_cid8 = make_msgid()
        attachment_cid9 = make_msgid()
        attachment_cid10 = make_msgid()

        message.set_content(f"""
            <p>
                Morning Nezar,
            </p>

            <!-- Weather Today -->
            <p style='font-family:Cavolini;font-size:30px;white-space: pre-line'>
                <img src="cid:{attachment_cid1[1:-1]}" width="50" height="50"/> Today is {self.dataCity[0][0][2].lower()} in {self.city}
                <p style="font-size:20px;margin-left:100px"><strong>Feels like:</strong> {self.get_realfeel()}</p>
                <p style="font-size:20px;margin-left:100px"><strong>Today's High:</strong> {self.dataCity[0][0][1]}</p>
                <p style="font-size:20px;margin-left:100px"><strong>Today's Low:</strong> {self.dataCity[0][0][3]}</p>
            </p>
            <!-- Weather Next Ten Days -->

            <p style='font-family:Cavolini;font-size:30px'>
                Weather Next 10 Days
                    <p style='font-family:Cavolini;font-size:22px;white-space: pre-line;margin-left:100px'>
                        <img src="cid:{attachment_cid2[1:-1]}" width="50" height="50"/> {data[0]}
                        <img src="cid:{attachment_cid3[1:-1]}" width="50" height="50"/> {data[1]}
                        <img src="cid:{attachment_cid4[1:-1]}" width="50" height="50"/> {data[2]}
                        <img src="cid:{attachment_cid5[1:-1]}" width="50" height="50"/> {data[3]}
                        <img src="cid:{attachment_cid6[1:-1]}" width="50" height="50"/> {data[4]}
                        <img src="cid:{attachment_cid7[1:-1]}" width="50" height="50"/> {data[5]}
                        <img src="cid:{attachment_cid8[1:-1]}" width="50" height="50"/> {data[6]}
                        <img src="cid:{attachment_cid9[1:-1]}" width="50" height="50"/> {data[7]}
                        <img src="cid:{attachment_cid10[1:-1]}" width="50" height="50"/> {data[8]}
                    </p>
            </p>

            <a href={self.msn_link}>Source</a>
            """, 'html')

        with open(self.get_path(self.dataCity[0][0][2]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid1)

        with open(self.get_path(self.dataCity[2][1]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid2)

        with open(self.get_path(self.dataCity[2][2]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid3)

        with open(self.get_path(self.dataCity[2][3]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid4)

        with open(self.get_path(self.dataCity[2][4]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid5)

        with open(self.get_path(self.dataCity[2][5]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid6)

        with open(self.get_path(self.dataCity[2][6]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid7)

        with open(self.get_path(self.dataCity[2][7]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid8)

        with open(self.get_path(self.dataCity[2][8]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid9)

        with open(self.get_path(self.dataCity[2][9]) + ".jpg", 'rb') as fp:
            message.add_related(
                fp.read(), 'image', 'jpg', cid=attachment_cid10)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, message.as_string())


if __name__ == "__main__":
    send_email("nz.ghanem@gmail.com", "https://www.msn.com/en-us/weather/forecast/in-Brno,South-Moravia?ocid=ansmsnweather&loc=eyJsIjoiQnJubyIsInIiOiJTb3V0aCBNb3JhdmlhIiwicjIiOiJCcm5vIC0gbcSbc3RvIiwiYyI6IkN6ZWNoaWEiLCJpIjoiQ1oiLCJnIjoiZW4tdXMiLCJ4IjoiMTYuNDkiLCJ5IjoiNDkuMjEifQ%3D%3D&weadegreetype=C", "Brno")
