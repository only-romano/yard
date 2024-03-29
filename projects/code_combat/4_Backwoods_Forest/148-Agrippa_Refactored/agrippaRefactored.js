function cleaveOrAttack(enemy) {
    // If "cleave" is ready, cleave; otherwise, attack.
    if (hero.isReady("cleave")) {
        hero.cleave(enemy);
    } else {
        hero.attack(enemy);
    }
}

while(true) {
    var enemy = hero.findNearestEnemy();
    if(enemy) {
        var distance = hero.distanceTo(enemy);
        if(distance < 5) {
            // Call the "cleaveOrAttack" function, defined above.
            cleaveOrAttack(enemy);
        }
    }
}
