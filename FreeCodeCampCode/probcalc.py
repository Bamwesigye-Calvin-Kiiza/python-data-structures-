import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents
        else:
            drawn_balls = random.sample(self.contents, num_balls_drawn)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        drawn_balls = copied_hat.draw(num_balls_drawn)
        drawn_balls_count = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}
        success = all(drawn_balls_count.get(color, 0) >= expected_balls.get(color, 0) for color in expected_balls)
        if success:
            success_count += 1
    return success_count / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)
print("Estimated Probability:", probability)
