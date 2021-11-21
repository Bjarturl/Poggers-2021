from helpers import *
import random, os, shutil


class DataParser:
    def __init__(self, save_path, chat_id):
        self.db = connect_to_database()
        self.cursor = self.db.cursor()
        self.set_save_path(save_path)
        self.chat_id = get_id_from_name(chat_id)

    def set_dates(self, min_year, max_year):
        self.min_date = f"{min_year}/01/01"
        self.max_date = f"{max_year}/12/31"

    def set_save_path(self, save_path):
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        else:
            shutil.rmtree(save_path)
            os.makedirs(save_path)
        self.save_path = save_path

    # Gives number of messages in a specific chat on a specific time interval
    def heildarfjöldi_skilaboða(self):
        self.cursor.execute(f"""
        SELECT COUNT(*)
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
        """)
        with open(f"{self.save_path}/Heildarfjöldi skilaboða.csv", "w+", encoding="utf-8") as f:
            f.write("Heildarfjöldi skilaboða\n")
            f.write(str(self.cursor.fetchone()[0]))
        f.close()

    # Gives number of photo messages in a specific chat on a specific time interval
    def heildarfjöldi_mynda(self):
        self.cursor.execute(f"""
            SELECT COUNT(*)
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            AND is_photo = 1
        """)
        with open(f"{self.save_path}/Heildarfjöldi mynda.csv", "w+", encoding="utf-8") as f:
            f.write("Heildarfjöldi mynda\n")
            f.write(str(self.cursor.fetchone()[0]))
        f.close()

    # Gives individual reaction data in a specific chat on a specific time interval
    def reactions_per_einstaklingur(self):
        self.cursor.execute(f"""
            SELECT distinct S.name, R.reaction as emoji, COUNT(R.reaction) as no_occurences
            FROM messenger_reaction R 
                JOIN messenger_message M on R.message_id = M.id
                JOIN messenger_sender S on R.sender_id = S.id
            where R.timestamp >= '{self.min_date}'
            AND R.timestamp <= '{self.max_date}' 
            AND S.name <> ''
            AND M.chat_identifier_id = '{self.chat_id}'
            GROUP BY S.name
            ORDER BY S.name, no_occurences DESC
        """)
        with open(f"{self.save_path}/Reactions per einstaklingur.csv", "w+", encoding="utf-8") as f:
            f.write("name,no_occurences,emoji\n")
            name = ""
            count = 0
            vals = []
            hearts = open("hearts.txt", "r", encoding="utf-8").read().split()
            heart = '❤'
            occ = 0
            tmp = ""

            for actor, emoji, no_occurences in self.cursor.fetchall():
                if name == "":
                    name = actor

                if name != actor:
                    if tmp and occ < int(tmp.split(",")[1]):
                        vals.append(tmp)
                    else:
                        if occ > 0:
                            vals.append(f"{name},{occ},{heart}\n")
                    random.shuffle(vals)
                    f.write("".join(vals))
                    name = actor
                    count = 0
                    tmp = ""
                    occ = 0
                    vals = []
                else:
                    count += 1
                if emoji in hearts:
                    occ += no_occurences
                if count < 8 and emoji not in hearts:
                    vals.append(f"{actor},{no_occurences},{emoji}\n")
                else:
                    if tmp == "":
                        tmp = f"{actor},{no_occurences},{emoji}\n"
            if tmp and occ < int(tmp.split(",")[1]):
                vals.append(tmp)
            else:
                if occ > 0:
                    vals.append(f"{name},{occ},{heart}\n")
            f.write("".join(vals))
        f.close()

    def fékk_flest_reactions(self):
        self.cursor.execute(f"""
        SELECT COUNT(*) as 'Count of reaction', S.name as sender
            from messenger_reaction R JOIN messenger_message M ON R.message_id = M.id
            join messenger_sender S on S.id = R.sender_id
            where R.timestamp >= '{self.min_date}' 
            AND R.timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            and S.name <> ''
            GROUP BY sender
            ORDER BY COUNT(*) DESC
        """)
        with open(f"{self.save_path}/Fékk flest reactions.csv", "w+", encoding="utf-8") as f:
            f.write("Count of reaction,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def fjöldi_skilaboða_eftir_degi(self):
        self.cursor.execute(f"""
            SELECT COUNT(*) as Skilaboð, DAYNAME(timestamp) as Day
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            GROUP BY day(timestamp)
            ORDER BY day(timestamp) 
        """)
        with open(f"{self.save_path}/Fjöldi skilaboða eftir degi.csv", "w+", encoding="utf-8") as f:
            f.write("Skilaboð,Day\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def fjöldi_skilaboða_eftir_mánuðum(self):
        self.cursor.execute(f"""
            SELECT MONTHNAME(timestamp) as Month, COUNT(*) as Skilaboð
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            GROUP BY MONTH(timestamp)
            ORDER BY Month(timestamp)
        """)
        with open(f"{self.save_path}/Fjöldi skilaboða eftir mánuðum.csv", "w+", encoding="utf-8") as f:
            f.write("Month,Skilaboð\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def fjöldi_skilaboða_eftir_tíma_dags(self):
        self.cursor.execute(f"""
            SELECT COUNT(*) as Skilaboð, hour as Klukkutími
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            GROUP BY hour
            ORDER BY hour
        """)
        with open(f"{self.save_path}/Fjöldi skilaboða eftir tíma dags.csv", "w+", encoding="utf-8") as f:
            f.write("Skilaboð,Klukkutími\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def flest_skilaboð_send(self):
        self.cursor.execute(f"""
        SELECT COUNT(*) as 'Count of message', S.name
            from messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            GROUP BY s.NAME
            ORDER BY COUNT(*) DESC
        """)
        with open(f"{self.save_path}/Flest skilaboð send.csv", "w+", encoding="utf-8") as f:
            f.write("Count of message,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def flestar_myndir_sendar(self):
        self.cursor.execute(f"""
        SELECT COUNT(*) as 'Count of message', S.name
            from messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            AND M.is_photo = 1
            GROUP BY S.NAME
            ORDER BY COUNT(*) DESC
        """)
        with open(f"{self.save_path}/Flestar myndir sendar.csv", "w+", encoding="utf-8") as f:
            f.write("Count of message,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def lengstu_skilaboðin(self):
        self.cursor.execute(f"""
            SELECT msg_len as 'Message length', S.name
            FROM messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            ORDER BY msg_len DESC
        """)
        with open(f"{self.save_path}/Lengstu skilaboðin (í orðum).csv", "w+", encoding="utf-8") as f:
            f.write("Max of msg_len,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def meðallengd_skilaboða(self):
        self.cursor.execute(f"""
        SELECT S.name, truncate(avg(cast(msg_len as float)), 2) as 'Average of msg_len' 
            FROM messenger_message M join messenger_sender S on M.sender_id = S.id
            WHERE timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            GROUP BY S.name
            ORDER BY  truncate(avg(cast(msg_len as float)), 2) DESC
        """)
        with open(f"{self.save_path}/Meðallengd skilaboða (í orðum).csv", "w+", encoding="utf-8") as f:
            f.write("sender,Average of msg_len\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},\"{str(line[1]).replace('.', ',')}\"\n")
        f.close()

    def nafnið(self):
        self.cursor.execute(f"""
            SELECT timestamp, message
            FROM messenger_message
            where message like '%named the group%'
            AND timestamp >= '{self.min_date}' 
            AND timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            ORDER BY timestamp 
        """)
        with open(f"{self.save_path}/Nafnið.csv", "w+", encoding="utf-8") as f:
            f.write("date,message\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{str(line[1])}\n")
        f.close()

    def reactaði_oftast(self):
        self.cursor.execute(f"""
            SELECT  COUNT(*) as 'Count of reaction', S.name
            from messenger_reaction R JOIN messenger_message M ON R.message_id = M.id
            join messenger_sender S ON M.sender_id = S.id
            where S.name <> ''
            AND R.timestamp >= '{self.min_date}' 
            AND R.timestamp <= '{self.max_date}'
            AND chat_identifier_id = '{self.chat_id}'
            GROUP BY S.name
            ORDER BY COUNT(*) DESC
        """)
        with open(f"{self.save_path}/Reactaði oftast.csv", "w+", encoding="utf-8") as f:
            f.write("Count of reaction,actor\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    # def vinsælustu_reactions(self):
    #     self.cursor.execute(f"""
    #         SELECT top 12 reaction collate Latin1_General_100_CI_AS_SC as emoji, COUNT(reaction) as no_occurences
    #         FROM Reaction R JOIN Message M ON R.message = M.id
    #         where R.timestamp >= '{self.min_date}' 
    #         AND R.timestamp <= '{self.max_date}'
    #         AND chat_identifier_id = '{self.chat_id}'
    #         GROUP BY reaction collate Latin1_General_100_CI_AS_SC
    #         ORDER BY no_occurences DESC
    #     """)
    #     with open(f"{self.save_path}/Vinsælustu reactions.csv", "w+", encoding="utf-8") as f:
    #         f.write("emoji,no_occurences\n")
    #         hearts = ['❤', '💗', '💖', '♥️', '💝']
    #         heart = '❤'
    #         occ = 0
    #         for line in self.cursor.fetchall():
    #             if line[0] in hearts:
    #                 occ += line[1]
    #             else:
    #                 f.write(f"{line[0]},{line[1]}\n")
    #         f.write(f"{heart},{occ}\n")
    #     f.close()

    def wordcloud(self):
        stop_words = get_stop_words()
        senders = get_senders(self.min_date, self.max_date, self.chat_id)
        f = open(f"{self.save_path}/wordcloud.csv", "w+", encoding="utf-8")
        f.write("sender,word,value\n")
        for s in senders:
            print(s)
            q = f""" 
                WITH 
                    Num1 (n) AS (SELECT 1 UNION ALL SELECT 1),
                    Num2 (n) AS (SELECT 1 FROM Num1 AS X, Num1 AS Y),
                    Num3 (n) AS (SELECT 1 FROM Num2 AS X, Num2 AS Y),
                    Num4 (n) AS (SELECT 1 FROM Num3 AS X, Num3 AS Y),
                    Nums (n) AS (SELECT ROW_NUMBER() OVER(ORDER BY n) FROM Num4),
                    Words (word) AS (
                        SELECT SUBSTRING(' ' + DESCr + ' ', n + 1,
                            CHARINDEX(' ', ' ' + DESCr + ' ', n + 1) - n - 1)
                        FROM Nums
                        JOIN (SELECT  CAST(message AS NVARCHAR(MAX)) FROM PersonalProjects.dbo.Message WHERE timestamp >= '{self.min_date}' 
                        AND timestamp <= '{self.max_date}' AND chat_identifier_id = '{self.chat_id}' {"AND sender = '" + s + "'" if s != 'Allir' else ''}) AS F(DESCr)
                        ON SUBSTRING(' ' + DESCr + ' ', n, 1 ) = ' '
                        AND n < LEN(' ' + DESCr + ' '))
                SELECT top 100 word, COUNT(*) AS value
                FROM Words
                where word not in ({stop_words})
                GROUP BY word
                ORDER BY value DESC
            """
            self.cursor.execute(q)
            for word, value in self.cursor.fetchall():
                word = word.replace('\"', '')
                f.write(f"{s},{word},{value}\n")
        f.close()

    def create_all(self, skip_wordcloud):
        print("Executing heildarfjöldi_skilaboða()...")
        self.heildarfjöldi_skilaboða()
        print("Executing heildarfjöldi_mynda()...")
        self.heildarfjöldi_mynda()
        print("Executing fjöldi_skilaboða_eftir_degi()...")
        self.fjöldi_skilaboða_eftir_degi()
        print("Executing fjöldi_skilaboða_eftir_mánuðum()...")
        self.fjöldi_skilaboða_eftir_mánuðum()
        print("Executing fjöldi_skilaboða_eftir_tíma_dags()...")
        self.fjöldi_skilaboða_eftir_tíma_dags()
        print("Executing reactions_per_einstaklingur()...")
        self.reactions_per_einstaklingur()
        print("Executing fékk_flest_reactions()...")
        self.fékk_flest_reactions()
        print("Executing flest_skilaboð_send()...")
        self.flest_skilaboð_send()
        print("Executing flestar_myndir_sendar()...")
        self.flestar_myndir_sendar()
        print("Executing lengstu_skilaboðin()...")
        self.lengstu_skilaboðin()
        print("Executing meðallengd_skilaboða()...")
        self.meðallengd_skilaboða()
        print("Executing nafnið()...")
        self.nafnið()
        # print("Executing reactaði_oftast()...")
        # self.reactaði_oftast()
        # print("Executing vinsælustu_reactions()...")
        # self.vinsælustu_reactions()
        # if not skip_wordcloud:
        #     print("Executing wordcloud()...")
        #     self.wordcloud()


    def data_by_years(self, skip_wordcloud=False):
        min_year = get_min_year(self.chat_id)
        curr_year = get_curr_year()
        save_path_root = self.save_path

        self.set_dates(min_year, curr_year)
        self.set_save_path(f'{save_path_root}/all')
        print(f"Years: {min_year} - {curr_year}")
        self.create_all(skip_wordcloud)
        # for i in range(min_year, curr_year+1):
        #     print(f"Year: {i}")
        #     self.set_dates(i, i)
        #     self.set_save_path(f'{save_path_root}/{i}')
        #     self.create_all(skip_wordcloud)