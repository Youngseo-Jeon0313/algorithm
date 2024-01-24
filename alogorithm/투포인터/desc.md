```python
while start<end:
  	Sum = array[start] + array[end]
  	if Sum > target:
			start += 1
      elif Sum < target:
      	end -= 1
      else:
      	count += 1
          start += 1
          end -= 1
```
### testcase
경계값 되는 경우를 넣어보자 !   
예를 들어 펠린드롬일 경우   
abba ->    
ababa ->   

