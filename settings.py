import pygame

PROJECT = {
    "name": 'ASTEROIDS',
    "width": 800,
    "height": 600,
    "colors":{
        "black":(0,0,0),
        "red":(250,0,0),
        "green":(0,250,0),
        "blue":(0,0,250),
        "white":(250,250,250)
    }
}

INSTANCES = {
    "player":{
    "localization":{
        "x":int(PROJECT["width"] / 2),
        "y":int(PROJECT["height"] / 2)
    },
    "representation":{
        "sprites_sheet":"asteroids/sheets/player_sheet.png",
        "frame":0,
        "width":92,
        "height":82,
        "scale":1,

    }
    },
    "bullet":{
    "localization":{
        "x":0,
        "y":0
    },
    "representation":{
        "sprites_sheet":"asteroids/sheets/player.png",
        "frame":4,
        "width":20,
        "height":20,
        "scale":1,

    }
},
"interactive_objs":
{"rocks":[
    
    {
    "localization":{
        "x":0,
        "y":0
    },
    "representation":{
        "sprites_sheet":"asteroids/sheets/rocks_sheet.png",
        "frame":0,
        "width":194,
        "height":130,
        "scale":1,

    },
    "physics":{
        "speed":1
    }
},
    {
    "localization":{
        "x":0,
        "y":400
    },
    "representation":{
        "sprites_sheet":"asteroids/sheets/rocks_sheet.png",
        "frame":0,
        "width":194,
        "height":130,
        "scale":1,

    },
    "physics":{
        "speed":1
    }
},
    {
    "localization":{
        "x":600,
        "y":400
    },
    "representation":{
        "sprites_sheet":"asteroids/sheets/rocks_sheet.png",
        "frame":0,
        "width":194,
        "height":130,
        "scale":1,

    },
    "physics":{
        "speed":1
    }
},
    {
    "localization":{
        "x":350,
        "y":400
    },
    "representation":{
        "sprites_sheet":"asteroids/sheets/rocks_sheet.png",
        "frame":0,
        "width":194,
        "height":130,
        "scale":1,

    },
    "physics":{
        "speed":1
    }
}
]}

}
pygame.init()

SCREEN = pygame.display.set_mode((PROJECT["width"], PROJECT["height"]))
CLOCK = pygame.time.Clock()

# Controller settings 
CONTROLLERS = {
"UP_BTN":pygame.K_w,
        "ALT_UP_BTN":pygame.K_UP,
        "R_BTN":pygame.K_d,
        "ALT_R_BTN":pygame.K_RIGHT,
        "L_BTN":pygame.K_a,
        "ALT_L_BTN":pygame.K_LEFT,
        "SHOOT_BTN":pygame.K_SPACE, 
        "START_GAME_BTN":pygame.K_b,
        "CLOSE_APP_BTN":pygame.K_ESCAPE} 


