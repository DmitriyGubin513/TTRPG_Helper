import pygame

class ImageButton:
    # Инициализация.
    # Параметры: Координаты, Размер кнопки, текст на кнопке,
    # путь к изображению до нажатия и Путь после,
    # Путь к звуку, громкость звука
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None, vol=0.1):
        self.x = x
        self.y = y
        self.vol = vol
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width,height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
            self.sound.set_volume(vol)

        self.is_hovered = False

    #Создание кнопки (Картинка + Текст)
    #Передаётся экран для создания
    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        if self.text != "":
            font = pygame.font.SysFont('eberronrussian',36)
            text_surface = font.render(self.text, True,(255,205,205))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    #Определение наведена ли мышка на кнопку
    #Передаём позицию мыши
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    #Обработка событий
    #Получает event
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button = self))