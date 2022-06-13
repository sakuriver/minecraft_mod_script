startValue = 0

def on_on_chat():
    blocks.print("DOTNOSATO", DIORITE, pos(0, 0, 0), WEST)
player.on_chat("towntitle", on_on_chat)

def on_on_chat2():
    agent.teleport_to_player()
player.on_chat("top", on_on_chat2)

def on_on_chat3():
    gameplay.time_set(gameplay.time(DAY))
player.on_chat("changedaily", on_on_chat3)

def on_on_chat4():
    global startValue
    blocks.fill(DOUBLE_WOODEN_SLAB,
        world(-20, 124, -20),
        world(80, 124, 20),
        FillOperation.HOLLOW)
    blocks.fill(DOUBLE_WOODEN_SLAB,
        world(20, 126, 20),
        world(0, 126, 0),
        FillOperation.HOLLOW)
    blocks.fill(TORCH,
        world(20, 130, 18),
        world(0, 130, 0),
        FillOperation.HOLLOW)
    housecreate(60, 145, 5, 63, 148, 8)
    housecreate(60, 145, 10, 68, 148, 8)
    housecreate(55, 145, 0, 52, 148, -3)
    player.teleport(world(40, 150, 6))
    mobs.spawn(WANDERING_TRADER, world(0, 64, 7))
    startValue = -18
    for index in range(40):
        if index % 5 == 0:
            blocks.fill(TORCH,
                world(-18, 125, startValue + index),
                world(78, 125, startValue + index + 1),
                FillOperation.HOLLOW)
player.on_chat("towncreate", on_on_chat4)

def housecreate(startBaseX: number, startBaseY: number, startBaseZ: number, endBaseX: number, endBaseY: number, endBaseZ: number):
    blocks.fill(GRAY_WOOL,
        world(startBaseX, startBaseY, startBaseZ),
        world(endBaseX, endBaseY, endBaseZ),
        FillOperation.HOLLOW)
    for index2 in range(4):
        baseXValue = index2 % 2 * 3
        blocks.fill(GRAY_WOOL,
            world(baseXValue, endBaseY + 1, startBaseZ),
            world(baseXValue, endBaseY + 3, startBaseZ),
            FillOperation.HOLLOW)
        blocks.fill(GRAY_WOOL,
            world(baseXValue, endBaseY + 1, endBaseZ),
            world(baseXValue, endBaseY + 3, endBaseZ),
            FillOperation.HOLLOW)
    blocks.fill(GRAY_WOOL,
        world(startBaseX, endBaseY + 2, startBaseZ),
        world(endBaseX, endBaseY + 3, endBaseZ),
        FillOperation.HOLLOW)
    blocks.fill(BRICKS_SLAB,
        world(startBaseX - 1, endBaseY + 3, startBaseZ - 1),
        world(endBaseX + 1, endBaseY + 3, endBaseZ + 1),
        FillOperation.HOLLOW)

def on_on_chat5():
    gameplay.toggle_downfall()
player.on_chat("skychange", on_on_chat5)

def on_on_chat6():
    agent.move(FORWARD, 10)
player.on_chat("run", on_on_chat6)

def on_on_chat7():
    player.teleport(pos(0, 0, 0))
player.on_chat("lsmypos", on_on_chat7)
