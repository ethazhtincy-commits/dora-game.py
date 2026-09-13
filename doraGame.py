from IPython.display import display, HTML
import uuid

game_id = "dora_game_" + str(uuid.uuid4())[:8]

display(HTML(f"""
<style>

#game_{game_id} {{
    width: 800px;
    height: 500px;
    position: relative;
    overflow: hidden;
    border: 5px solid #222;
    background: linear-gradient(
        skyblue 0%,
        #dff7ff 65%,
        #b7e58b 100%
    );
    font-family: Arial, sans-serif;
    user-select: none;
}}

/* ================= BACKGROUND ================= */

.sun {{
    position: absolute;
    width: 70px;
    height: 70px;
    background: #FFD93D;
    border-radius: 50%;
    right: 80px;
    top: 45px;
    box-shadow: 0 0 30px #FFD93D;
}}

.cloud {{
    position: absolute;
    background: white;
    width: 90px;
    height: 28px;
    border-radius: 30px;
    z-index: 1;
}}

.cloud::before {{
    content: "";
    position: absolute;
    width: 38px;
    height: 38px;
    background: white;
    border-radius: 50%;
    left: 15px;
    top: -18px;
}}

.cloud::after {{
    content: "";
    position: absolute;
    width: 48px;
    height: 48px;
    background: white;
    border-radius: 50%;
    right: 10px;
    top: -25px;
}}

/* Mountains */

.mountain {{
    position: absolute;
    bottom: 95px;
    width: 280px;
    height: 180px;
    background: #6fa85b;
    border-radius: 50% 50% 0 0;
    z-index: 2;
}}

.mountain::after {{
    content: "";
    position: absolute;
    width: 120px;
    height: 80px;
    background: #9acb76;
    left: 80px;
    top: 25px;
    border-radius: 50%;
}}

/* Jungle trees */

.tree {{
    position: absolute;
    bottom: 70px;
    width: 35px;
    height: 130px;
    background: #704214;
    z-index: 4;
}}

.tree::before {{
    content: "";
    position: absolute;
    width: 100px;
    height: 90px;
    background: #269447;
    border-radius: 50%;
    left: -32px;
    top: -55px;
}}

.tree::after {{
    content: "";
    position: absolute;
    width: 75px;
    height: 65px;
    background: #35ad52;
    border-radius: 50%;
    left: -20px;
    top: -80px;
}}

/* ================= RIVER ================= */

.river {{
    position: absolute;
    left: 0;
    bottom: 45px;
    width: 100%;
    height: 85px;
    background: #55c7e8;
    z-index: 5;
    border-top: 5px solid #2b9fc4;
}}

/* ================= GROUND ================= */

.ground {{
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 55px;
    background: #8B5A2B;
    border-top: 8px solid #45a832;
    z-index: 10;
}}

/* ================= BRIDGE ================= */

.bridge {{
    position: absolute;
    left: 310px;
    bottom: 45px;
    width: 180px;
    height: 25px;
    background: #b87535;
    border: 4px solid #704214;
    z-index: 15;
}}

.bridge::before,
.bridge::after {{
    content: "";
    position: absolute;
    width: 12px;
    height: 55px;
    background: #704214;
    bottom: -55px;
}}

.bridge::before {{
    left: 20px;
}}

.bridge::after {{
    right: 20px;
}}

/* ================= PLATFORMS ================= */

.platform {{
    position: absolute;
    height: 22px;
    background: #704214;
    border-top: 7px solid #45a832;
    border-radius: 5px;
    z-index: 20;
}}

/* New obstacle styles */
.water-zone {{
    position: absolute;
    background: #00bfff; /* Blue for water */
    opacity: 0.8;
    z-index: 10; /* Below player, above river/ground for visual overlap */
    border-top: 3px solid #008fcc;
}}

.moving-platform {{
    background: #a87e45; /* Different color for moving platform */
    border-top: 7px solid #704214;
}}

/* ================= DORA PLAYER ================= */

.player {{
    position: absolute;
    width: 42px;
    height: 65px;
    z-index: 40;
}}

/* Hair */

.dora-hair {{
    position: absolute;
    left: 4px;
    top: 5px;
    width: 34px;
    height: 35px;
    background: #32180e;
    border-radius: 50%;
}}

/* Face */

.dora-face {{
    position: absolute;
    left: 9px;
    top: 8px;
    width: 25px;
    height: 27px;
    background: #c98255;
    border-radius: 50%;
    z-index: 2;
}}

/* Eyes */

.dora-eye {{
    position: absolute;
    width: 4px;
    height: 7px;
    background: black;
    border-radius: 50%;
    top: 17px;
    z-index: 3;
}}

.dora-eye.one {{
    left: 15px;
}}

.dora-eye.two {{
    left: 25px;
}}

/* Pink shirt */

.dora-shirt {{
    position: absolute;
    left: 7px;
    top: 32px;
    width: 28px;
    height: 18px;
    background: #f45b9a;
    border-radius: 5px;
}}

/* Orange shorts */

.dora-shorts {{
    position: absolute;
    left: 8px;
    top: 48px;
    width: 27px;
    height: 13px;
    background: #f28c28;
    border-radius: 4px;
}}

/* Backpack */

.backpack {{
    position: absolute;
    left: 0px;
    top: 32px;
    width: 10px;
    height: 23px;
    background: #8e44ad;
    border-radius: 5px;
}}

/* Shoes */

.dora-shoes {{
    position: absolute;
    left: 7px;
    top: 59px;
    width: 28px;
    height: 8px;
    background: #56351e;
    border-radius: 50%;
}}

/* ================= STARS ================= */

.star {{
    position: absolute;
    width: 28px;
    height: 28px;
    z-index: 30;
    font-size: 28px;
}}

/* Particle effect for collected stars */
.star-particle {{
    position: absolute;
    background-color: yellow;
    border-radius: 50%;
    width: 8px;
    height: 8px;
    opacity: 0;
    animation: fadeOutUp 0.8s forwards;
    z-index: 31;
}}

@keyframes fadeOutUp {{
    from {{
        transform: translateY(0) scale(1);
        opacity: 1;
    }}
    to {{
        transform: translateY(-20px) scale(0);
        opacity: 0;
    }}
}}

/* ================= SWIPER ================= */

.enemy {{
    position: absolute;
    width: 48px;
    height: 38px;
    background: #9b5b28;
    border-radius: 50% 50% 40% 40%;
    z-index: 35;
}}

.enemy-ear {{
    position: absolute;
    width: 15px;
    height: 15px;
    background: #704214;
    top: -8px;
    border-radius: 50%;
}}

.enemy-ear.one {{
    left: 5px;
}}

.enemy-ear.two {{
    right: 5px;
}}

.enemy-eye {{
    position: absolute;
    width: 7px;
    height: 9px;
    background: white;
    border-radius: 50%;
    top: 10px;
}}

.enemy-eye.one {{
    left: 12px;
}}

.enemy-eye.two {{
    right: 12px;
}}

.enemy-nose {{
    position: absolute;
    width: 10px;
    height: 8px;
    background: black;
    border-radius: 50%;
    left: 19px;
    top: 23px;
}}

/* ================= UI ================= */

.ui {{
    position: absolute;
    top: 12px;
    left: 12px;
    right: 12px;
    display: flex;
    justify-content: space-between;
    z-index: 100;
    pointer-events: none;
}}

.score {{
    background: white;
    border: 3px solid #222;
    border-radius: 12px;
    padding: 7px 12px;
    font-size: 16px;
    font-weight: bold;
}}

.music-button {{
    position: absolute;
    top: 12px;
    right: 12px;
    background: white;
    border: 3px solid #222;
    border-radius: 12px;
    padding: 7px 12px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    z-index: 101;
    pointer-events: all;
}}

/* ================= MESSAGE ================= */

.message {{
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.72);
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    text-align: center;
    z-index: 500;
}}

.message-title {{
    font-size: 45px;
    font-weight: bold;
}}

.message-text {{
    font-size: 20px;
    margin-top: 12px;
}}

.restart {{
    margin-top: 25px;
    padding: 10px 25px;
    font-size: 18px;
    border-radius: 10px;
    cursor: pointer;
}}

</style>


<div id="game_{game_id}">

    <!-- BACKGROUND -->

    <div class="sun"></div>

    <div class="cloud" style="left:80px; top:65px;"></div>
    <div class="cloud" style="left:400px; top:100px;"></div>
    <div class="cloud" style="left:250px; top:120px; width:70px;"></div>
    <div class="cloud" style="left:600px; top:70px; width:110px; height:35px;"></div>

    <div class="mountain" style="left:-80px;"></div>
    <div class="mountain" style="left:200px; bottom:85px; width:220px; height:150px;"></div>
    <div class="mountain" style="left:450px; width:330px;"></div>

    <div class="tree" style="left:40px;"></div>
    <div class="tree" style="left:180px; bottom:60px; transform:scale(0.8);"></div>
    <div class="tree" style="left:650px; bottom:75px; transform:scale(0.9);"></div>
    <div class="tree" style="left:720px;"></div>

    <!-- RIVER -->

    <div class="river"></div>

    <!-- BRIDGE -->

    <div class="bridge"></div>

    <!-- PLATFORMS -->

    <div class="platform"
         style="left:100px; top:330px; width:150px;"></div>

    <div class="platform"
         style="left:520px; top:300px; width:150px;"></div>

    <!-- New Platforms for moving platform context -->
    <div class="platform" style="left:250px; top:200px; width:80px;"></div>
    <div class="platform moving-platform" id="moving_platform_1_{game_id}" style="left:350px; top:200px; width:80px;"></div>
    <div class="platform" style="left:450px; top:200px; width:80px;"></div>


    <!-- GROUND -->

    <div class="ground"></div>

    <!-- WATER ZONES -->
    <div class="water-zone" style="left:260px; top:445px; width:45px; height:55px;"></div>


    <!-- STARS -->

    <div class="star" style="left:170px; top:285px;">⭐</div>
    <div class="star" style="left:350px; top:250px;">⭐</div>
    <div class="star" style="left:570px; top:255px;">⭐</div>
    <div class="star" style="left:690px; top:380px;">⭐</div>


    <!-- SWIPER -->

    <div id="enemy_{game_id}" class="enemy"> <!-- Removed game_id from id -->

        <div class="enemy-ear one"></div>
        <div class="enemy-ear two"></div>

        <div class="enemy-eye one"></div>
        <div class="enemy-eye two"></div>

        <div class="enemy-nose"></div>

    </div>


    <!-- PLAYER / DORA -->

    <div id="player_{game_id}" class="player">

        <div class="dora-hair"></div>

        <div class="dora-face"></div>

        <div class="dora-eye one"></div>
        <div class="dora-eye two"></div>

        <div class="backpack"></div>

        <div class="dora-shirt"></div>

        <div class="dora-shorts"></div>

        <div class="dora-shoes"></div>

    </div>


    <!-- UI -->

    <div class="ui">

        <div class="score" id="score_{game_id}">
            ⭐ Stars: 0
        </div>

        <div class="score" id="lives_{game_id}">
            ❤️ Lives: 3
        </div>

        <div class="score" id="timer_{game_id}">
            ⏱️ Time: 0s
        </div>

    </div>

    <!-- MUSIC CONTROL -->
    <button class="music-button" id="music_toggle_{game_id}">🎵</button>

    <!-- MESSAGE -->

    <div class="message" id="message_{game_id}">

        <div class="message-title"
             id="messageTitle_{game_id}">
            YOU WIN!
        </div>

        <div class="message-text"
             id="messageText_{game_id}">
            Adventure completed!
        </div>

        <button class="restart"
                onclick="location.reload()">
            🔄 Play Again
        </button>

    </div>

    <audio id="game_music_{game_id}" loop>
        <source src="https://www.learningcontainer.com/wp-content/uploads/2020/02/sample-mp3-file.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>

</div>


<script>

(function() {{

    const game =
        document.getElementById("game_{game_id}");

    const player =
        document.getElementById("player_{game_id}");

    const enemy =
        document.getElementById("enemy_{game_id}");

    const scoreDisplay =
        document.getElementById("score_{game_id}");

    const livesDisplay =
        document.getElementById("lives_{game_id}");

    const timerDisplay =
        document.getElementById("timer_{game_id}");

    const message =
        document.getElementById("message_{game_id}");

    const messageTitle =
        document.getElementById("messageTitle_{game_id}");

    const messageText =
        document.getElementById("messageText_{game_id}");

    const gameMusic = document.getElementById("game_music_{game_id}");
    const musicToggleButton = document.getElementById("music_toggle_{game_id}");

    // References to the new elements
    const movingPlatform1 = document.getElementById(`moving_platform_1_${game_id}`);

    /* ================= MUSIC CONTROL ================= */
    let isMusicPlaying = false;

    function toggleMusic() {{
        if (isMusicPlaying) {{
            gameMusic.pause();
            musicToggleButton.textContent = '🔇'; // Muted icon
        }} else {{
            gameMusic.play().catch(e => console.error("Error playing music:", e));
            musicToggleButton.textContent = '🎵'; // Playing icon
        }}
        isMusicPlaying = !isMusicPlaying;
    }}

    musicToggleButton.addEventListener('click', toggleMusic);

    // Attempt to play music when the game starts, might be blocked by browser policies
    gameMusic.volume = 0.3; // Set a default volume
    gameMusic.play().then(() => {{
        isMusicPlaying = true;
        musicToggleButton.textContent = '🎵';
    }}).catch(e => {{
        console.log("Autoplay blocked. User interaction needed to play music.");
        isMusicPlaying = false;
        musicToggleButton.textContent = '🔇';
    }});;


    /* ================= PLAYER ================= */

    let playerX = 40;
    let playerY = 385;

    let velocityY = 0;

    const playerWidth = 42;
    const playerHeight = 65;

    const moveSpeed = 5;
    const gravity = 0.6;
    const jumpPower = -12;

    let onGround = true;


    /* ================= GAME ================= */

    let stars = 0;
    let lives = 3;

    let gameOver = false;
    let currentLevel = 1; // Start at Level 1
    const totalLevels = 3; // Example: Define total number of levels

    let startTime;
    let elapsedTime = 0;
    let timerInterval;


    /* ================= KEYBOARD ================= */

    const keys = {{}};

    document.addEventListener("keydown", function(e) {{

        const key = e.key.toLowerCase();

        keys[key] = true;

        if (
            (key === " " ||
             key === "arrowup" ||
             key === "w") &&
            onGround &&
            !gameOver
        ) {{

            velocityY = jumpPower;
            onGround = false;

        }}

    }});;


    document.addEventListener("keyup", function(e) {{

        keys[e.key.toLowerCase()] = false;

    }});;


    /* ================= PLATFORMS ================= */

    const platforms = [

        {{x:100, y:330, width:150, height:22}},

        {{x:520, y:300, width:150, height:22}},

        {{x:310, y:405, width:180, height:25}},

        // New static platforms
        {{x:250, y:200, width:80, height:22}},
        {{x:450, y:200, width:80, height:22}},

        // New water zone
        {{x:260, y:445, width:45, height:55, type: 'water'}},

        // Moving platforms
        {{x:350, y:200, width:80, height:22, type: 'moving', element: movingPlatform1, speed: 1, minX: 350, maxX: 450}}
    ];


    /* ================= STARS ================= */

    const starElements =
        Array.from(game.querySelectorAll(".star"));

    const starData =
        starElements.map(function(el) {{

            return {{

                element: el,

                x: parseInt(el.style.left),

                y: parseInt(el.style.top),

                collected: false

            }};

        }});;

    function createStarParticle(x, y) {{
        const particle = document.createElement('div');
        particle.className = 'star-particle';
        game.appendChild(particle);

        const size = Math.random() * 5 + 3; // Random size between 3 and 8px
        particle.style.width = `{{$size}}px`; // Escaped JS template literal
        particle.style.height = `{{$size}}px`; // Escaped JS template literal
        particle.style.left = `{{$x + 10 + (Math.random() * 10 - 5)}}px`; // Escaped JS template literal
        particle.style.top = `{{$y + 10 + (Math.random() * 10 - 5)}}px`; // Escaped JS template literal

        setTimeout(() => {{ particle.remove(); }}, 800); // Escaped arrow function braces
    }};


    /* ================= SWIPER ================= */

    let enemyX = 430;
    let enemyY = 365;

    let enemyDirection = 1;

    const enemySpeed = 1.5;

    let enemyAlive = true;


    /* ================= COLLISION ================= */

    function overlap(
        ax, ay, aw, ah,
        bx, by, bw, bh
    ) {{

        return (

            ax < bx + bw &&

            ax + aw > bx &&

            ay < by + bh &&

            ay + ah > by

        );

    }};;


    /* ================= LOSE LIFE ================= */

    function loseLife() {{

        lives--;

        livesDisplay.innerHTML =
            "❤️ Lives: " + lives;

        // Reset player position more generically to start or safe point
        playerX = 40;
        playerY = 385; // Default starting position

        velocityY = 0;

        if (lives <= 0) {{

            gameOver = true;
            clearInterval(timerInterval); // Stop the timer

            messageTitle.innerHTML =
                "😵 GAME OVER";

            messageText.innerHTML =
                "Swiper caught Dora!";

            message.style.display = "flex";

        }}

    }}


    /* ================= COLLECT STARS ================= */

    function checkStars() {{

        starData.forEach(function(star) {{

            if (star.collected) {{

                return;

            }}


            if (

                overlap(

                    playerX,
                    playerY,
                    playerWidth,
                    playerHeight,

                    star.x,
                    star.y,

                    28,
                    28

                )

            ) {{

                star.collected = true;

                star.element.style.display = "none";

                stars++;

                scoreDisplay.innerHTML = \
                    "⭐ Stars: " + stars;

                // Create particle effect
                for (let i = 0; i < 5; i++) {{
                    createStarParticle(star.x, star.y);
                }}

            }}

        }});;

    }}


    /* ================= SWIPER ================= */

    function updateEnemy() {{

        if (!enemyAlive) {{

            return;

        }}


        enemyX +=
            enemySpeed * enemyDirection;


        if (enemyX >= 650) {{

            enemyDirection = -1;

        }}


        if (enemyX <= 380) {{

            enemyDirection = 1;

        }}


        enemy.style.left =
            enemyX + "px";

        enemy.style.top =
            enemyY + "px";


        /* Enemy collision */

        if (

            overlap(

                playerX,
                playerY,
                playerWidth,
                playerHeight,

                enemyX,
                enemyY,

                48,
                38

            )

        ) {{

            const playerBottom =
                playerY + playerHeight;

            const enemyTop =
                enemyY;


            /* Dora jumps on Swiper */

            if (

                velocityY > 0 &&

                playerBottom - enemyTop < 25

            ) {{

                enemyAlive = false;

                enemy.style.display = "none";

                velocityY = -8;

                scoreDisplay.innerHTML =
                    "⭐ Stars: " + stars + "   💥 +100";

                setTimeout(function() {{

                    scoreDisplay.innerHTML =
                        "⭐ Stars: " + stars;

                }}, 800);

            }}

            else {{

                loseLife();

            }}

        }};;

    }}

    /* ================= MOVING PLATFORMS ================= */
    function updateMovingPlatforms() {{
        platforms.forEach(function(p) {{
            if (p.type === 'moving') {{
                p.x += p.speed;

                if (p.x <= p.minX || p.x >= p.maxX) {{
                    p.speed *= -1; // Reverse direction
                }}
                p.element.style.left = p.x + "px";
            }}
        }});;
    }}


    /* ================= PLAYER PHYSICS ================= */

    function updatePlayer() {{

        /* LEFT */

        if (
            keys["arrowleft"] ||
            keys["a"]
        ) {{

            playerX -= moveSpeed;

        }}


        /* RIGHT */

        if (
            keys["arrowright"] ||
            keys["d"]
        ) {{

            playerX += moveSpeed;

        }}


        /* SCREEN LIMITS */

        if (playerX < 0) {{

            playerX = 0;

        }}


        if (playerX > 750) {{

            playerX = 750;

        }}


        const oldBottom =
            playerY + playerHeight;


        /* GRAVITY */

        velocityY += gravity;

        playerY += velocityY;

        onGround = false;


        /* PLATFORM COLLISION */

        let onMovingPlatform = false;
        let movingPlatformSpeed = 0;

        platforms.forEach(function(p) {{
            const horizontal =
                playerX + playerWidth > p.x &&
                playerX < p.x + p.width;

            const landing =
                oldBottom <= p.y &&
                playerY + playerHeight >= p.y &&
                velocityY >= 0;

            if (horizontal && landing) {{
                playerY = p.y - playerHeight;
                velocityY = 0;
                onGround = true;

                if (p.type === 'moving') {{
                    onMovingPlatform = true;
                    movingPlatformSpeed = p.speed;
                }}
            }}

            // Water collision
            if (p.type === 'water' && overlap(
                playerX, playerY, playerWidth, playerHeight,
                p.x, p.y, p.width, p.height
            )) {{
                loseLife();
            }}
        }});;

        // If player is on a moving platform, move with it
        if (onMovingPlatform) {{
            playerX += movingPlatformSpeed;
        }}

        /* GROUND */

        if (playerY >= 385) {{
            playerY = 385;
            velocityY = 0;
            onGround = true;
        }}


        /* UPDATE PLAYER */

        player.style.left =
            playerX + "px";

        player.style.top =
            playerY + "px";

    }}


    /* ================= TIMER ================= */

    function updateTimer() {{
        if (!gameOver) {{
            elapsedTime = Math.floor((Date.now() - startTime) / 1000);
            timerDisplay.innerHTML = `⏱️ Time: ${{$elapsedTime}}s`;
        }}
    }}


    /* ================= FINISH ================= */

    function checkFinish() {{

        if (playerX >= 730) {{

            gameOver = true;
            clearInterval(timerInterval); // Stop the timer

            if (currentLevel < totalLevels) {{
                messageTitle.innerHTML =
                    "🎉 LEVEL " + currentLevel + " COMPLETE!";
                messageText.innerHTML =
                    `Dora reached the end of Level ${{$currentLevel}}! Stars collected: ${{$stars}}. Time taken: ${{$elapsedTime}}s`;
                // Future: Add a button to load next level
            }} else {{
                messageTitle.innerHTML =
                    "🏆 ADVENTURE COMPLETE!";

                messageText.innerHTML =
                    `Dora reached the destination! Stars collected: ${{$stars}}. Time taken: ${{$elapsedTime}}s`;
            }}

            message.style.display = "flex";

        }}

    }}


    /* ================= GAME LOOP ================= */

    function gameLoop() {{

        if (!gameOver) {{

            updatePlayer();

            updateEnemy();

            updateMovingPlatforms(); // Call new function

            checkStars();

            checkFinish();

        }}

        requestAnimationFrame(gameLoop);

    }}


    /* ================= START ================= */

    function startGame() {{
        startTime = Date.now();
        timerInterval = setInterval(updateTimer, 1000); // Update timer every second
        gameLoop();
        console.log("🎒 Dora Adventure Game Started!");
    }}

    startGame();

}})();

</script>
"""))

print("🎒 DORA ADVENTURE GAME READY!")
print()
print("⬅️ A / Left Arrow  = Move Left")
print("➡️ D / Right Arrow = Move Right")
print("⬆️ W / Up Arrow    = Jump")
print("␣ Space            = Jump")
print()
print("⭐ Collect stars")
print("🦊 Avoid or jump on Swiper")
print("❤️ You have 3 lives")
print("🏆 Reach the destination")
