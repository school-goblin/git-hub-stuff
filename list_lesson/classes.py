from untensel import Untensil

fork = Untensil("fork", "metal")

spoon = Untensil("spoon", "plastic")

knife = Untensil("knife", "gold")

spork = Untensil("spork", "orphan bones")


print(fork.material)

print(knife.material)

print(spoon.material)

print(spork.material)

print()
knife.cut()

print()
fork.liftfood()

print()
spoon.liftfood()

print()
knife.liftfood()

print()
spork.liftfood()

print()

