#minigame.rpy

init python:
    renpy.random.seed()
    correct_placements = {
        f"paper_{i}_{j}": f"folder_{j}"
        for i in range(1, 11)
        for j in range(1, 7)
        }
    starting_item_options = {
            f"starting_item_options{i}": [
                {"image": f"minigame_assets/archie_minigame/paper_{j}.avif", "drag_name": f"paper_{i}_{j}"}
                for j in range(1, 7)
            ]
            for i in range(1, 11)
        }
    selected_items = {}
    for i in range(1, 11):
        selected_items[f"selected_item{i}"] = renpy.random.choice(starting_item_options[f"starting_item_options{i}"])
    ingredient_snaps = {
        "ingredient_1": ((0.12, 0.065, 0.4), "mirae_beefcubes"),
        "ingredient_2": ((0.395, 0.065, 0.4), "mirae_butter"),
        "ingredient_3": ((0.675, 0.065, 0.4), "mirae_potatoes"),
        "ingredient_4": ((0.12, 0.345, 0.4), "mirae_currycubes"),
        "ingredient_5": ((0.395, 0.345, 0.4), "mirae_carrots"),
        "ingredient_6": ((0.675, 0.345, 0.4), "mirae_onions"),
        }

    def drag_function_archie(dragged_items, dropped_on):
        if dropped_on is not None:
            dragged_name = dragged_items[0].drag_name
            dropped_name = dropped_on.drag_name
            n = int(dragged_name[6:8].strip('_'))
            folder_group.remove(getattr(store, f"starting_item{n}"))
            if n != 10:
                folder_group.add(getattr(store, f"starting_item{n+1}"))
            if dragged_name[-1] == dropped_name[-1]:
                store.archie_win_count += 1
                renpy.sound.play("audio/Correct.ogg")
                if store.archie_win_count == 8:
                    renpy.jump("archie_winlose")
            else:
                store.archie_mistake_count += 1
                renpy.sound.play("audio/Wrong.ogg")
                if store.archie_mistake_count == 3:
                    renpy.jump("archie_winlose")

    def drag_function_mirae(dragged_items, dropped_on):
        if dropped_on is not None:
            dragged_name = dragged_items[0].drag_name
            dropped_name = dropped_on.drag_name
            snap_coords, variable_name = ingredient_snaps[dragged_name]
            dragged_items[0].snap(*snap_coords)
            setattr(store, variable_name, getattr(store, variable_name) + 1)
            store.mirae_total_ingredients += 1
            if store.mirae_total_ingredients == 10:
                current_ingredients = {
                    "beefcubes": mirae_beefcubes,
                    "butter": mirae_butter,
                    "potatoes": mirae_potatoes,
                    "currycubes": mirae_currycubes,
                    "carrots": mirae_carrots,
                    "onions": mirae_onions,
                }
                if selected_recipe == current_ingredients:
                    store.mirae_correct_recipe = True
                    renpy.sound.play("audio/Correct.ogg")
                    renpy.jump("mirae_winlose")
                else:
                    renpy.sound.play("audio/Wrong.ogg")
                    renpy.jump("mirae_winlose")
                    
    def play_archie_drag_activated_sound(dragged_items):
        renpy.sound.play("audio/Paper.ogg")


#Archie_Minigame ==============================================================
#Archie_Minigame ==============================================================
#Archie_Minigame ==============================================================
default archie_win_count = 0 #up to 8
default archie_mistake_count = 0 #up to 3

#Folders Droppables =============================
default folder_1 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_1", draggable = False, droppable = True, align = (0.15,0.1), focus_mask = True, mouse_drop = True) #Applied Theories
default folder_2 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_2", draggable = False, droppable = True, align = (0.5,0.1), focus_mask = True, mouse_drop = True) #FGD Transcripts
default folder_3 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_3", draggable = False, droppable = True, align = (0.85,0.1), focus_mask = True, mouse_drop = True) #Key Takeaways
default folder_4 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_4", draggable = False, droppable = True, align = (0.15,0.55), focus_mask = True, mouse_drop = True) #RRL
default folder_5 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_5", draggable = False, droppable = True, align = (0.5,0.55), focus_mask = True, mouse_drop = True) #Scope of the Research
default folder_6 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_6", draggable = False, droppable = True, align = (0.85,0.55), focus_mask = True, mouse_drop = True) #Statistical Graph

#Starting Item Draggables =============================
default starting_item1 = Drag(d=selected_items["selected_item1"]["image"], drag_name=selected_items["selected_item1"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item2 = Drag(d=selected_items["selected_item2"]["image"], drag_name=selected_items["selected_item2"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item3 = Drag(d=selected_items["selected_item3"]["image"], drag_name=selected_items["selected_item3"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item4 = Drag(d=selected_items["selected_item4"]["image"], drag_name=selected_items["selected_item4"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item5 = Drag(d=selected_items["selected_item5"]["image"], drag_name=selected_items["selected_item5"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item6 = Drag(d=selected_items["selected_item6"]["image"], drag_name=selected_items["selected_item6"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item7 = Drag(d=selected_items["selected_item7"]["image"], drag_name=selected_items["selected_item7"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item8 = Drag(d=selected_items["selected_item8"]["image"], drag_name=selected_items["selected_item8"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item9 = Drag(d=selected_items["selected_item9"]["image"], drag_name=selected_items["selected_item9"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)
default starting_item10 = Drag(d=selected_items["selected_item10"]["image"], drag_name=selected_items["selected_item10"]["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_archie_drag_activated_sound)

#Folder Group and Screen=============================
default folder_group = DragGroup(folder_1, folder_2, folder_3, folder_4, folder_5, folder_6, starting_item1)

screen draggroup_archie:
    add "dim_effect.avif" alpha 0.8
    text "Applied Theories" xalign 0.19 yalign 0.38 color "#FFF" font "windows-xp-tahoma.ttf" size 35
    text "FGD Transcripts" xalign 0.49 yalign 0.38 color "#FFF" font "windows-xp-tahoma.ttf" size 35
    text "Key Takeaways" xalign 0.795 yalign 0.38 color "#FFF" font "windows-xp-tahoma.ttf" size 35
    text "RRL" xalign 0.21 yalign 0.675 color "#FFF" font "windows-xp-tahoma.ttf" size 35
    text "Scope of the Study" xalign 0.49 yalign 0.675 color "#FFF" font "windows-xp-tahoma.ttf" size 35
    text "Statistical Graphs" xalign 0.79 yalign 0.675 color "#FFF" font "windows-xp-tahoma.ttf" size 35
    add folder_group
    imagebutton:
        xalign 0.02
        yalign 0.98
        idle "minigame_assets/archie_minigame/open_notes_idle.avif"
        hover "minigame_assets/archie_minigame/open_notes_hover.avif"
        action Show("archie_minigame_notes", transition=easeintop)


#Mirae_Minigame ==============================================================
#Mirae_Minigame ==============================================================
#Mirae_Minigame ==============================================================
default mirae_total_ingredients = 0 #up to 10
default mirae_correct_recipe = False
default mirae_beefcubes = 0
default mirae_butter = 0
default mirae_potatoes = 0
default mirae_currycubes = 0
default mirae_carrots = 0
default mirae_onions = 0

#Selected_Recipe =============================
define recipe_1_ingredients = {"beefcubes": 1, "butter": 1, "potatoes": 2, "currycubes": 2, "carrots": 2, "onions": 2} #Simply Savory Japanese Curry
define recipe_2_ingredients = {"beefcubes": 3, "butter": 2, "potatoes": 1, "currycubes": 2, "carrots": 1, "onions": 1} #Rich and Meaty Japanese Curry
define recipe_3_ingredients = {"beefcubes": 2, "butter": 1, "potatoes": 2, "currycubes": 1, "carrots": 2, "onions": 2} #Balanced Veggie Japanese Curry
default selected_recipe = renpy.random.choice([recipe_1_ingredients, recipe_2_ingredients, recipe_3_ingredients])

#Ingredients =============================
default ingredient_1 = Drag(d ="minigame_assets/mirae_minigame/beefcubes_idle.avif", drag_name = "ingredient_1", draggable = True, align = (0.15,0.1), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae) #Beef Cubes
default ingredient_2 = Drag(d ="minigame_assets/mirae_minigame/butter_idle.avif", drag_name = "ingredient_2", draggable = True, align = (0.5,0.1), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae) #Butter
default ingredient_3 = Drag(d ="minigame_assets/mirae_minigame/potatoes_idle.avif", drag_name = "ingredient_3", draggable = True, align = (0.85,0.1), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae) #Potatoes
default ingredient_4 = Drag(d ="minigame_assets/mirae_minigame/currycubes_idle.avif", drag_name = "ingredient_4", draggable = True, align = (0.15,0.55), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae) #Curry Cubes
default ingredient_5 = Drag(d ="minigame_assets/mirae_minigame/carrots_idle.avif", drag_name = "ingredient_5", draggable = True, align = (0.5,0.55), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae) #Carrots
default ingredient_6 = Drag(d ="minigame_assets/mirae_minigame/onions_idle.avif", drag_name = "ingredient_6", draggable = True, align = (0.85,0.55), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae) #Onions
default cooking_pot = Drag(d ="minigame_assets/mirae_minigame/cooking_pot.avif", drag_name = "cooking_pot", draggable = False, droppable = True, align = (0.5, 1.00), focus_mask = True, mouse_drop = True) #Cooking Pot

#Cooking Group and Screen =============================
default cooking_group = DragGroup(ingredient_1, ingredient_2, ingredient_3, ingredient_4, ingredient_5, ingredient_6, cooking_pot)

screen draggroup_mirae:
    add "dim_effect.avif" alpha 0.8
    add cooking_group
    imagebutton:
        xalign 0.02
        yalign 0.98
        idle "minigame_assets/mirae_minigame/open_recipe_idle.avif"
        hover "minigame_assets/mirae_minigame/open_recipe_hover.avif"
        action If(selected_recipe == recipe_1_ingredients, Show("mirae_minigame_recipe_1", transition=easeintop),
                If(selected_recipe == recipe_2_ingredients, Show("mirae_minigame_recipe_2", transition=easeintop),
                If(selected_recipe == recipe_3_ingredients, Show("mirae_minigame_recipe_3", transition=easeintop))))
    