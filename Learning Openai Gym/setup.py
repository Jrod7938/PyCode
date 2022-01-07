import gym
import random

env = gym.make("CartPole-v1")

def Random_games():
    # Each of these episodes are their own game
    for episode in range(10):
        env.reset()
        # This is each frame, up to 500... but we wont make it that far with random.
        for t in range(500):
            # This will display the environment
            # Only display if ypu really want to see it.
            # Takes much longer to display it.
            env.render()

            # This will just create a simple action in any envirnment.
            # In this environment, the action can be 0 or 1, which is left or right
            action = env.action_space.sample()

            # This executes the environment with an action
            # and returns the observation of the environment,
            # the reward, if the env is over, and other info.
            next_state, reward, done, info = env.step(action)

            # lets print everything in one line:
            print(t, next_state, reward, done, info, action)
            if done:
                break

Random_games()