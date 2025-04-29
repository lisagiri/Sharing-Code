#Put minigames code here

default archie_win_count = 0 #up to 8
default archie_mistake_count = 0 #up to 3

default mirae_beefcubes = 0
default mirae_butter = 0
default mirae_potatoes = 0
default mirae_currycubes = 0
default mirae_carrots = 0
default mirae_onions = 0
default mirae_total_ingredients = 0 #up to 10
default mirae_correct_recipe = False
default mirae_selectedrecipe_variable = False
default mirae_currentingredients_variable = False

init python:
    correct_placements = {
        "paper_1_1": "folder_1",
        "paper_1_2": "folder_2",
        "paper_1_3": "folder_3",
        "paper_1_4": "folder_4",
        "paper_1_5": "folder_5",
        "paper_1_6": "folder_6",
        "paper_2_1": "folder_1",
        "paper_2_2": "folder_2",
        "paper_2_3": "folder_3",
        "paper_2_4": "folder_4",
        "paper_2_5": "folder_5",
        "paper_2_6": "folder_6",
        "paper_3_1": "folder_1",
        "paper_3_2": "folder_2",
        "paper_3_3": "folder_3",
        "paper_3_4": "folder_4",
        "paper_3_5": "folder_5",
        "paper_3_6": "folder_6",
        "paper_4_1": "folder_1",
        "paper_4_2": "folder_2",
        "paper_4_3": "folder_3",
        "paper_4_4": "folder_4",
        "paper_4_5": "folder_5",
        "paper_4_6": "folder_6",
        "paper_5_1": "folder_1",
        "paper_5_2": "folder_2",
        "paper_5_3": "folder_3",
        "paper_5_4": "folder_4",
        "paper_5_5": "folder_5",
        "paper_5_6": "folder_6",
        "paper_6_1": "folder_1",
        "paper_6_2": "folder_2",
        "paper_6_3": "folder_3",
        "paper_6_4": "folder_4",
        "paper_6_5": "folder_5",
        "paper_6_6": "folder_6",
        "paper_7_1": "folder_1",
        "paper_7_2": "folder_2",
        "paper_7_3": "folder_3",
        "paper_7_4": "folder_4",
        "paper_7_5": "folder_5",
        "paper_7_6": "folder_6",
        "paper_8_1": "folder_1",
        "paper_8_2": "folder_2",
        "paper_8_3": "folder_3",
        "paper_8_4": "folder_4",
        "paper_8_5": "folder_5",
        "paper_8_6": "folder_6",
        "paper_9_1": "folder_1",
        "paper_9_2": "folder_2",
        "paper_9_3": "folder_3",
        "paper_9_4": "folder_4",
        "paper_9_5": "folder_5",
        "paper_9_6": "folder_6",
        "paper_10_1": "folder_1",
        "paper_10_2": "folder_2",
        "paper_10_3": "folder_3",
        "paper_10_4": "folder_4",
        "paper_10_5": "folder_5",
        "paper_10_6": "folder_6",
    }

    def drag_function_archie(dragged_items, dropped_on):
        global archie_win_count
        global archie_mistake_count
        if dropped_on is not None:
            dragged_name = dragged_items[0].drag_name
            dropped_name = dropped_on.drag_name
            if dragged_name in correct_placements and correct_placements[dragged_name] == dropped_name:
                if dragged_name.startswith("paper_1_"):
                    folder_group.remove(starting_item1)
                    folder_group.add(starting_item2)
                elif dragged_name.startswith("paper_2_"):
                    folder_group.remove(starting_item2)
                    folder_group.add(starting_item3)
                elif dragged_name.startswith("paper_3_"):
                    folder_group.remove(starting_item3)
                    folder_group.add(starting_item4)
                elif dragged_name.startswith("paper_4_"):
                    folder_group.remove(starting_item4)
                    folder_group.add(starting_item5)
                elif dragged_name.startswith("paper_5_"):
                    folder_group.remove(starting_item5)
                    folder_group.add(starting_item6)
                elif dragged_name.startswith("paper_6_"):
                    folder_group.remove(starting_item6)
                    folder_group.add(starting_item7)
                elif dragged_name.startswith("paper_7_"):
                    folder_group.remove(starting_item7)
                    folder_group.add(starting_item8)
                elif dragged_name.startswith("paper_8_"):
                    folder_group.remove(starting_item8)
                    folder_group.add(starting_item9)
                elif dragged_name.startswith("paper_9_"):
                    folder_group.remove(starting_item9)
                    folder_group.add(starting_item10)
                elif dragged_name.startswith("paper_10_"):
                    folder_group.remove(starting_item10)
                archie_win_count += 1
                renpy.sound.play("audio/Correct.ogg")
                if archie_win_count == 8:
                    renpy.jump("archie_winlose")
            else:
                if dragged_name.startswith("paper_1_"):
                    folder_group.remove(starting_item1)
                    folder_group.add(starting_item2)
                elif dragged_name.startswith("paper_2_"):
                    folder_group.remove(starting_item2)
                    folder_group.add(starting_item3)
                elif dragged_name.startswith("paper_3_"):
                    folder_group.remove(starting_item3)
                    folder_group.add(starting_item4)
                elif dragged_name.startswith("paper_4_"):
                    folder_group.remove(starting_item4)
                    folder_group.add(starting_item5)
                elif dragged_name.startswith("paper_5_"):
                    folder_group.remove(starting_item5)
                    folder_group.add(starting_item6)
                elif dragged_name.startswith("paper_6_"):
                    folder_group.remove(starting_item6)
                    folder_group.add(starting_item7)
                elif dragged_name.startswith("paper_7_"):
                    folder_group.remove(starting_item7)
                    folder_group.add(starting_item8)
                elif dragged_name.startswith("paper_8_"):
                    folder_group.remove(starting_item8)
                    folder_group.add(starting_item9)
                elif dragged_name.startswith("paper_9_"):
                    folder_group.remove(starting_item9)
                    folder_group.add(starting_item10)
                elif dragged_name.startswith("paper_10_"):
                    folder_group.remove(starting_item10)
                archie_mistake_count += 1
                renpy.sound.play("audio/Wrong.ogg")
                if archie_mistake_count == 3:
                    renpy.jump("archie_winlose")

    def drag_function_mirae(dragged_items, dropped_on):
        global mirae_beefcubes
        global mirae_butter
        global mirae_potatoes
        global mirae_currycubes
        global mirae_carrots
        global mirae_onions
        global mirae_total_ingredients
        global mirae_correct_recipe
        global mirae_selectedrecipe_variable
        global mirae_currentingredients_variable
        if dropped_on is not None:
            dragged_name = dragged_items[0].drag_name
            dropped_name = dropped_on.drag_name
            if dragged_name in ["ingredient_1", "ingredient_2", "ingredient_3", "ingredient_4", "ingredient_5", "ingredient_6"] and dropped_name == "cooking_pot":
                if dragged_name == "ingredient_1":
                    dragged_items[0].snap(0.12, 0.065, 0.4)
                    mirae_beefcubes += 1
                elif dragged_name == "ingredient_2":
                    dragged_items[0].snap(0.395, 0.065, 0.4)
                    mirae_butter += 1
                elif dragged_name == "ingredient_3":
                    dragged_items[0].snap(0.675, 0.065, 0.4)
                    mirae_potatoes += 1
                elif dragged_name == "ingredient_4":
                    dragged_items[0].snap(0.12, 0.345, 0.4)
                    mirae_currycubes += 1
                elif dragged_name == "ingredient_5":
                    dragged_items[0].snap(0.395, 0.345, 0.4)
                    mirae_carrots += 1
                elif dragged_name == "ingredient_6":
                    dragged_items[0].snap(0.675, 0.345, 0.4)
                    mirae_onions += 1
                mirae_total_ingredients += 1
                if mirae_total_ingredients == 10:
                    current_ingredients = {
                        "beefcubes": mirae_beefcubes,
                        "butter": mirae_butter,
                        "potatoes": mirae_potatoes,
                        "currycubes": mirae_currycubes,
                        "carrots": mirae_carrots,
                        "onions": mirae_onions,
                    }
                    if selected_recipe == recipe_1_ingredients and current_ingredients == recipe_1_ingredients:
                        mirae_correct_recipe = True
                        renpy.jump("mirae_winlose")
                    if selected_recipe == recipe_2_ingredients and current_ingredients == recipe_2_ingredients:
                        mirae_correct_recipe = True
                        renpy.jump("mirae_winlose")
                    if selected_recipe == recipe_3_ingredients and current_ingredients == recipe_3_ingredients:
                        mirae_correct_recipe = True
                        renpy.jump("mirae_winlose")
          
                    else:
                        mirae_correct_recipe = False
                        renpy.jump("mirae_winlose")
                    
    def play_drag_activated_sound(dragged_items):
        renpy.sound.play("audio/Paper.ogg")
#Archie_Minigame ==============================================================
#Starting_Item_Options List
    starting_item_options1 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_1_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_1_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_1_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_1_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_1_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_1_6"},
    ]
    starting_item_options2 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_2_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_2_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_2_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_2_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_2_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_2_6"},
    ]
    starting_item_options3 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_3_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_3_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_3_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_3_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_3_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_3_6"},
    ]
    starting_item_options4 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_4_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_4_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_4_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_4_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_4_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_4_6"},
    ]
    starting_item_options5 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_5_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_5_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_5_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_5_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_5_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_5_6"},
    ]
    starting_item_options6 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_6_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_6_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_6_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_6_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_6_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_6_6"},
    ]
    starting_item_options7 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_7_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_7_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_7_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_7_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_7_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_7_6"},
    ]
    starting_item_options8 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_8_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_8_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_8_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_8_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_8_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_8_6"},
    ]
    starting_item_options9 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_9_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_9_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_9_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_9_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_9_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_9_6"},
    ]
    starting_item_options10 = [
    {"image": "minigame_assets/archie_minigame/paper_1.avif", "drag_name": "paper_10_1"},
    {"image": "minigame_assets/archie_minigame/paper_2.avif", "drag_name": "paper_10_2"},
    {"image": "minigame_assets/archie_minigame/paper_3.avif", "drag_name": "paper_10_3"},
    {"image": "minigame_assets/archie_minigame/paper_4.avif", "drag_name": "paper_10_4"},
    {"image": "minigame_assets/archie_minigame/paper_5.avif", "drag_name": "paper_10_5"},
    {"image": "minigame_assets/archie_minigame/paper_6.avif", "drag_name": "paper_10_6"},
    ]
        
#Folders
    #Applied Theories
default folder_1 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_1", draggable = False, droppable = True, align = (0.15,0.1), focus_mask = True, mouse_drop = True)
    #FGD Transcripts
default folder_2 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_2", draggable = False, droppable = True, align = (0.5,0.1), focus_mask = True, mouse_drop = True)
    #Key Takeaways
default folder_3 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_3", draggable = False, droppable = True, align = (0.85,0.1), focus_mask = True, mouse_drop = True)
    #RRL
default folder_4 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_4", draggable = False, droppable = True, align = (0.15,0.55), focus_mask = True, mouse_drop = True)
    #Scope of the Research
default folder_5 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_5", draggable = False, droppable = True, align = (0.5,0.55), focus_mask = True, mouse_drop = True)
    #Statistical Graph
default folder_6 = Drag(d ="minigame_assets/archie_minigame/folder_idle.avif", drag_name = "folder_6", draggable = False, droppable = True, align = (0.85,0.55), focus_mask = True, mouse_drop = True)

    #Selected Item
default selected_item1 = renpy.random.choice(starting_item_options1)
default selected_item2 = renpy.random.choice(starting_item_options2)
default selected_item3 = renpy.random.choice(starting_item_options3)
default selected_item4 = renpy.random.choice(starting_item_options4)
default selected_item5 = renpy.random.choice(starting_item_options5)
default selected_item6 = renpy.random.choice(starting_item_options6)
default selected_item7 = renpy.random.choice(starting_item_options7)
default selected_item8 = renpy.random.choice(starting_item_options8)
default selected_item9 = renpy.random.choice(starting_item_options9)
default selected_item10 = renpy.random.choice(starting_item_options10)

    #Starting Item
default starting_item1 = Drag(d=selected_item1["image"], drag_name=selected_item1["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item2 = Drag(d=selected_item2["image"], drag_name=selected_item2["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item3 = Drag(d=selected_item3["image"], drag_name=selected_item3["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item4 = Drag(d=selected_item4["image"], drag_name=selected_item4["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item5 = Drag(d=selected_item5["image"], drag_name=selected_item5["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item6 = Drag(d=selected_item6["image"], drag_name=selected_item6["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item7 = Drag(d=selected_item7["image"], drag_name=selected_item7["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item8 = Drag(d=selected_item8["image"], drag_name=selected_item8["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item9 = Drag(d=selected_item9["image"], drag_name=selected_item9["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)
default starting_item10 = Drag(d=selected_item10["image"], drag_name=selected_item10["drag_name"], dragged = drag_function_archie, draggable=True, droppable=False, align=(0.5, 0.98), focus_mask = True, mouse_drop = True, activated = play_drag_activated_sound)

    #Folder Group
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

#Simply Savory Japanese Curry
define recipe_1_ingredients = {"beefcubes": 1, "butter": 1, "potatoes": 2, "currycubes": 2, "carrots": 2, "onions": 2}
#Rich and Meaty Japanese Curry
define recipe_2_ingredients = {"beefcubes": 3, "butter": 2, "potatoes": 1, "currycubes": 2, "carrots": 1, "onions": 1}
#Balanced Veggie Japanese Curry
define recipe_3_ingredients = {"beefcubes": 2, "butter": 1, "potatoes": 2, "currycubes": 1, "carrots": 2, "onions": 2}

default selected_recipe = renpy.random.choice([recipe_1_ingredients, recipe_2_ingredients, recipe_3_ingredients])

#Ingredients
    #Beef Cubes
default ingredient_1 = Drag(d ="minigame_assets/mirae_minigame/beefcubes_idle.avif", drag_name = "ingredient_1", draggable = True, align = (0.15,0.1), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae)
    #Butter
default ingredient_2 = Drag(d ="minigame_assets/mirae_minigame/butter_idle.avif", drag_name = "ingredient_2", draggable = True, align = (0.5,0.1), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae)
    #Potatoes
default ingredient_3 = Drag(d ="minigame_assets/mirae_minigame/potatoes_idle.avif", drag_name = "ingredient_3", draggable = True, align = (0.85,0.1), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae)
    #Curry Cubes
default ingredient_4 = Drag(d ="minigame_assets/mirae_minigame/currycubes_idle.avif", drag_name = "ingredient_4", draggable = True, align = (0.15,0.55), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae)
    #Carrots
default ingredient_5 = Drag(d ="minigame_assets/mirae_minigame/carrots_idle.avif", drag_name = "ingredient_5", draggable = True, align = (0.5,0.55), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae)
    #Onions
default ingredient_6 = Drag(d ="minigame_assets/mirae_minigame/onions_idle.avif", drag_name = "ingredient_6", draggable = True, align = (0.85,0.55), focus_mask = True, mouse_drop = True, dragged = drag_function_mirae)

    #Cooking Pot
default cooking_pot = Drag(d ="minigame_assets/mirae_minigame/cooking_pot.avif", drag_name = "cooking_pot", draggable = False, droppable = True, align = (0.5, 1.00), focus_mask = True, mouse_drop = True)
    #Cooking Group
default cooking_group = DragGroup(ingredient_1, ingredient_2, ingredient_3, ingredient_4, ingredient_5, ingredient_6, cooking_pot)

screen draggroup_mirae:
    add "dim_effect.avif" alpha 0.8
    add cooking_group
    imagebutton:
        xalign 0.02
        yalign 0.98
        idle "minigame_assets/mirae_minigame/open_recipe_idle.avif"
        hover "minigame_assets/mirae_minigame/open_recipe_hover.avif"
        # action Show("archie_minigame_recipe", transition=easeintop)
        action If(
                selected_recipe == recipe_1_ingredients,
                Show("mirae_minigame_recipe_1", transition=easeintop),
                If(
                    selected_recipe == recipe_2_ingredients,
                    Show("mirae_minigame_recipe_2", transition=easeintop),
                    If(
                        selected_recipe == recipe_3_ingredients,
                        Show("mirae_minigame_recipe_3", transition=easeintop)
                    )
                )
            )
    
