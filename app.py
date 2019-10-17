import tkinter as tk
from googletrans import Translator

translator = Translator()

# ボタンを押したときの処理を記述 --- (*1)
def search_dic():
    # テキストボックスから英単語を得る --- (*2)
    word = textWord.get()

    replaced = word.replace('\n', ' ')

    print(word)

    res = translator.translate(replaced, dest='ja').text

    textResult.delete('1.0', 'end') #一度全部消す
    textResult.insert(tk.END, res)


# ウィンドウを作成 --- (*6)
win = tk.Tk()
win.title("gts")
win.geometry("500x250")

# 部品を作成 --- (*7)
labelWord = tk.Label(win, text='input:')
labelWord.pack()

textWord = tk.Entry(win)
textWord.insert(tk.END, '')
textWord.pack()

calcButton = tk.Button(win, text='transrate')
calcButton["command"] = search_dic
calcButton.pack()

textResult = tk.Text(win)
textResult.insert(tk.END, 'ここに結果が表示されます')
textResult.pack()

# ウィンドウを動かす --- (*8)
win.mainloop()
