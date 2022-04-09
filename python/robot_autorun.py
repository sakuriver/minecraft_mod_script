def on_on_chat():
    agent.teleport_to_player()
player.on_chat("top", on_on_chat)

def on_forever():
    agent.destroy(FORWARD)
    agent.move(FORWARD, 2)
    agent.collect_all()
loops.forever(on_forever)

def on_on_chat2():
    agent.move(FORWARD, 10)
player.on_chat("run", on_on_chat2)
