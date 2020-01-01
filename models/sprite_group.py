''' Import needed in the module '''
import pygame


class SpriteGroup(pygame.sprite.Group):
    ''' SubClass from sprite.Group used to redefine draw method '''

    @classmethod
    def by_order(cls, spr):
        ''' Return order attribute from instance '''

        return spr.order

    def draw(self, surface):
        ''' Draw sprite on screen by their order attribute '''

        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sorted(sprites, key=self.by_order):
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
