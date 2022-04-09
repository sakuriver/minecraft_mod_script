player.onChat("top", function () {
    agent.teleportToPlayer()
})
loops.forever(function () {
    agent.destroy(FORWARD)
    agent.move(FORWARD, 2)
    agent.collectAll()
})
player.onChat("run", function () {
    agent.move(FORWARD, 10)
})
