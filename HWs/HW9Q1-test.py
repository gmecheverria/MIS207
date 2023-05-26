from HW9_Q1 import lamp

state = lamp('off')
print(state._light)
state.switch()
print(state._light)


state = lamp('on')
print(state._light)
state.switch()
print(state._light)