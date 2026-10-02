import time

population = int(input("Population: "))
infection_rate = int(input("Infection Rate: "))
infected = int(input("Infected Start: "))
generations = int(input("Generations to run: "))
healthy = population - infected
remainder = 0

print("---------------")


def simulation(generations, infected, infection_rate, healthy, remainder):
    while generations > 0:

        new_infections = healthy * (infection_rate / 100)
        whole_infections = int(new_infections)
        decimal_part = new_infections - whole_infections

        infected += whole_infections
        remainder += decimal_part

        if remainder >= 1:
            infected += 1
            remainder -= 1

        healthy = population - infected
        print(f"Generation: {generations}")
        generations -= 1
        print(f"Infected: {infected}")
        print(f"Healthy: {healthy}")
        print(f"Remainder: {remainder}")
        print("---------------")
        time.sleep(2)
        if healthy <= 0:
            break


simulation(generations, infected, infection_rate, healthy, remainder)
