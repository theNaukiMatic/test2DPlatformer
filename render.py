import pygame


class Animation():
    def __init__(self, images):
        self.imageList = images
        self.currentImage = 0
        self.counter = 0
        self.animationSpeed = 4

    def update(self):
        self.counter += 1
        if self.counter >= self.animationSpeed:
            self.counter = 0
            self.currentImage += 1
            if self.currentImage > len(self.imageList) - 1:
                self.currentImage = 0

    def draw(self, screen, x, y, isFlipped):

        if isFlipped:
            screen.blit(pygame.transform.flip(
                self.imageList[self.currentImage], True, False), (x, y))
        else:
            screen.blit(self.imageList[self.currentImage], (x, y))

    def setAnimationSpeed(self, speed):
        self.animationSpeed = speed
