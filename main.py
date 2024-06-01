import random
import pygame
import sys
from button import ImageButton
from game_config import *
from tools import i_counter as i_c

pygame.init()

i_counter = i_c.InitiativeCounter()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TTRPG Assist")
icon = pygame.image.load("Icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# Далее куча функций создающие разные меню
# К каждой меню прилагается функция <Название>_button,
# она генерит кнопки, нужно для адекватного отображения после
# изменения настроек звука или размера окна

def create_main_menu_buttons():
    # Кнопки сюда, потом обновить в местах нужных
    DnD_button = ImageButton(width_ic, 0, width_ic, height_ic, "", DnD_im1, DnD_im2, "sound/test_sound1.mp3", vol)
    CyberRed_button = ImageButton(width_ic * 2, 0, width_ic, height_ic, "", CR_im1, CR_im2, "sound/test_sound1.mp3", vol)
    Initiative_button = ImageButton(width_ic * 3, 0, width_ic, height_ic, "", Init_im1, Init_im2,
                                    "sound/test_sound1.mp3", vol)
    Save_button = ImageButton(width_ic * 4, 0, width_ic, height_ic, "", Save_im1, Save_im2, "sound/test_sound1.mp3", vol)
    Settings_button = ImageButton(0, 0, width_ic, height_ic, "", Settings_im1, Settings_im2, "sound/test_sound1.mp3",
                                  vol)
    # Вот тут например
    return CyberRed_button, Initiative_button, DnD_button, Save_button, Settings_button

def main_menu():
    CyberRed_button, Initiative_button, DnD_button, Save_button, Settings_button = create_main_menu_buttons()
    Buttons = [CyberRed_button, Initiative_button, DnD_button, Save_button, Settings_button]
    prev_vol = 0
    prev_W = 0
    while True:
        screen.fill((0,0,0))
        screen.blit(main_background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                fade()
                setting_menu()

            #Обработка нажатия на кнопку
            if event.type == pygame.USEREVENT and event.button == Settings_button:
                print("Настройки")
                fade()
                setting_menu()

            if event.type == pygame.USEREVENT and event.button == DnD_button:
                print("DnD_button down")
                fade()
                DnD_menu()

            if event.type == pygame.USEREVENT and event.button == CyberRed_button:
                print("CyberRed_button down")
                fade()
                Cyberpunk_menu()

            if event.type == pygame.USEREVENT and event.button == Initiative_button:
                print("Initiative_button down")
                fade()
                Innitiative_menu()

            for btn in Buttons:
                btn.handle_event(event)

        if vol != prev_vol or prev_W != Width:
            CyberRed_button, Initiative_button, DnD_button, Save_button, Settings_button = create_main_menu_buttons()
            Buttons = [CyberRed_button, Initiative_button, DnD_button, Save_button, Settings_button]
            prev_vol = vol
            prev_W = Width
        #update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

### Cyberpunk Red menu ###

def create_Cyberpunk_menu_buttons():
    DnD_button = ImageButton(width_ic, 0, width_ic, height_ic, "", DnD_im1, DnD_im2, "sound/test_sound1.mp3", vol)
    CyberRed_button = ImageButton(width_ic * 2, 0, width_ic, height_ic, "", CR_im1, CR_im2, "sound/test_sound1.mp3", vol)
    Initiative_button = ImageButton(width_ic * 3, 0, width_ic, height_ic, "", Init_im1, Init_im2,
                                    "sound/test_sound1.mp3", vol)
    Save_button = ImageButton(width_ic * 4, 0, width_ic, height_ic, "", Save_im1, Save_im2, "sound/test_sound1.mp3", vol)
    cr_Meat_button = ImageButton(0, height_ic, width_ic * 6, height_ic * 4, "", "image/C_menu/meat.png", "image/C_menu/meat_h.png",
                                  "sound/test_sound1.mp3", vol)
    cr_Monster_edit_button = ImageButton(0, height_ic + height_ic * 4, width_ic * 6, height_ic * 4, "", "image/C_menu/red.png", "image/C_menu/red_h.png",
                                      "sound/test_sound1.mp3", vol)
    cr_Ars_button = ImageButton(width_ic * 6, height_ic, width_ic * 4, height_ic * 4, "", "image/C_menu/a.png", "image/C_menu/a_h.png",
                                "sound/test_sound1.mp3", vol)
    cr_Ayg_button = ImageButton(width_ic * 6, height_ic + height_ic * 4, width_ic * 4, height_ic * 4, "", "image/C_menu/ayg.png",
                                  "image/C_menu/ayg_h.png", "sound/test_sound1.mp3", vol)
    cr_Char_edit_button = ImageButton(width_ic * 6 + width_ic * 4, 0, width_ic * 6, Height, "", "image/C_menu/l.png", "image/C_menu/l_h.png",
                                   "sound/test_sound1.mp3", vol)
    Settings_button = ImageButton(0, 0, width_ic, height_ic, "", Settings_im1, Settings_im2, "sound/test_sound1.mp3",
                                  vol)
    return DnD_button, CyberRed_button, Initiative_button, Save_button, cr_Meat_button, cr_Monster_edit_button, cr_Ars_button, cr_Ayg_button, cr_Char_edit_button, Settings_button

def Cyberpunk_menu():
    DnD_button, CyberRed_button, Initiative_button, Save_button, cr_Bestiary_button, cr_Monster_edit_button, cr_Spells_button, cr_Items_button, cr_Char_edit_button, Settings_button = create_Cyberpunk_menu_buttons()
    Buttons = [DnD_button, CyberRed_button, Initiative_button, Save_button, cr_Bestiary_button, cr_Monster_edit_button, cr_Spells_button, cr_Items_button, cr_Char_edit_button, Settings_button]

    prev_W = 0
    prev_vol = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка нажатия на кнопку
            if event.type == pygame.USEREVENT and event.button == Settings_button:
                print("Настройки")
                fade()
                setting_menu()

            if event.type == pygame.USEREVENT and event.button == CyberRed_button:
                print("CyberRed_button down")
                running = False

            if event.type == pygame.USEREVENT and event.button == DnD_button:
                print("DnD_button down")
                fade()
                DnD_menu()
                running = False

            if event.type == pygame.USEREVENT and event.button == Initiative_button:
                print("Initiative_button down")
                fade()
                Innitiative_menu()
                running = False

            if event.type == pygame.USEREVENT and event.button == cr_Char_edit_button:
                fade()
                print("Char_edit - CYBER")

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            for btn in Buttons:
                btn.handle_event(event)

        # Апдейт кнопок
        if vol != prev_vol or prev_W != Width:
            DnD_button, CyberRed_button, Initiative_button, Save_button, cr_Bestiary_button, cr_Monster_edit_button, cr_Spells_button, cr_Items_button, cr_Char_edit_button, Settings_button = create_Cyberpunk_menu_buttons()
            Buttons = [DnD_button, CyberRed_button, Initiative_button, Save_button, cr_Bestiary_button, cr_Monster_edit_button, cr_Spells_button, cr_Items_button, cr_Char_edit_button, Settings_button]
            prev_vol = vol
            prev_W = Width

        # update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

### Inittiative ###
def create_Innitiatiave_menu_button():
    back_button = ImageButton(Width - width_ic * 2, Height - height_ic, width_ic * 2, height_ic, "", "image/n_h/back.png",
                              "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    d20_button_plus = ImageButton(width_ic / 10, height_ic * 1.5 + height_ic / 10, width_ic, height_ic, "20",
                                  "image/Dices/20.png", "image/Dices/20.png", "sound/plop-11.mp3", vol)
    d12_button_plus = ImageButton(width_ic * 12 / 10, height_ic * 1.5 + height_ic / 10, width_ic, height_ic, "12",
                                  "image/Dices/12.png", "image/Dices/12.png", "sound/plop-11.mp3", vol)
    d10_button_plus = ImageButton(width_ic * 23 / 10, height_ic * 1.5 + height_ic / 10, width_ic, height_ic, "0",
                                  "image/Dices/10.png", "image/Dices/10.png", "sound/plop-11.mp3", vol)
    d8_button_plus = ImageButton(width_ic * 34 / 10, height_ic * 1.5 + height_ic / 10, width_ic, height_ic, "8",
                                 "image/Dices/8.png", "image/Dices/8.png", "sound/plop-11.mp3", vol)
    d6_button_plus = ImageButton(width_ic * 12 / 10, 27 * height_ic / 10, width_ic, height_ic, "6",
                                 "image/Dices/6.png", "image/Dices/6.png", "sound/plop-11.mp3", vol)
    d4_button_plus = ImageButton(width_ic * 23 / 10, 27 * height_ic / 10, width_ic, height_ic, "4",
                                 "image/Dices/4.png", "image/Dices/4.png", "sound/plop-11.mp3", vol)
    d20_button = ImageButton(width_ic * 12 / 10, 4 * height_ic, width_ic, height_ic, "", "image/Dices/20.png",
                             "image/Dices/20.png", "sound/podbor.mp3", vol)
    d12_button = ImageButton(width_ic * 23 / 10, 4 * height_ic, width_ic, height_ic, "", "image/Dices/12.png",
                             "image/Dices/12.png", "sound/podbor.mp3", vol)
    d10_button = ImageButton(width_ic / 10, 5 * height_ic + height_ic / 10, width_ic, height_ic, "",
                             "image/Dices/10.png", "image/Dices/10.png", "sound/podbor.mp3", vol)
    d8_button = ImageButton(width_ic * 12 / 10, 5 * height_ic + height_ic / 10, width_ic, height_ic, "",
                            "image/Dices/8.png", "image/Dices/8.png", "sound/podbor.mp3", vol)
    d6_button = ImageButton(width_ic * 23 / 10, 5 * height_ic + height_ic / 10, width_ic, height_ic, "",
                            "image/Dices/6.png", "image/Dices/6.png", "sound/podbor.mp3", vol)
    d4_button = ImageButton(width_ic * 34 / 10, 5 * height_ic + height_ic / 10, width_ic, height_ic, "",
                            "image/Dices/4.png", "image/Dices/4.png", "sound/podbor.mp3", vol)
    roll_button = ImageButton(width_ic * 1.3, Height - height_ic * 1.2, width_ic * 2, height_ic, "Roll",
                              "image/n_h/nothing.png", "image/h/nothing_hovered.png", "sound/roll-dice.mp3", vol)
    plus_button_enemy = ImageButton(width_ic * 9.6, Height - height_ic, width_ic, height_ic, "", "image/Plus.png", "image/Plus.png", "sound/test_sound1.mp3")
    plus_button_friend = ImageButton(width_ic * 10.6, Height - height_ic, width_ic, height_ic, "", "image/Plus_green.png", "image/Plus_green.png", "sound/test_sound1.mp3")
    sort_button = ImageButton(width_ic * 11.8, Height - height_ic, width_ic * 2, height_ic, "", "image/n_h/sort.png", "image/h/sort_hovered.png", "sound/test_sound1.mp3")
    kill_button = ImageButton(width_ic * 7.4, Height - height_ic, width_ic * 2, height_ic, "", "image/n_h/kill.png", "image/h/kill_h.png", "sound/test_sound1.mp3")
    clear_button = ImageButton(width_ic * 5.2, Height - height_ic, width_ic * 2, height_ic, "", "image/n_h/clear.png", "image/h/clear_h.png", "sound/test_sound1.mp3")
    return back_button, d20_button_plus, d12_button_plus, d10_button_plus, d8_button_plus, d6_button_plus, d4_button_plus, d20_button, d12_button, d10_button, d8_button, d6_button, d4_button, roll_button, plus_button_enemy, plus_button_friend, sort_button, clear_button, kill_button

def Innitiative_menu():
    prev_vol = 0
    prev_W = 0
    result = 0

    back_button, d20_button_plus, d12_button_plus, d10_button_plus, d8_button_plus, d6_button_plus, d4_button_plus, d20_button, d12_button, d10_button, d8_button, d6_button, d4_button, roll_button, plus_button_enemy, plus_button_friend, sort_button, clear_button, kill_button = create_Innitiatiave_menu_button()
    Buttons = [back_button, d20_button_plus, d12_button_plus, d10_button_plus, d8_button_plus, d6_button_plus, d4_button_plus, d20_button, d12_button, d10_button, d8_button, d6_button, d4_button, roll_button, plus_button_enemy, plus_button_friend, sort_button, clear_button, kill_button]

    counter = [0, 0, 0, 0, 0, 0]
    d_array = [20, 12, 10, 8, 6, 4]

    if Width == 960:
        size, size2 = 42, 28
    else:
        if Width == 1280:
            size, size2 = 62, 46
        else: size, size2 = 82, 64

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        i_counter.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i_counter.to_edit == None:
                if event.type == pygame.KEYDOWN:
                    # Возврат в меню
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    i_counter.handle_click(event.pos, screen)

                if event.type == pygame.USEREVENT and event.button == back_button:
                    fade()
                    running = False

                if event.type == pygame.USEREVENT and event.button == plus_button_enemy:
                    i_counter.add_row(False)

                if event.type == pygame.USEREVENT and event.button == plus_button_friend:
                    i_counter.add_row(True)

                if event.type == pygame.USEREVENT and event.button == clear_button:
                    i_counter.delete_all_rows()

                if event.type == pygame.USEREVENT and event.button == kill_button:
                    i_counter.kill_zero()

                if event.type == pygame.USEREVENT and event.button == sort_button:
                    i_counter.sort()

                # Обработка Roll
                if event.type == pygame.USEREVENT and event.button == d20_button and counter[0] > 0:
                    counter[0] -= 1
                if event.type == pygame.USEREVENT and event.button == d12_button and counter[1] > 0:
                    counter[1] -= 1
                if event.type == pygame.USEREVENT and event.button == d10_button and counter[2] > 0:
                    counter[2] -= 1
                if event.type == pygame.USEREVENT and event.button == d8_button and counter[3] > 0:
                    counter[3] -= 1
                if event.type == pygame.USEREVENT and event.button == d6_button and counter[4] > 0:
                    counter[4] -= 1
                if event.type == pygame.USEREVENT and event.button == d4_button and counter[5] > 0:
                    counter[5] -= 1

                if event.type == pygame.USEREVENT and event.button == d20_button_plus:
                    counter[0] += 1
                if event.type == pygame.USEREVENT and event.button == d12_button_plus:
                    counter[1] += 1
                if event.type == pygame.USEREVENT and event.button == d10_button_plus:
                    counter[2] += 1
                if event.type == pygame.USEREVENT and event.button == d8_button_plus:
                    counter[3] += 1
                if event.type == pygame.USEREVENT and event.button == d6_button_plus:
                    counter[4] += 1
                if event.type == pygame.USEREVENT and event.button == d4_button_plus:
                    counter[5] += 1

                if event.type == pygame.USEREVENT and event.button == roll_button:
                    result = 0
                    for i in range(0, 6):
                        if counter[i] != 0:
                            for j in range(0, counter[i]):
                                print(counter[i], " ", d_array[i])
                                result += random.randint(1, d_array[i])

                for btn in Buttons:
                    btn.handle_event(event)
            ###Тут Редактирование текста###
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    i_counter.handle_click(event.pos, screen)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        need_put_in = False
                    elif event.key == pygame.K_RETURN:
                        need_put_in = False
                    else:
                        row = i_counter.rows[i_counter.to_edit[1]]
                        i_counter.edit_your_put_in(i_counter.to_edit[0], event.unicode, row)

        font = pygame.font.SysFont(main_font, size)
        text_init = font.render("Инициатива", True, (255, 205, 205))
        screen.blit(text_init, (10,10))
        pygame.draw.rect(screen, (175, 60, 30), (-20, height_ic * 1.5 - 3, Width / 4 + width_ic, Height + 20), 8)
        pygame.draw.rect(screen, (50, 25, 20), (-20, height_ic * 1.5 + 5, Width / 4 + width_ic - 8, Height))
        pygame.draw.line(screen, (175, 60, 30), (width_ic / 10 + width_ic / 2, height_ic * 1.5 + 2 * height_ic / 10 + height_ic), (width_ic / 10 + width_ic / 2, height_ic * 1.5 + 2 * height_ic / 10 + 2 * height_ic), 6)
        pygame.draw.line(screen, (175, 60, 30), (width_ic / 10 + width_ic, height_ic * 2 + 2 * height_ic / 10 + height_ic), (width_ic / 10, height_ic * 2 + 2 * height_ic / 10 + height_ic), 6)
        pygame.draw.line(screen, (175, 60, 30), (width_ic / 10 + width_ic, 4.45 * height_ic), (width_ic / 10, 4.45 * height_ic), 6)
        pygame.draw.line(screen, (175, 60, 30), (0, 3.85 * height_ic), (4.73 * width_ic, 3.85 * height_ic), 8)
        img = pygame.image.load("image/n_h/nothing.png")
        img = pygame.transform.scale(img, (width_ic * 3, height_ic))
        img_rect = (width_ic * 0.8, Height - height_ic * 2.3)
        screen.blit(img, img_rect)

        text_init = font.render(str(result), True, (255, 255, 255))
        screen.blit(text_init, (width_ic, Height - height_ic * 2.3))


        # Апдейт кнопок
        if vol != prev_vol or prev_W != Width:
            back_button, d20_button_plus, d12_button_plus, d10_button_plus, d8_button_plus, d6_button_plus, d4_button_plus, d20_button, d12_button, d10_button, d8_button, d6_button, d4_button, roll_button, plus_button_enemy, plus_button_friend, sort_button, clear_button, kill_button = create_Innitiatiave_menu_button()
            Buttons = [back_button, d20_button_plus, d12_button_plus, d10_button_plus, d8_button_plus, d6_button_plus, d4_button_plus, d20_button, d12_button, d10_button, d8_button, d6_button, d4_button, roll_button, plus_button_enemy, plus_button_friend, sort_button, clear_button, kill_button]
            prev_vol = vol
            prev_W = Width

        # update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        font2 = pygame.font.SysFont(main_font, size2)
        text_d20 = font2.render(str(counter[0]), True, (0, 0, 0))
        text_d12 = font2.render(str(counter[1]), True, (0, 0, 0))
        text_d10 = font2.render(str(counter[2]), True, (0, 0, 0))
        text_d8 = font2.render(str(counter[3]), True, (0, 0, 0))
        text_d6 = font2.render(str(counter[4]), True, (0, 0, 0))
        text_d4 = font2.render(str(counter[5]), True, (0, 0, 0))
        screen.blit(text_d20, (width_ic * 1.462, 4.1 * height_ic))
        screen.blit(text_d12, (width_ic * 2.562, 4.1 * height_ic))
        screen.blit(text_d10, (width_ic * 1.462 - width_ic * 1.1, 5.2 * height_ic))
        screen.blit(text_d8, (width_ic * 1.462, 5.2 * height_ic))
        screen.blit(text_d6, (width_ic * 2.562, 5.2 * height_ic))
        screen.blit(text_d4, (width_ic * 3.662, 5.2 * height_ic))

        pygame.display.flip()

### DnD_menu ###

def create_DnD_menu_buttons():
    DnD_button = ImageButton(width_ic, 0, width_ic, height_ic, "", DnD_im1, DnD_im2, "sound/test_sound1.mp3", vol)
    CyberRed_button = ImageButton(width_ic * 2, 0, width_ic, height_ic, "", CR_im1, CR_im2, "sound/test_sound1.mp3", vol)
    Initiative_button = ImageButton(width_ic * 3, 0, width_ic, height_ic, "", Init_im1, Init_im2, "sound/test_sound1.mp3", vol)
    Save_button = ImageButton(width_ic * 4, 0, width_ic, height_ic, "", Save_im1, Save_im2, "sound/test_sound1.mp3", vol)
    Bestiary_button = ImageButton(0, height_ic, width_ic * 6, height_ic * 4, "", Bestiary_im1, Bestiary_im2, "sound/test_sound1.mp3", vol)
    Monster_edit_button = ImageButton(0, height_ic + height_ic * 4, width_ic * 6, height_ic * 4, "", M_e_im1, M_e_im2, "sound/test_sound1.mp3", vol)
    Spells_button = ImageButton(width_ic * 6, height_ic, width_ic * 4, height_ic * 4, "", Spells_im1, Spells_im2, "sound/test_sound1.mp3", vol)
    Items_button = ImageButton(width_ic * 6, height_ic + height_ic * 4, width_ic * 4, height_ic * 4, "", Item_im1, Item_im2, "sound/test_sound1.mp3", vol)
    Char_edit_button = ImageButton(width_ic * 6 + width_ic * 4, 0, width_ic * 6, Height, "", C_e_im1, C_e_im2,"sound/test_sound1.mp3", vol)
    Settings_button = ImageButton(0, 0, width_ic, height_ic, "", Settings_im1, Settings_im2, "sound/test_sound1.mp3", vol)
    return DnD_button, CyberRed_button, Initiative_button, Save_button, Bestiary_button, Monster_edit_button, Spells_button, Items_button, Char_edit_button, Settings_button

def DnD_menu():
    DnD_button, CyberRed_button, Initiative_button, Save_button, Bestiary_button, Monster_edit_button, Spells_button, Items_button, Char_edit_button, Settings_button = create_DnD_menu_buttons()
    Buttons = [DnD_button, CyberRed_button, Initiative_button, Save_button, Bestiary_button, Monster_edit_button, Spells_button, Items_button, Char_edit_button, Settings_button]

    prev_W = 0
    prev_vol = 0

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(main_background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Обработка нажатия на кнопку
            if event.type == pygame.USEREVENT and event.button == Settings_button:
                print("Настройки")
                fade()
                setting_menu()

            if event.type == pygame.USEREVENT and event.button == DnD_button:
                print("DnD_button down")
                running = False

            if event.type == pygame.USEREVENT and event.button == CyberRed_button:
                print("CyberRed_button down")
                fade()
                Cyberpunk_menu()
                running = False

            if event.type == pygame.USEREVENT and event.button == Initiative_button:
                print("Initiative_button down")
                fade()
                Innitiative_menu()
                running = False

            if event.type == pygame.USEREVENT and event.button == Items_button:
                print("Items_button down")
                fade()
                DnD_Inv_menu()

            if event.type == pygame.USEREVENT and event.button == Char_edit_button:
                print("Char_edit_button down")
                fade()
                DnD_char_edit_menu()

            if event.type == pygame.KEYDOWN:
                #Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            for btn in Buttons:
                btn.handle_event(event)

        #Апдейт кнопок
        if vol != prev_vol or prev_W != Width:
            DnD_button, CyberRed_button, Initiative_button, Save_button, Bestiary_button, Monster_edit_button, Spells_button, Items_button, Char_edit_button, Settings_button = create_DnD_menu_buttons()
            Buttons = [DnD_button, CyberRed_button, Initiative_button, Save_button, Bestiary_button, Monster_edit_button, Spells_button, Items_button, Char_edit_button, Settings_button]
            prev_vol = vol
            prev_W = Width

        #update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

### DnD_char_edit_menu ###
def create_DnD_char_edit_menu_buttons():
    back_button = ImageButton(Width - width_ic * 2, Height - height_ic, width_ic * 2, height_ic, "", "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    comming_soon_button = ImageButton(width_ic, height_ic, Width - width_ic * 3, Height - height_ic * 2, "", "image/coming_soon.png", "image/coming_soon.png", "sound/rick.mp3", vol)
    return back_button, comming_soon_button

def DnD_char_edit_menu():

    prev_vol = 0
    prev_W = 0

    back_button, comming_soon_button = create_DnD_char_edit_menu_buttons()
    Buttons = [back_button, comming_soon_button]

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in Buttons:
                btn.handle_event(event)
        #Апдейт кнопок
        if vol != prev_vol or prev_W != Width:
            back_button, comming_soon_button = create_DnD_char_edit_menu_buttons()
            Buttons = [back_button, comming_soon_button]
            prev_vol = vol
            prev_W = Width

        #update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

### DnD_Inventory ###

def create_DnD_Inv_menu_buttons():
    weapon_button = ImageButton(0, 0, width_ic * 3, height_ic, "", "image/n_h/weapon.png", "image/h/weapon_hovered.png", "sound/test_sound1.mp3",
                                vol)
    simple_items_button = ImageButton(width_ic * 3, 0, width_ic * 3, height_ic, "", "image/n_h/item1.png", "image/h/item1_hovered.png", "sound/test_sound1.mp3",
                                      vol)
    mg_inv_button = ImageButton(width_ic * 6, 0, width_ic * 3, height_ic, "", "image/n_h/magic_items.png", "image/h/magic_items_hovered.png", "sound/test_sound1.mp3",
                                vol)
    back_button = ImageButton(Width - width_ic * 1.6, Height - height_ic * 0.8, width_ic * 1.6, height_ic * 0.8, "", "image/n_h/back.png",
                              "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    return weapon_button, simple_items_button, mg_inv_button, back_button

def DnD_Inv_menu():

    prev_vol = 0
    prev_W = 0

    weapon_button, simple_items_button, mg_inv_button, back_button = create_DnD_Inv_menu_buttons()
    Buttons = [weapon_button, simple_items_button, mg_inv_button, back_button]

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            if event.type == pygame.USEREVENT and event.button == weapon_button:
                fade()
                DnD_Inv_1_menu()
            if event.type == pygame.USEREVENT and event.button == simple_items_button:
                fade()
                DnD_Inv_2_menu()
            if event.type == pygame.USEREVENT and event.button == mg_inv_button:
                fade()
                DnD_Inv_3_menu()

            for btn in Buttons:
                btn.handle_event(event)
        # Апдейт кнопок
        if vol != prev_vol or prev_W != Width:
            weapon_button, simple_items_button, mg_inv_button, back_button = create_DnD_Inv_menu_buttons()
            Buttons = [weapon_button, simple_items_button, mg_inv_button, back_button]
            prev_vol = vol
            prev_W = Width

        # update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def create_DnD_Inv_1_menu_buttons():
    arrow_left_button = ImageButton(0, (Height - height_ic) / 2, width_ic, height_ic, "", "image/n_h/arrow_l.png",
                              "image/h/arrow_l.png", "sound/test_sound1.mp3",
                                    vol)
    arrow_right_button = ImageButton(Width - width_ic, (Height - height_ic) / 2, width_ic, height_ic, "", "image/n_h/arrow_r.png",
                              "image/h/arrow_r.png", "sound/test_sound1.mp3",
                                     vol)
    back_button = ImageButton(Width - width_ic * 1.6, Height - height_ic * 0.8, width_ic * 1.6, height_ic * 0.8, "", "image/n_h/back.png",
                              "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    weapon_button = ImageButton(0, 0, width_ic * 3, height_ic, "", "image/n_h/weapon.png", "image/h/weapon_hovered.png",
                                "sound/test_sound1.mp3",
                                vol)
    simple_items_button = ImageButton(width_ic * 3, 0, width_ic * 3, height_ic, "", "image/n_h/item1.png",
                                      "image/h/item1_hovered.png", "sound/test_sound1.mp3",
                                      vol)
    mg_inv_button = ImageButton(width_ic * 6, 0, width_ic * 3, height_ic, "", "image/n_h/magic_items.png",
                                "image/h/magic_items_hovered.png", "sound/test_sound1.mp3",
                                vol)
    return arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button

def DnD_Inv_1_menu():
    arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button = create_DnD_Inv_1_menu_buttons()
    Buttons = [arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button]

    prev_W = 0
    prev_vol = 0

    weapon_image = pygame.image.load("image/Weapons/Weapon1.png")
    counter = 1
    weapon_image_rect = (Width - width_ic * 14.5, Height - height_ic * 7.8)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        weapon_image = pygame.transform.scale(weapon_image, (Width - width_ic * 3, Height - height_ic * 2))
        screen.blit(weapon_image, weapon_image_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка нажатия на кнопку
            if event.type == pygame.USEREVENT and event.button == arrow_right_button:
                print("Arrow_right down")
                if counter < 4:
                    counter += 1
                    weapon_image = pygame.image.load(f"image/Weapons/Weapon{counter}.png")
                #>>>>>>>>>>>>>>>>

            if event.type == pygame.USEREVENT and event.button == arrow_left_button:
                print("arrow_left down")
                if counter > 1:
                    counter -= 1
                    weapon_image = pygame.image.load(f"image/Weapons/Weapon{counter}.png")
                #<<<<<<<<<<<<<<<<

            if event.type == pygame.USEREVENT and event.button == weapon_button:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == simple_items_button:
                fade()
                DnD_Inv_2_menu()
                running = False

            if event.type == pygame.USEREVENT and event.button == mg_inv_button:
                fade()
                DnD_Inv_3_menu()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in Buttons:
                btn.handle_event(event)

        # Апдейт кнопок
        if vol != prev_vol or prev_W != Width:
            arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button = create_DnD_Inv_1_menu_buttons()
            Buttons = [arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button]
            prev_vol = vol
            prev_W = Width

        # update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def DnD_Inv_2_menu():
    arrow_left_button, arrow_right_button, back_button, weapon_button, simple_items_button, mg_inv_button = create_DnD_Inv_1_menu_buttons()
    Buttons = [arrow_left_button, arrow_right_button, back_button, weapon_button, simple_items_button, mg_inv_button]

    prev_W = 0
    prev_vol = 0

    weapon_image = pygame.image.load("image/Items/Item1.png")
    counter = 1
    weapon_image_rect = (Width - width_ic * 14.5, Height - height_ic * 7.8)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        weapon_image = pygame.transform.scale(weapon_image, (Width - width_ic * 3, Height - height_ic * 2))
        screen.blit(weapon_image, weapon_image_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка нажатия на кнопку
            if event.type == pygame.USEREVENT and event.button == arrow_right_button:
                print("Arrow_right down")
                if counter < 6:
                    counter += 1
                    weapon_image = pygame.image.load(f"image/Items/Item{counter}.png")
                # >>>>>>>>>>>>>>>>

            if event.type == pygame.USEREVENT and event.button == arrow_left_button:
                print("arrow_left down")
                if counter > 1:
                    counter -= 1
                    weapon_image = pygame.image.load(f"image/Items/Item{counter}.png")
                # <<<<<<<<<<<<<<<<

            if event.type == pygame.USEREVENT and event.button == weapon_button:
                fade()
                DnD_Inv_1_menu()
                running = False

            if event.type == pygame.USEREVENT and event.button == simple_items_button:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == mg_inv_button:
                fade()
                DnD_Inv_3_menu()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in Buttons:
                btn.handle_event(event)

        # Апдейт кнопок
        if vol != prev_vol or prev_W != Width:
            arrow_left_button, arrow_right_button, back_button, weapon_button, simple_items_button, mg_inv_button = create_DnD_Inv_1_menu_buttons()
            Buttons = [arrow_left_button, arrow_right_button, back_button, weapon_button, simple_items_button,
                       mg_inv_button]
            prev_vol = vol
            prev_W = Width

        # update
        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def DnD_Inv_3_menu():
    pass

### Setting menu ###
def create_setting_menu_buttons():
    audio_button = ImageButton((Width - width_ic * 3) / 2, (Height - height_ic) / 2 - height_ic / 4 * 5, width_ic * 3,
                               height_ic, "", "image/n_h/audio.png", "image/h/audio_hovered.png",
                               "sound/test_sound1.mp3", vol)
    video_button = ImageButton((Width - width_ic * 3) / 2, (Height - height_ic) / 2, width_ic * 3, height_ic, "",
                               "image/n_h/resolithion.png", "image/h/resolithion_hovered.png", "sound/test_sound1.mp3",
                               vol)
    back_button = ImageButton((Width - width_ic * 3) / 2, (Height - height_ic) / 2 + height_ic / 4 * 5, width_ic * 3,
                              height_ic, "", "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    exit_button = ImageButton((Width - width_ic * 3) / 2, (Height - height_ic) / 2 + height_ic / 4 * 5 * 2, width_ic * 3,
                              height_ic, "", "image/h/exit_hovered.png", "image/h/exit_hovered.png",
                              "sound/test_sound1.mp3", vol)
    return audio_button, video_button, back_button, exit_button

def setting_menu():

    audio_button, video_button, back_button, exit_button = create_setting_menu_buttons()
    Buttons = [audio_button, video_button, back_button, exit_button]

    prev_vol = 0
    prev_W = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False
            #Возврат в меню через кнопку "Назад"
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            #Открытие экрана видео настроек
            if event.type == pygame.USEREVENT and event.button == video_button:
                fade()
                setting_video_menu()
            # Открытие экрана аудио настроек
            if event.type == pygame.USEREVENT and event.button == audio_button:
                fade()
                setting_audio_menu()

            for btn in Buttons:
                btn.handle_event(event)

        if prev_vol != vol or prev_W != Width:
            audio_button, video_button, back_button, exit_button = create_setting_menu_buttons()
            Buttons = [audio_button, video_button, back_button, exit_button]
            prev_vol = vol
            prev_W = Width

        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def create_setting_video_menu_buttons():
    b960x540_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 - 2 * (height_ic / 4 * 5), width_ic * 3,
                                  height_ic, "", "image/n_h/960x540.png", "image/h/960x540_hovered.png",
                                  "sound/test_sound1.mp3", vol)
    b1280x720_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 - height_ic / 4 * 5, width_ic * 3, height_ic,
                                   "", "image/n_h/1280x720.png", "image/h/1280x720_hovered.png",
                                   "sound/test_sound1.mp3", vol)
    Full_HD_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2, width_ic * 3, height_ic, "",
                                 "image/n_h/fullscreen.png", "image/h/fullscreen_hovered.png", "sound/test_sound1.mp3",
                                 vol)
    back_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 + height_ic / 4 * 5, width_ic * 3, height_ic, "",
                              "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3", vol)
    return b960x540_button, b1280x720_button, Full_HD_button, back_button

def setting_video_menu():

    b960x540_button, b1280x720_button, Full_HD_button, back_button = create_setting_video_menu_buttons()
    Buttons = [b960x540_button, b1280x720_button, Full_HD_button, back_button]

    prev_W = 0
    prev_vol = vol

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False
            #Возврат в меню настроек через кнопку "Назад"
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == b1280x720_button:
                change_screen_mode(1280, 720)
                running = False

            if event.type == pygame.USEREVENT and event.button == b960x540_button:
                change_screen_mode(960, 540)
                running = False

            if event.type == pygame.USEREVENT and event.button == Full_HD_button:
                change_screen_mode(1920, 1080, pygame.FULLSCREEN)
                running = False

            for btn in Buttons:
                btn.handle_event(event)

        if prev_vol != vol or prev_W != Width:
            b960x540_button, b1280x720_button, Full_HD_button, back_button = create_setting_video_menu_buttons()
            Buttons = [b960x540_button, b1280x720_button, Full_HD_button, back_button]
            prev_vol = vol
            prev_W = Width

        for btn in Buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def create_setting_audio_menu_buttons():
    plus_button = ImageButton(Width / 2 + width_ic * 2, Height / 2, width_ic, height_ic, "",
                              "image/Plus.png", "image/Plus.png", "sound/test_sound1.mp3", vol)
    minus_button = ImageButton(Width / 2 - width_ic * 3, Height / 2, width_ic, height_ic, "",
                               "image/Minus.png", "image/Minus.png", "sound/test_sound1.mp3", vol)
    back_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 + height_ic / 4 * 5, width_ic * 3, height_ic, "",
                              "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3", vol)
    return plus_button, minus_button, back_button

def setting_audio_menu():
    global vol
    plus_button, minus_button, back_button = create_setting_audio_menu_buttons()

    prev_W = Width

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Громкость", True, (255, 205, 205))
        text_rect = text_surface.get_rect(center=(Width / 2, (Height + height_ic) / 2))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False
            # Возврат в меню настроек через кнопку "Назад"
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == plus_button and vol < 1:
                vol += 0.1
                plus_button, minus_button, back_button = create_setting_audio_menu_buttons()
            if event.type == pygame.USEREVENT and event.button == minus_button and vol > 0:
                vol -= 0.1
                plus_button, minus_button, back_button = create_setting_audio_menu_buttons()

            for btn in [plus_button, minus_button, back_button]:
                btn.handle_event(event)

        if prev_W != Width:
            plus_button, minus_button, back_button = create_setting_audio_menu_buttons()
            prev_W = Width

        for btn in [plus_button, minus_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

#Затемнение при переходе между экранами
def fade():
    running = True
    fade_alpha = 0 #Уровень прозрачности анимации

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Сама анимация
        fade_surface = pygame.Surface((Width,Height))
        fade_surface.fill((0,0,0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        #Увеличение уровня прозрачности
        fade_alpha +=10
        if fade_alpha >= 115:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(Max_fps) #Максимум фпс при затухании

#Меняет размерность окна
#Параметры: ширина, высота, флаг фуллскрина
def change_screen_mode(w, h, f = 0):
    global main_background, screen, Width, Height, width_ic, height_ic
    Width, Height = w, h
    width_ic, height_ic = Width / 16, Height / 9
    main_background = pygame.transform.scale(main_background, (w, h))
    screen = pygame.display.set_mode((w, h), f)
    fade()

if __name__ == "__main__":
    main_menu()