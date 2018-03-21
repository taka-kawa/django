import sqlite3

con = sqlite3.connect('db.sqlite3')

def set_up_text_cat():
    sql = u"insert into text_cat (id, category) values (0, '無効'), (1, '問い合わせ'), (2, '返信')"
    try:
        con.execute(sql)
        con.commit()
        print("complete text_cat setup")
    except sqlite3.IntegrityError:
        print("すでにtext_catはセットアップされています")

set_up_text_cat()