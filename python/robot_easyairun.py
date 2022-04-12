directionchange = 0

def on_on_chat():
    agent.teleport_to_player()
player.on_chat("top", on_on_chat)

def on_forever():
    global directionchange
    agent.destroy(FORWARD)
    directionchange = randint(0, 1000) % 500
    # サイコロ200以下だったら前進.
    if directionchange >= 0 and directionchange <= 200:
        agent.move(FORWARD, 2)
    # 400以下だったら、右に並行ウォークする    
    elif directionchange <= 400:
        agent.set_assist(PLACE_ON_MOVE, False)
        agent.move(RIGHT, 4)
    else:
    # 左に曲がる    
        agent.turn(LEFT_TURN)
    agent.collect_all()
# ループ関数を設定.
loops.forever(on_forever)

def on_on_chat2():
    gameplay.toggle_downfall()
player.on_chat("skychange", on_on_chat2)

def on_on_chat3():
    agent.move(FORWARD, 10)
player.on_chat("run", on_on_chat3)
