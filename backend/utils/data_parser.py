from helpers import *
import random
import os
import shutil
import csv


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
        # else:
        #     shutil.rmtree(save_path)
        #     os.makedirs(save_path)
        self.save_path = save_path

    # Gives number of messages in a specific chat on a specific time interval
    def heildarfjöldi_skilaboða(self):
        self.cursor.execute(f"""
        SELECT COUNT(*)
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
        """)
        with open(f"{self.save_path}/heildarfjoldi_skilaboda.csv", "w+", encoding="utf-8") as f:
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
            AND is_photo = true
        """)
        with open(f"{self.save_path}/heildarfjoldi_mynda.csv", "w+", encoding="utf-8") as f:
            f.write("Heildarfjöldi mynda\n")
            f.write(str(self.cursor.fetchone()[0]))
        f.close()

    # Gives individual reaction data in a specific chat on a specific time interval
    def reactions_per_einstaklingur(self):
        self.cursor.execute(f"""
            SELECT COUNT(R.reaction) as no_occurences, S.name, R.reaction as emoji
            FROM messenger_reaction R
                JOIN messenger_message M on R.message_id = M.id
                JOIN messenger_sender S on R.sender_id = S.id
            where R.timestamp >= '{self.min_date}'
            AND R.timestamp <= '{self.max_date}'
            AND S.name <> ''
            GROUP BY S.name, R.reaction
            ORDER BY S.name, no_occurences DESC
        """)
        with open(f"{self.save_path}/reactions_per_einstaklingur.csv", "w+", encoding="utf-8") as f:
            f.write("no_occurences,name\n")
            name = ""
            count = 0
            vals = []
            hearts = open("static/hearts.txt", "r",
                          encoding="utf-8").read().split()
            heart = '❤'
            occ = 0
            tmp = ""
            for no_occurences, actor, emoji in self.cursor.fetchall():
                if name == "":
                    name = actor

                if name != actor:
                    if tmp and occ < int(tmp.split(",")[0]):
                        vals.append(tmp)
                        print(tmp)
                    else:
                        if occ > 0:
                            vals.append(f"{occ},{name} {heart}\n")
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
                    vals.append(f"{no_occurences},{actor} {emoji}\n")
                else:
                    if tmp == "":
                        tmp = f"{no_occurences},{actor} {emoji}\n"
            if tmp and occ < int(tmp.split(",")[0]):
                vals.append(tmp)
            else:
                if occ > 0:
                    vals.append(f"{occ},{name} {heart}\n")
            f.write("".join(vals))
        f.close()
        data = open(f"{self.save_path}/reactions_per_einstaklingur.csv", "r",
                    encoding="utf-8").readlines()
        people = {}
        for d in data[1:]:
            occ, name = d.split(',')
            occ = int(occ)
            name_only = ' '.join(name.split()[0:-1])
            if name_only not in people:
                people[name_only] = {
                    'occ': occ,
                    'name': name.strip(),
                }
            if occ > people[name_only]['occ']:
                people[name_only]['occ'] = occ
        with open(f"{self.save_path}/reactions_per_einstaklingur.csv", "w+", encoding="utf-8") as f:
            f.write("no_occurences,name\n")
            for p in people:
                f.write(f"{people[p]['occ']},{people[p]['name']}\n")
        f.close()

    def fékk_flest_reactions(self):
        self.cursor.execute(f"""
        SELECT COUNT(*) as "Count of reaction", S.name as sender
            from messenger_reaction R JOIN messenger_message M ON R.message_id = M.id
            join messenger_sender S on S.id = R.sender_id
            where R.timestamp >= '{self.min_date}'
            AND R.timestamp <= '{self.max_date}'
            and S.name <> ''
            GROUP BY sender
            ORDER BY COUNT(*) DESC
            LIMIT 5
        """)
        with open(f"{self.save_path}/fekk_flest_reactions.csv", "w+", encoding="utf-8") as f:
            f.write("Count of reaction,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def fjöldi_skilaboða_eftir_degi(self):
        self.cursor.execute(f"""
            SELECT COUNT(*) as Skilaboð, extract(day from timestamp) as Day
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            GROUP BY extract(day from timestamp)
            ORDER BY extract(day from timestamp)
        """)
        with open(f"{self.save_path}/fjoldi_skilaboda_eftir_degi.csv", "w+", encoding="utf-8") as f:
            f.write("Skilaboð,Dagur\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def fjöldi_skilaboða_eftir_mánuðum(self):
        self.cursor.execute(f"""
            SELECT COUNT(*) as Skilaboð,
            TO_CHAR(timestamp, 'month') AS "Month"
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            GROUP BY TO_CHAR(timestamp, 'month')
            ORDER BY TO_CHAR(timestamp, 'month')
        """)
        with open(f"{self.save_path}/fjoldi_skilaboda_eftir_manudum.csv", "w+", encoding="utf-8") as f:
            f.write("Skilaboð,Mánuður\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def fjöldi_skilaboða_eftir_tíma_dags(self):
        self.cursor.execute(f"""
            SELECT COUNT(*) as Skilaboð, hour as Klukkutími
            FROM messenger_message
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            GROUP BY hour
            ORDER BY hour
        """)
        with open(f"{self.save_path}/fjoldi_skilaboda_eftir_tima_dags.csv", "w+", encoding="utf-8") as f:
            f.write("Skilaboð,Klukkutími\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def flest_skilaboð_send(self):
        self.cursor.execute(f"""
        SELECT COUNT(*) as "Count of message", S.name
            from messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            GROUP BY s.NAME
            ORDER BY COUNT(*) DESC
            LIMIT 5
        """)
        with open(f"{self.save_path}/flest_skilabod_send.csv", "w+", encoding="utf-8") as f:
            f.write("Count of message,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def flestar_myndir_sendar(self):
        self.cursor.execute(f"""
        SELECT COUNT(*) as "Count of message", S.name
            from messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            AND M.is_photo = true
            GROUP BY S.NAME
            ORDER BY COUNT(*) DESC
            LIMIT 5
        """)
        with open(f"{self.save_path}/flestar_myndir_sendar.csv", "w+", encoding="utf-8") as f:
            f.write("Count of message,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def lengstu_skilaboðin(self):
        self.cursor.execute(f"""
            SELECT msg_len as "Message length", S.name
            FROM messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            ORDER BY msg_len DESC
            LIMIT 5
        """)
        with open(f"{self.save_path}/lengstu_skilabodin_i_ordum.csv", "w+", encoding="utf-8") as f:
            f.write("Max of msg_len,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def meðallengd_skilaboða(self):
        self.cursor.execute(f"""

               SELECT substring(cast(avg(cast(msg_len as float)) as varchar), 0, 4) as "Average of msg_len", S.name
            FROM messenger_message M join messenger_sender S on M.sender_id = S.id
                   WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'

            GROUP BY S.name
ORDER BY  avg(cast(msg_len as float)) DESC
            LIMIT 5
        """)
        with open(f"{self.save_path}/medallengd_skilaboda_i_ordum.csv", "w+", encoding="utf-8") as f:
            f.write("Average of msg_len,sender\n")
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
            ORDER BY timestamp
        """)
        with open(f"{self.save_path}/nafnid.csv", "w+", encoding="utf-8") as f:
            f.write("date,message\n")
            for line in self.cursor.fetchall():
                n = line[1].replace('\"', '\'')
                f.write(f"{line[0]},\"{n}\"\n")
        f.close()

    def reactaði_oftast(self):
        self.cursor.execute(f"""
            SELECT  COUNT(*) as "Count of reaction", S.name
            from messenger_reaction R JOIN messenger_message M ON R.message_id = M.id
            join messenger_sender S ON M.sender_id = S.id
            where S.name <> ''
            AND R.timestamp >= '{self.min_date}'
            AND R.timestamp <= '{self.max_date}'
            GROUP BY S.name
            ORDER BY COUNT(*) DESC
            LIMIT 5
        """)
        with open(f"{self.save_path}/reactadi_oftast.csv", "w+", encoding="utf-8") as f:
            f.write("Count of reaction,sender\n")
            for line in self.cursor.fetchall():
                f.write(f"{line[0]},{line[1]}\n")
        f.close()

    def get_stats(self):
        self.cursor.execute(f"""
            SELECT S.name, round(count(*) / 100, 0) as "ATK", (2500 - MAX(msg_len)) / 2500 as "ACC"
            from messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            GROUP BY s.NAME
        """)
        names = {}
        for line in self.cursor.fetchall():
            name = line[0]
            if name not in names:
                names[name] = {}
            names[name]['ATK'] = line[1]
            names[name]['ACC'] = float(line[2])

        self.cursor.execute(f"""
            SELECT S.name as sender, round(count(*) / 10, 0) as "HP"
            from messenger_reaction R JOIN messenger_message M ON R.message_id = M.id
            join messenger_sender S on S.id = R.sender_id
            where R.timestamp >= '{self.min_date}'
            AND R.timestamp <= '{self.max_date}'
            and S.name <> ''
            GROUP BY sender
            ORDER BY COUNT(*) DESC
        """)
        for line in self.cursor.fetchall():
            name = line[0]
            if name not in names:
                names[name] = {}
            names[name]['HP'] = line[1]
        self.cursor.execute(f"""
            SELECT S.name, (COUNT(*) / 20000) as "CRIT"
            from messenger_reaction R JOIN messenger_message M ON R.message_id = M.id
            join messenger_sender S ON M.sender_id = S.id
            where R.timestamp >= '{self.min_date}'
            AND R.timestamp <= '{self.max_date}'
            and S.name <> ''
            GROUP BY S.name
        """)
        for line in self.cursor.fetchall():
            name = line[0]
            if name not in names:
                names[name] = {}
            names[name]['CRIT'] = float(line[1])
        self.cursor.execute(f"""
            SELECT S.name, round((8500 - COUNT(*)) / 8500 / 3, 2) as "DEF"
            from messenger_message M JOIN messenger_sender S on S.id = M.sender_id
            WHERE timestamp >= '{self.min_date}'
            AND timestamp <= '{self.max_date}'
            AND M.is_photo = true
            GROUP BY S.NAME
        """)
        for line in self.cursor.fetchall():
            name = line[0]
            if name not in names:
                names[name] = {}
            names[name]['DEF'] = float(line[1])

        with open(f"{self.save_path}/battle_stats.csv", "w+", encoding="utf-8") as f:
            f.write("Name,ATK,ACC,HP,CRIT,DEF\n")
            for name in names:
                ATK = names[name]['ATK'] if 'ATK' in names[name] else 0
                ACC = names[name]['ACC'] if 'ACC' in names[name] else 0
                HP = names[name]['HP'] if 'HP' in names[name] else 0
                CRIT = names[name]['CRIT'] if 'CRIT' in names[name] else 0
                DEF = names[name]['DEF'] if 'DEF' in names[name] else 0
                f.write(
                    f"{name},{ATK},{ACC},{HP},{CRIT},{DEF}\n")
        f.close()

    def create_all(self):
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
        print("Executing reactaði_oftast()...")
        self.reactaði_oftast()
        print("Executing get_stats()...")
        self.get_stats()

    def data_by_years(self):
        min_year = get_min_year(self.chat_id)
        curr_year = get_curr_year()
        save_path_root = self.save_path

        self.set_dates(min_year, curr_year)
        print(f"Years: {min_year} - {curr_year}")
        # self.set_save_path(f'{save_path_root}/Frá byrjun')
        # self.create_all()
        for i in range(int(min_year), curr_year+1):
            print(f"Year: {i}")
            self.set_dates(i, i)
            self.set_save_path(f'{save_path_root}/{i}')
            self.create_all()
