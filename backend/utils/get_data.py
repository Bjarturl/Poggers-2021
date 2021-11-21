from data_parser import DataParser
# python manage.py shell < apps/messenger/utils/populate_database.py 

chat_id = 'boycott'
dp = DataParser(
    save_path=f"C:/Users/Notandi/Desktop/poggers21/backend/data/parsed/{chat_id}", 
    chat_id=chat_id, 
    is_id=False,
    trivia_words=[]
)
dp.data_by_years(True)
