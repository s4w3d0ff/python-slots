# python-slots [![Build Status](https://travis-ci.org/s4w3d0ff/python-slots.svg?branch=master)](https://travis-ci.org/s4w3d0ff/python-slots)
Simple, expandable, customizable slot machine

`pip install slotmachine`

```python
import slotmachine
slotM = slotmachine.SlotMachine()
print(slotM())
# [['!!!', 'BAR', '(M)']]

slotM = slotmachine.SlotMachine(size=(5,1))
print(slotM())
# [['(H)', '(N)', '!!!', '!!!', '(H)']]

slotM = slotmachine.SlotMachine(jack='BTC', bonus='LTC', size=(5,3))
print(slotM())
# [
#   ['(Z)', '(O)', '(X)', '(M)', '(Z)'],
#   ['(O)', '(Z)', '(H)', 'LTC', 'BTC'],
#   ['(H)', 'LTC', '(O)', '(M)', '(Z)']
# ]

print(slotM.reel)
# ['BTC', '(Z)', '(O)', '(H)', '(X)', '(W)', '(N)', '(M)', 'LTC', '(M)', '(N)', '(W)', '(X)', '(H)', '(O)', '(Z)', 'LTC', '(Z)', '(O)', '(H)', '(X)', '(W)', '(N)', '(M)', 'LTC', '(M)', '(N)', '(W)', '(X)', '(H)', '(O)', '(Z)', 'LTC', '(Z)', '(O)', '(H)', '(X)', '(W)', '(N)', '(M)', 'LTC', '(M)', '(N)', '(W)', '(X)', '(H)', '(O)', '(Z)']

slotM = slotmachine.SlotMachine(size=(5,1))
r = slotM()
print(r)
# [['(X)', '(W)', '(M)', '!!!', '(N)']]
print(slotM.checkLine(r[0]))
# False
r = slotM()
print(r)
# [['BAR', 'BAR', 'BAR', 'BAR', 'BAR']]
print(slotM.checkLine(r[0]))
# 'jackpot'
```
