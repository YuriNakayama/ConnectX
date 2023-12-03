import gym
from gym import wrappers

env = gym.make('CartPole-v0')
env = wrappers.Monitor(env, "./movie", force=True)
for i_episode in range(1):
    observation = env.reset()
    for t in range(1000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
