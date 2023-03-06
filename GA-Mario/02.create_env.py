# 02. create_env
# 게임 환경 생성
import retro
env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()     #게임을 껐다키는 것