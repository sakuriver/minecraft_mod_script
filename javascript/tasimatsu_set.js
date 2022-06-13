



let startValue = 0
player.onChat("towntitle", function () {
    blocks.print(
    "DOTNOSATO",
    DIORITE,
    pos(0, 0, 0),
    WEST
    )
})
player.onChat("top", function () {
    agent.teleportToPlayer()
})
player.onChat("changedaily", function () {
    gameplay.timeSet(gameplay.time(DAY))
})
player.onChat("towncreate", function () {
    blocks.fill(
    DOUBLE_WOODEN_SLAB,
    world(-20, 124, -20),
    world(80, 124, 20),
    FillOperation.Hollow
    )
    blocks.fill(
    DOUBLE_WOODEN_SLAB,
    world(20, 126, 20),
    world(0, 126, 0),
    FillOperation.Hollow
    )
    blocks.fill(
    TORCH,
    world(20, 130, 18),
    world(0, 130, 0),
    FillOperation.Hollow
    )
    housecreate(60, 145, 5, 63, 148, 8)
    housecreate(60, 145, 10, 68, 148, 8)
    housecreate(55, 145, 0, 52, 148, -3)
    player.teleport(world(40, 150, 6))
    mobs.spawn(WANDERING_TRADER, world(0, 64, 7))
    startValue = -18
    for (let index = 0; index <= 39; index++) {
        if (index % 5 == 0) {
            blocks.fill(
            TORCH,
            world(-18, 125, startValue + index),
            world(78, 125, startValue + index + 1),
            FillOperation.Hollow
            )
        }
    }
})
function housecreate (startBaseX: number, startBaseY: number, startBaseZ: number, endBaseX: number, endBaseY: number, endBaseZ: number) {
    let baseXValue: number;
blocks.fill(
    GRAY_WOOL,
    world(startBaseX, startBaseY, startBaseZ),
    world(endBaseX, endBaseY, endBaseZ),
    FillOperation.Hollow
    )
    for (let index2 = 0; index2 <= 3; index2++) {
        baseXValue = index2 % 2 * 3
        blocks.fill(
        GRAY_WOOL,
        world(baseXValue, endBaseY + 1, startBaseZ),
        world(baseXValue, endBaseY + 3, startBaseZ),
        FillOperation.Hollow
        )
        blocks.fill(
        GRAY_WOOL,
        world(baseXValue, endBaseY + 1, endBaseZ),
        world(baseXValue, endBaseY + 3, endBaseZ),
        FillOperation.Hollow
        )
    }
    blocks.fill(
    GRAY_WOOL,
    world(startBaseX, endBaseY + 2, startBaseZ),
    world(endBaseX, endBaseY + 3, endBaseZ),
    FillOperation.Hollow
    )
    blocks.fill(
    BRICKS_SLAB,
    world(startBaseX - 1, endBaseY + 3, startBaseZ - 1),
    world(endBaseX + 1, endBaseY + 3, endBaseZ + 1),
    FillOperation.Hollow
    )
}
player.onChat("skychange", function () {
    gameplay.toggleDownfall()
})
player.onChat("run", function () {
    agent.move(FORWARD, 10)
})
player.onChat("lsmypos", function () {
    player.teleport(pos(0, 0, 0))
})
