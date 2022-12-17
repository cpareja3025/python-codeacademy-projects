def f_to_c(f_temp):
    return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
    return c_temp * (9/5) + 32

c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)

def get_force(mass, acc):
    return mass * acc

train_force = get_force(5, 2.5)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force")

def get_energy(mass, c = 3*10**8):
    return mass * c**2

bomb_energy = get_energy(1)
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")



def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance


train_work = get_work(1, 356, 32)
