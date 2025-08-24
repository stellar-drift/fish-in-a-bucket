import pygame

class DisplayCounter:
    def __init__(self, font_size=18, padding=4, bg_color="#011925", text_color = "#fffdd0"):
        self.font = pygame.font.SysFont("Courier New", font_size, bold=True)
        self.padding = padding
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self, screen, total_collected):
        counter_text = self.font.render(f"Fish: {total_collected}", True, self.text_color)
        text_rect = screen.blit(counter_text, (10,10))

        # background rectangle
        bg_rect = pygame.Rect(
            text_rect.left - self.padding,
            text_rect.top - self.padding,
            text_rect.width + 2*self.padding,
            text_rect.height + 2*self.padding
        )

        pygame.draw.rect(screen, self.bg_color, bg_rect)

        screen.blit(counter_text, text_rect)