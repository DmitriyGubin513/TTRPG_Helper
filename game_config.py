import pygame

vol=0.1

Max_fps = 60

Width, Height = 1280, 720

main_background = pygame.image.load("image/Background.png")
main_background = pygame.transform.scale(main_background, (Width, Height))

main_font = 'eberronrussian'

# Изображения кнопок
DnD_im1 = "image/n_h/DnD.png"
DnD_im2 = "image/h/DnD_hovered.png"
CR_im1 = "image/n_h/Cyber.png"
CR_im2 = "image/h/Cyber_hovered.png"
Init_im1 = "image/n_h/init.png"
Init_im2 = "image/h/init_hovered.png"
Save_im1 = "image/n_h/Save.png"
Save_im2 = "image/h/Save_hovered.png"
Bestiary_im1 = "image/n_h/Bestiary.png"
Bestiary_im2 = "image/h/Bestiary_hovered.png"
Spells_im1 = "image/n_h/Spells.png"
Spells_im2 = "image/h/Spells_hovered.png"
Item_im1 = "image/n_h/Items.png"
Item_im2 = "image/h/Items_hovered.png"
M_e_im1 = "image/n_h/monster_editor.png"
M_e_im2 = "image/h/monster_editor_hovered.png"
C_e_im1 = "image/n_h/character_editor.png"
C_e_im2 = "image/h/character_editor_hovered.png"
Settings_im1 = "image/h/Settings_hovered.png"
Settings_im2 = "image/n_h/Settings.png"

width_ic = Width/16
height_ic = Height / 9
