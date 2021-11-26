from data_parser import DataParser
# python manage.py shell < apps/messenger/utils/populate_database.py 
import os
chat_id = 'thebicuriousnerdassociationchatboycottdominos'
dp = DataParser(
    save_path=f"{os.getcwd()}\\data\\", 
    chat_id=chat_id
)
dp.data_by_years()
