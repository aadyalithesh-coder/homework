class dog:
    kingdom="animal"

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

labrador=dog("labrador","peach")
pug=dog("pug","brown")

print("{} is {}".format(labrador.breed,labrador.color))
print("{} is {}".format(pug.breed,pug.color))
