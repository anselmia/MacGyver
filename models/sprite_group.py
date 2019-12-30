import pygame


class SpriteGroup(pygame.sprite.Group):
    def by_order(self, spr):
        return spr.order

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sorted(sprites, key=self.by_order):
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []