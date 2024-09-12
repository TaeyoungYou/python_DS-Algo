words = ['hello','my','name','is','taeyoung','you']
message = 'hlelo si tayeuong'

print("".join("".join(sorted(s)) for s in message.split()))