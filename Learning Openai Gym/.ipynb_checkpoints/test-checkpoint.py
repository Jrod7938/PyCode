#https://www.youtube.com/watch?v=cO5g5qLrLSo
import gym
import random
import numpy as np
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.python.keras.layers.core import Activation
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from tensorflow.python.util import memory

env = gym.make("CartPole-v0")
states = env.observation_space.shape[0]
actions = env.action_space.n
episodes = 10

for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([0,1])
        n_state, reward, done, info = env.step(action)
        score += reward
    print(f"Episode: {episode} Score:{score}")

def build_model(states,actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1, states)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model 

model = build_model(states, actions)
model.summary()

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)

scores = dqn.test(env, nb_episodes=100, visualize=True)
print(np.mean(scores.history['episode_reward']))

dqn.save_weights('dqn_weights.h5f', overwrite=True)

#env = gym.make('CartPole-v0')
#actions = env.action_space.n
#states = env.observation_space.shape[0]
#model = build_model(states, actions)
#dqn = build_agent(model, actions)
#dqn.compile(Adam(lr=1e-3), metrics=['mae'])

#dqn.load_weights('dqn_weights.h5f')

#dqn.test(env, nb_episodes=5, visualize=True)