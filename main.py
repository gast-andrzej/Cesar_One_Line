def cesar(z=input('message to code: '), n=int(input('value your Cesar'))): return print(f"{''.join(list(chr(ord(i)+n) for i in z))} \nThis same in numbers ord after cesar {list(ord(i)+n for i in z)}")
cesar()