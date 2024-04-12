from flask import Flask, render_template, redirect, jsonify
from random import shuffle, choices

cards = ["Duke"]*3 + ["Contessa"]*3 + ["Ambassador"]*3 + ["Captain"]*3 + ["Assassin"]*3
shuffle(cards)
currently_challenging = False


class Player:
    def __init__(self, player_num):
        self.money = 2
        self.cards = [cards.pop()] + [cards.pop()]
        self.options = ["Income", "Foreign Aid", "Coup", "Tax", "Assassinate", "Swap", "Steal", "Save"]
        self.can_block = False
        self.can_be_challenged = False
        self.player_num = player_num
        self.can_play = False
        if self.player_num == 1:
            self.can_play = True

    def pass_play(self):
        pass


    def take_income(self):
        self.can_be_challenged = True
        self.money += 1
        self.can_play = False

players = [Player(player_num=i) for i in range(1, 5)]
player_names = [f"Player_{i}" for i in range(1, 5)]

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def home():
    player_num = 1
    players = [player_names[i] for i in range(4) if i + 1 != player_num]
    return render_template("template.html", player_num=player_num, players=players, player=players[player_num-1])


@app.route("/<int:player_num>/tax", methods=['POST'])
def tax(player_num):
    players[player_num-1].money += 3
    print(players[player_num-1].money)
    return jsonify({'money': players[player_num-1].money})


@app.route("/<int:player_num>")
def player_room(player_num):
    if (1 <= player_num <= 4):
        player_num = 1
        players = [player_names[i] for i in range(4) if i + 1 != player_num]
        return render_template("template.html", player_num = player_num, players = players)
    else:
        redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

#
# root = Tk()
# root.geometry("800x800")
# # image = Image.open("Billiard Tablecloth.png")
# # image = image.resize((700,700))
# # bg = PhotoImage(file="Billiard Tablecloth.png", width=1500, height=2000)
# # Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
# root.mainloop()