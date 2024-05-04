import pygame
import sys
from button import ImageButton
from game_config import *

pygame.init()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TTRPG Assist")
clock = pygame.time.Clock()

#Далее куча функций создающие разные меню
#К каждой меню прилагается функция <Название>_button, она генерит кнопки, нужно для адекватного отображения после
#изменения настроек



def create_main_menu_buttons():
    # Кнопки сюда, потом обновить в местах нужных
    DnD_button = ImageButton(width_ic, 0, width_ic, hight_ic, "", DnD_im1, DnD_im2, "sound/test_sound1.mp3", vol)
    CyberRed_button = ImageButton(width_ic * 2, 0, width_ic, hight_ic, "", CR_im1, CR_im2, "sound/test_sound1.mp3", vol)
    Initiative_button = ImageButton(width_ic * 3, 0, width_ic, hight_ic, "", Init_im1, Init_im2,
                                    "sound/test_sound1.mp3", vol)
    Save_button = ImageButton(width_ic * 4, 0, width_ic, hight_ic, "", Save_im1, Save_im2, "sound/test_sound1.mp3", vol)
    Settings_button = ImageButton(0, 0, width_ic, hight_ic, "", Settings_im1, Settings_im2, "sound/test_sound1.mp3",
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

            #Обработка нажатия на кнопку
            if event.type == pygame.USEREVENT and event.button == Settings_button:
                print("Настройки")
                fade()
                setting_menu()

            if event.type == pygame.USEREVENT and event.button == DnD_button:
                print("DnD_button down")
                DnD_menu()

            if event.type == pygame.USEREVENT and event.button == CyberRed_button:
                print("CyberRed_button down")
                Cyberpunk_menu()

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
    DnD_button = ImageButton(width_ic, 0, width_ic, hight_ic, "", DnD_im1, DnD_im2, "sound/test_sound1.mp3", vol)
    CyberRed_button = ImageButton(width_ic * 2, 0, width_ic, hight_ic, "", CR_im1, CR_im2, "sound/test_sound1.mp3", vol)
    Initiative_button = ImageButton(width_ic * 3, 0, width_ic, hight_ic, "", Init_im1, Init_im2,
                                    "sound/test_sound1.mp3", vol)
    Save_button = ImageButton(width_ic * 4, 0, width_ic, hight_ic, "", Save_im1, Save_im2, "sound/test_sound1.mp3", vol)
    cr_Bestiary_button = ImageButton(0, hight_ic, width_ic * 6, hight_ic * 4, "", Bestiary_im1, Bestiary_im2,
                                  "sound/test_sound1.mp3", vol)
    cr_Monster_edit_button = ImageButton(0, hight_ic + hight_ic * 4, width_ic * 6, hight_ic * 4, "", M_e_im1, M_e_im2,
                                      "sound/test_sound1.mp3", vol)
    cr_Spells_button = ImageButton(width_ic * 6, hight_ic, width_ic * 4, hight_ic * 4, "", Spells_im1, Spells_im2,
                                "sound/test_sound1.mp3", vol)
    cr_Items_button = ImageButton(width_ic * 6, hight_ic + hight_ic * 4, width_ic * 4, hight_ic * 4, "", Item_im1,
                               Item_im2, "sound/test_sound1.mp3", vol)
    cr_Char_edit_button = ImageButton(width_ic * 6 + width_ic * 4, 0, width_ic * 6, Height, "", C_e_im1, C_e_im2,
                                   "sound/test_sound1.mp3", vol)
    Settings_button = ImageButton(0, 0, width_ic, hight_ic, "", Settings_im1, Settings_im2, "sound/test_sound1.mp3",
                                  vol)
    return DnD_button, CyberRed_button, Initiative_button, Save_button, cr_Bestiary_button, cr_Monster_edit_button, cr_Spells_button, cr_Items_button, cr_Char_edit_button, Settings_button

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

### DnD_menu ###

def create_DnD_menu_buttons():
    DnD_button = ImageButton(width_ic, 0, width_ic, hight_ic, "", DnD_im1, DnD_im2, "sound/test_sound1.mp3", vol)
    CyberRed_button = ImageButton(width_ic * 2, 0, width_ic, hight_ic, "", CR_im1, CR_im2, "sound/test_sound1.mp3", vol)
    Initiative_button = ImageButton(width_ic * 3, 0, width_ic, hight_ic, "", Init_im1, Init_im2, "sound/test_sound1.mp3", vol)
    Save_button = ImageButton(width_ic * 4, 0, width_ic, hight_ic, "", Save_im1, Save_im2, "sound/test_sound1.mp3", vol)
    Bestiary_button = ImageButton(0, hight_ic, width_ic * 6, hight_ic * 4, "", Bestiary_im1, Bestiary_im2, "sound/test_sound1.mp3", vol)
    Monster_edit_button = ImageButton(0, hight_ic + hight_ic * 4, width_ic * 6, hight_ic * 4, "", M_e_im1, M_e_im2, "sound/test_sound1.mp3", vol)
    Spells_button = ImageButton(width_ic * 6, hight_ic, width_ic * 4, hight_ic * 4, "", Spells_im1, Spells_im2, "sound/test_sound1.mp3", vol)
    Items_button = ImageButton(width_ic * 6, hight_ic + hight_ic * 4, width_ic * 4, hight_ic * 4, "", Item_im1, Item_im2, "sound/test_sound1.mp3", vol)
    Char_edit_button = ImageButton(width_ic * 6 + width_ic * 4, 0, width_ic * 6, Height, "", C_e_im1, C_e_im2,"sound/test_sound1.mp3", vol)
    Settings_button = ImageButton(0,0,width_ic, hight_ic, "", Settings_im1, Settings_im2, "sound/test_sound1.mp3", vol)
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

def create_DnD_char_edit_menu_buttons():
    back_button = ImageButton(Width - width_ic * 2, Height - hight_ic, width_ic * 2, hight_ic, "", "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    comming_soon_button = ImageButton(width_ic, hight_ic, Width - width_ic * 3, Height - hight_ic * 2, "","image/coming_soon.png", "image/coming_soon.png", "sound/rick.mp3", vol)
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
    weapon_button = ImageButton(0, 0, width_ic * 2, hight_ic,"1", "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    simple_items_button = ImageButton(width_ic * 2, 0, width_ic * 2, hight_ic, "2", "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    mg_inv_button = ImageButton(width_ic * 4, 0, width_ic * 2, hight_ic, "3", "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    back_button = ImageButton(Width - width_ic * 1.6, Height - hight_ic * 0.8, width_ic * 1.6, hight_ic * 0.8, "", "image/n_h/back.png",
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
    arrow_left_button = ImageButton(0, (Height - hight_ic) / 2, width_ic, hight_ic, "", "image/n_h/back.png",
                              "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    arrow_right_button = ImageButton(Width-width_ic, (Height - hight_ic) / 2, width_ic, hight_ic, "", "image/n_h/back.png",
                              "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    back_button = ImageButton(Width - width_ic * 1.6, Height - hight_ic * 0.8, width_ic * 1.6, hight_ic * 0.8, "", "image/n_h/back.png",
                              "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    weapon_button = ImageButton(0, 0, width_ic * 2, hight_ic, "1", "image/n_h/back.png", "image/h/back_hovered.png",
                                "sound/test_sound1.mp3",
                                vol)
    simple_items_button = ImageButton(width_ic * 2, 0, width_ic * 2, hight_ic, "2", "image/n_h/back.png",
                                      "image/h/back_hovered.png", "sound/test_sound1.mp3",
                                      vol)
    mg_inv_button = ImageButton(width_ic * 4, 0, width_ic * 2, hight_ic, "3", "image/n_h/back.png",
                                "image/h/back_hovered.png", "sound/test_sound1.mp3",
                                vol)
    return arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button

def DnD_Inv_1_menu():
    arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button = create_DnD_Inv_1_menu_buttons()
    Buttons = [arrow_left_button, arrow_right_button, back_button,weapon_button, simple_items_button, mg_inv_button]

    prev_W = 0
    prev_vol = 0

    weapon_image = pygame.image.load("image/Weapons/Weapon1.png")
    counter = 1
    weapon_image_rect = (Width - width_ic * 14.5, Height - hight_ic * 7.8)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        weapon_image = pygame.transform.scale(weapon_image,(Width - width_ic * 3, Height - hight_ic * 2))
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
    weapon_image_rect = (Width - width_ic * 14.5, Height - hight_ic * 7.8)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        weapon_image = pygame.transform.scale(weapon_image, (Width - width_ic * 3, Height - hight_ic * 2))
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
    audio_button = ImageButton((Width - width_ic * 3) / 2, (Height - hight_ic) / 2 - hight_ic / 4 * 5, width_ic * 3,
                               hight_ic, "", "image/n_h/audio.png", "image/h/audio_hovered.png",
                               "sound/test_sound1.mp3", vol)
    video_button = ImageButton((Width - width_ic * 3) / 2, (Height - hight_ic) / 2, width_ic * 3, hight_ic, "",
                               "image/n_h/resolithion.png", "image/h/resolithion_hovered.png", "sound/test_sound1.mp3",
                               vol)
    back_button = ImageButton((Width - width_ic * 3) / 2, (Height - hight_ic) / 2 + hight_ic / 4 * 5, width_ic * 3,
                              hight_ic, "", "image/n_h/back.png", "image/h/back_hovered.png", "sound/test_sound1.mp3",
                              vol)
    exit_button = ImageButton((Width - width_ic * 3) / 2, (Height - hight_ic) / 2 + hight_ic / 4 * 5 * 2, width_ic * 3,
                              hight_ic, "", "image/h/exit_hovered.png", "image/h/exit_hovered.png",
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
    b960x540_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 - 2 * (hight_ic / 4 * 5), width_ic * 3,
                                  hight_ic, "", "image/n_h/960x540.png", "image/h/960x540_hovered.png",
                                  "sound/test_sound1.mp3", vol)
    b1280x720_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 - hight_ic / 4 * 5, width_ic * 3, hight_ic,
                                   "", "image/n_h/1280x720.png", "image/h/1280x720_hovered.png",
                                   "sound/test_sound1.mp3", vol)
    Full_HD_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2, width_ic * 3, hight_ic, "",
                                 "image/n_h/fullscreen.png", "image/h/fullscreen_hovered.png", "sound/test_sound1.mp3",
                                 vol)
    back_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 + hight_ic / 4 * 5, width_ic * 3, hight_ic, "",
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
    plus_button = ImageButton(Width / 2 + width_ic * 2, Height / 2, width_ic, hight_ic, "",
                              "image/Plus.png", "image/Plus.png", "sound/test_sound1.mp3", vol)
    minus_button = ImageButton(Width / 2 - width_ic * 3, Height / 2, width_ic, hight_ic, "",
                               "image/Minus.png", "image/Minus.png", "sound/test_sound1.mp3", vol)
    back_button = ImageButton(Width / 2 - width_ic * 3 / 2, Height / 2 + hight_ic / 4 * 5, width_ic * 3, hight_ic, "",
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
        text_rect = text_surface.get_rect(center=(Width / 2, (Height+hight_ic) / 2))
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
    global main_background, screen, Width, Height, width_ic, hight_ic
    Width, Height = w, h
    width_ic, hight_ic = Width / 16, Height / 9
    main_background = pygame.transform.scale(main_background, (w, h))
    screen = pygame.display.set_mode((w, h), f)
    fade()

if __name__ == "__main__":
    main_menu()

