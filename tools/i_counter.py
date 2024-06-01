import pygame
import sys
from game_config import *


class DataRow:
    is_friend = True
    initiative = 0
    name = ""
    health_points = 0
    armor = 0
    bonus = 0

    def __init__(self, is_friend, initiative="", name="", health_point="", armor="", bonus=""):
        self.is_friend = is_friend
        self.initiative = initiative
        self.name = name
        self.health_points = health_point
        self.armor = armor
        self.bonus = bonus

    def set_value_initiative(self, val):
        self.initiative = val
        return self.initiative

    def set_value_health_points(self, val):
        self.health_points = val
        return self.health_points

    def set_value_armor(self, val):
        self.armor = val
        return self.armor

    def set_value_bonus(self, val):
        self.bonus = val
        return self.bonus

    def set_name(self, temp):
        self.name = temp
        return self.name


class InitiativeCounter:
    # Нужно 4 текстовых поля и 1 целочисленное и 1 булеево поле итого 6
    # Массив
    rows: [DataRow] = []
    background_img = "image/container_green.png"
    background_enemy_img = "image/container_red.png"
    to_edit: (int, int) = None


    def add_row(self, is_friend: bool = True):
        self.rows.append(DataRow(is_friend))

    def delete_all_rows(self):
        self.rows.clear()

    def kill_zero(self):
        temp = []
        for i, row in enumerate(self.rows):
            if row.health_points != "0":
                temp.append(row)
        self.rows = temp


    def sort(self):
        print("Ку", " ".join(i.initiative for i in self.rows))
        self.rows.sort(key=lambda r: r.initiative, reverse=True)

    def draw_row(self, screen, x, y, row: DataRow):
        font = pygame.font.SysFont('eberronrussian', 36)
        background = pygame.image.load(self.background_img if row.is_friend else self.background_enemy_img)
        background = pygame.transform.scale(background, (width_ic * 11, height_ic / 2))
        rect = background.get_rect(topleft=(x, y))
        screen.blit(background, rect.topleft)
        text_x, text_y = x + 10, y
        text_i = font.render(str(row.initiative), True,(255,205,205))
        text_i_rect = text_i.get_rect(topleft=(text_x + 5, text_y))
        screen.blit(text_i, text_i_rect)
        text_n = font.render(row.name, True, (255,205,205))
        text_n_rect = text_n.get_rect(topleft=(width_ic + text_x, text_y))
        screen.blit(text_n, text_n_rect)
        text_hp = font.render(str(row.health_points), True, (255, 205, 205))
        text_hp_rect = text_hp.get_rect(topleft=(width_ic * 7 + text_x, text_y))
        screen.blit(text_hp, text_hp_rect)
        text_a = font.render(str(row.armor), True, (255, 205, 205))
        text_a_rect = text_a.get_rect(topleft=(width_ic * 8 + text_x, text_y))
        screen.blit(text_a, text_a_rect)
        text_b = font.render(str(row.bonus), True, (255, 205, 205))
        text_b_rect = text_b.get_rect(topleft=(width_ic * 9 + text_x, text_y))
        screen.blit(text_b, text_b_rect)

    def draw_rows(self, screen, x=width_ic*5, y=10):
        for i, row in enumerate(self.rows):
            self.draw_row(screen, x, y + (i * height_ic / 2), row)

    def update(self, screen):
        self.draw_rows(screen)

    def handle_click(self, pos, screen):
        if len(self.rows) == 0:
            self.to_edit = None
            return
        if pos[1]<=10 or pos[1] >= 10 + height_ic / 2 * len(self.rows) or pos[0] <= width_ic * 5:
            self.to_edit = None
            return
        num = int((pos[1]-10)/(height_ic/2))
        num_x = int((pos[0]-width_ic*5)/width_ic)
        num_x = 0 if num_x==0 else (1 if num_x < 7 else (2 if num_x == 7 else (3 if num_x == 8 else 4)))
        print(num)
        print(num_x)
        print(pos)
        self.to_edit = (num_x, num)

    def edit_your_put_in(self, index, val, row):
        is_backspace = val == "\x08"
        if index == 0:
            temp = str(row.initiative) + val if not is_backspace else str(row.initiative)[:-1]
            row.set_value_initiative(temp)
        elif index == 1:
            temp = str(row.name) + val if not is_backspace else str(row.name)[:-1]
            row.set_name(temp)
        elif index == 2:
            temp = str(row.health_points) + val if not is_backspace else str(row.health_points)[:-1]
            row.set_value_health_points(temp)
        elif index == 3:
            temp = str(row.armor) + val if not is_backspace else str(row.armor)[:-1]
            row.set_value_armor(temp)
        else:
            temp = str(row.bonus) + val if not is_backspace else str(row.bonus)[:-1]
            row.set_value_bonus(temp)