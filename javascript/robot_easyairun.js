let directionchange = 0
player.onChat("top", function () {
    agent.teleportToPlayer()
})
// agentの歩行ロジック
loops.forever(function () {
    agent.destroy(FORWARD)
    // 歩く方向をサイコロ振って決める
    directionchange = randint(0, 1000) % 500
    // サイコロが200以下だった
    if (directionchange >= 0 && directionchange <= 200) {
        // ロボット君が２歩進む
        agent.move(FORWARD, 2)
    // 201以上で400未満のサイコロだった    
    } else if (directionchange <= 400) {
        // 右を曲がる
        agent.setAssist(PLACE_ON_MOVE, false)
        agent.move(RIGHT, 4)
    } else {
        // 左を向く
        agent.turn(LEFT_TURN)
    }
    agent.collectAll()
})
// 空の変更コマンド
player.onChat("skychange", function () {
    gameplay.toggleDownfall()
})
player.onChat("run", function () {
    agent.move(FORWARD, 10)
})
